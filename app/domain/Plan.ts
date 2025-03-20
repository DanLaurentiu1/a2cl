import { Problem } from "./Problem";
import { Profile } from "./Profile";
import { Topic } from "./Topic";

export class Plan {
  private _id: number;
  private _title: string;
  private _profile: Profile;
  private _problems: Array<[boolean, Problem]>;
  private _topics: Set<Topic>;

  constructor(
    id: number,
    title: string,
    profile: Profile,
    problems: Array<[boolean, Problem]>
  ) {
    this._id = id;
    this._title = title;
    this._profile = profile;
    this._problems = problems;
    this._topics = new Set();
    this.initializeTopicSet();
  }

  public initializeTopicSet() {
    for (let i = 0; i < this._problems.length; i++) {
      const [isDone, problem] = this._problems[i];
      for (let j = 0; j < problem.topics.length; j++) {
        const topic: Topic = problem.topics[j];
        this._topics.add(topic);
      }
    }
  }

  public get id(): number {
    return this._id;
  }

  public set id(newId: number) {
    if (newId < 0) {
      throw new Error("Value cannot be negative.");
    }
    this._id = newId;
  }

  public get title(): string {
    return this._title;
  }

  public set title(newTitle: string) {
    if (newTitle.length > 100) {
      throw new Error("Length of title exceeeds 100 characters.");
    }
    if (newTitle === null) {
      throw new Error("Title cannot be null.");
    }
    this._title = newTitle;
  }

  public get profile(): Profile {
    return this._profile;
  }

  private set profile(newProfile: Profile) {
    this._profile = newProfile;
  }

  public get problems(): Array<[boolean, Problem]> {
    return this._problems;
  }

  private set problems(newProblems: Array<[boolean, Problem]>) {
    this._problems = newProblems;
  }

  public get topics(): Set<Topic> {
    return this._topics;
  }

  public updateProblemDone(id: number) {
    for (let i = 0; i < this._problems.length; i++) {
      const [isDone, problem] = this._problems[i];
      if (problem.id === id) {
        this._problems[i][0] = !isDone;
        break;
      }
    }
  }

  public getPercentageCompleted(): number {
    let counter: number = 0;
    for (let i = 0; i < this._problems.length; i++) {
      const [isDone, problem] = this._problems[i];
      if (isDone === true) {
        counter += 1;
      }
    }
    return (counter / this._problems.length) * 100;
  }

  public toString(): string {
    return `Plan(id:${this._id}, title:${this._title}, profile:${this._profile}, problems:${this._problems})`;
  }
}
