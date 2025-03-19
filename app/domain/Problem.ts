import { Topic } from "./Topic";

export class Problem {
  private _id: number;
  private _name: string;
  private _topics: Array<Topic>;
  private _difficulty: 0 | 1 | 2;
  private _acceptanceRate: number;

  constructor(
    id: number,
    name: string,
    topics: Array<Topic>,
    difficulty: 0 | 1 | 2,
    acceptanceRate: number
  ) {
    this._id = id;
    this._name = name;
    this._topics = topics;
    this._difficulty = difficulty;
    this._acceptanceRate = acceptanceRate;
  }

  public get id(): bigint {
    return this.id;
  }

  public get name(): string {
    return this.name;
  }

  public get topics(): string {
    return this.topics;
  }

  public get difficulty(): string {
    return this.difficulty;
  }

  public get acceptanceRate(): string {
    return this.acceptanceRate;
  }

  public set id(newId: number) {
    if (newId < 0) {
      throw new Error("Id cannot be negative");
    }
    this._id = newId;
  }

  public set name(newName: string) {
    if (newName === null) {
      throw new Error("Name cannot be null");
    }
    this._name = newName;
  }

  private set topics(newTopics: Array<Topic>) {
    this.topics = newTopics;
  }

  private set difficulty(newDifficulty: 0 | 1 | 2) {
    this._difficulty = newDifficulty;
  }

  private set acceptanceRate(newAcceptanceRate: number) {
    if (newAcceptanceRate < 0 || newAcceptanceRate > 100) {
      throw new Error("Acceptance rate is a percentage between 0 and 100");
    }
    this._acceptanceRate = newAcceptanceRate;
  }

  public toString(): string {
    return `Problem(id:${this._id}, name:${this._name}, topics:${this._topics}, difficulty:${this._difficulty}, acceptanceRate:${this._acceptanceRate})`;
  }
}
