import { Problem, ProblemJSON } from "./Problem";
import { Profile, ProfileJSON } from "./Profile";
import { Topic, TopicJSON } from "./Topic";

export interface PlanJSON {
  id: number;
  title: string;
  profile: ProfileJSON;
  problems: Array<[boolean, ProblemJSON]>;
  topics?: Array<TopicJSON>;
  given_topics: Array<TopicJSON>;
}

export class Plan {
  private readonly _topics: Set<Topic>;

  public constructor(
    private readonly _id: number,
    private _title: string,
    private readonly _profile: Profile,
    private _problems: Array<[boolean, Problem]> = [],
    private _given_topics: Array<Topic> = []
  ) {
    this._topics = this.calculateTopics();
  }

  // ====================
  // Public API
  // ====================

  public get id(): number {
    return this._id;
  }

  public get title(): string {
    return this._title;
  }

  public get profile(): Profile {
    return this._profile;
  }

  public get problems(): Array<[boolean, Problem]> {
    return [...this._problems] as const;
  }

  public get given_topics(): Array<Topic> {
    return [...this._given_topics] as const;
  }

  public get topics(): ReadonlySet<Topic> {
    return new Set(this._topics);
  }

  // ====================
  // Domain Methods
  // ====================

  public updateTitle(newTitle: string): void {
    this._title = newTitle;
  }

  public getProblemById(problemId: number): [boolean, Problem] | undefined {
    const result = this._problems.find(
      (problem) => problem[1].id === problemId
    );
    if (result === undefined) {
      throw new Error(`Problem ${problemId} not found in plan`);
    }
    return result;
  }

  public toggleProblemCompletion(problemId: number): void {
    const problemIndex = this._problems.findIndex(
      ([_, problem]) => problem.id === problemId
    );
    if (problemIndex === -1) {
      throw new Error(`Problem ${problemId} not found in plan`);
    }
    this._problems[problemIndex][0] = !this._problems[problemIndex][0];
  }

  public getPercentageCompleted(): number {
    if (this._problems.length === 0) return 0;
    const completedCount = this._problems.reduce(
      (count, [isDone]) => (isDone ? count + 1 : count),
      0
    );
    return Math.round((completedCount / this._problems.length) * 100);
  }

  public toJSON(): PlanJSON {
    return {
      id: this._id,
      title: this._title,
      profile: this._profile.toJSON(),
      problems: this._problems.map(([completed, problem]) => [
        completed,
        problem.toJSON(),
      ]),
      topics: Array.from(this._topics).map((topic) => topic.toJSON()),
      given_topics: Array.from(this._given_topics).map((topic) => topic.toJSON()),
    };
  }

  static fromJSON(json: PlanJSON): Plan {
    if (
      json?.id === undefined ||
      json?.id === null ||
      json?.title === undefined ||
      json?.title === null ||
      json?.profile === null ||
      json?.profile === undefined ||
      json?.given_topics === null ||
      json?.given_topics === undefined
    ) {
      throw new Error("Invalid Plan JSON");
    }
    const problems = (json.problems || []).map(([completed, problemJson]) => [
      completed,
      Problem.fromJSON(problemJson),
    ]) as Array<[boolean, Problem]>;

    const given_topics = (json.given_topics || []).map(topic_json => Topic.fromJSON(topic_json)) as Array<Topic>;
    const plan = new Plan(
      json.id,
      json.title,
      Profile.fromJSON(json.profile),
      problems,
      given_topics
    );

    if (json.topics) {
      (plan as any)._topics = new Set(
        json.topics.map((topicJson) => Topic.fromJSON(topicJson))
      );
    }

    Object.setPrototypeOf(plan, Plan.prototype);
    return plan;
  }

  public toString(): string {
    return `Plan(id:${this._id}, title:${this._title}, profile:${this._profile}, problems:${this._problems}, given_topics:${this._given_topics})`;
  }

  // ====================
  // Private Helpers
  // ====================

  private calculateTopics(): Set<Topic> {
    const topics = new Set<Topic>();
    this._problems.forEach(([_, problem]) => {
      problem.topics.forEach((topic) => topics.add(topic));
    });
    return topics;
  }
}
