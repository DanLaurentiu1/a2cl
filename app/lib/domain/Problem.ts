import { Topic, TopicJSON } from "./Topic";

export interface ProblemJSON {
  id: number;
  name: string;
  topics: Array<TopicJSON>;
  difficulty: 0 | 1 | 2;
  acceptanceRate: number;
}

export class Problem {
  public constructor(
    private readonly _id: number,
    private readonly _name: string,
    private readonly _topics: Array<Topic>,
    private readonly _difficulty: 0 | 1 | 2,
    private readonly _acceptanceRate: number
  ) {}

  // ====================
  // Public API
  // ====================

  public get id(): number {
    return this._id;
  }

  public get name(): string {
    return this._name;
  }

  public get topics(): ReadonlyArray<Topic> {
    return this._topics;
  }

  public get difficulty(): 0 | 1 | 2 {
    return this._difficulty;
  }

  public get acceptanceRate(): number {
    return this._acceptanceRate;
  }

  // ====================
  // Domain Methods
  // ====================

  public toJSON(): ProblemJSON {
    return {
      id: this._id,
      name: this._name,
      topics: this._topics.map((topic) => topic.toJSON()),
      difficulty: this._difficulty,
      acceptanceRate: this._acceptanceRate,
    };
  }

  static fromJSON(json: ProblemJSON): Problem {
    if (
      !json?.id ||
      !json?.name ||
      json.difficulty === undefined ||
      json.acceptanceRate === undefined
    ) {
      throw new Error("Invalid Problem JSON");
    }

    return new Problem(
      json.id,
      json.name,
      json.topics.map((topicJson) => Topic.fromJSON(topicJson)),
      json.difficulty,
      json.acceptanceRate
    );
  }

  public toString(): string {
    return `Problem(id:${this._id}, name:${this._name}, topics:${this._topics}, difficulty:${this._difficulty}, acceptanceRate:${this._acceptanceRate})`;
  }
}
