import { topicRepository } from "../repository/TopicRepository";
import { Topic } from "./Topic";

const defaultProficiencies: Map<Topic, number> = new Map(
  topicRepository.getAllTopics().map((topic) => [topic, 0])
);

export class Profile {
  private _name: string;
  private _proficiencies: Map<Topic, number>;
  private _fromLeetcode: boolean;

  constructor(
    name: string,
    fromLeetcode: boolean,
    proficiencies: Map<Topic, number> = defaultProficiencies
  ) {
    this._name = name;
    this._proficiencies = proficiencies;
    this._fromLeetcode = fromLeetcode;
  }

  public get name(): string {
    return this._name;
  }

  public set name(newName: string) {
    if (newName === null) {
      throw new Error("Name cannot be null");
    }
    this._name = newName;
  }

  public get proficiencies(): Map<Topic, number> {
    return this._proficiencies;
  }

  public set proficiencies(newProficiencies: Map<Topic, number>) {
    if (newProficiencies === null) {
      throw new Error("Proficiencies cannot be null");
    }
    this._proficiencies = newProficiencies;
  }

  public get fromLeetcode(): boolean {
    return this._fromLeetcode;
  }

  private set fromLeetcode(newFromLeetcode: boolean) {
    if (newFromLeetcode === null) {
      throw new Error("FromLeetcode cannot be null");
    }
    this._fromLeetcode = newFromLeetcode;
  }

  public toString(): string {
    return `Profile(name:${this._name}, proficiencies:${this._proficiencies}, fromLeetcode:${this._fromLeetcode})`;
  }
}
