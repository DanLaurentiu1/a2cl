import { ALL_TOPICS } from "../shared/data/topics";
import { Topic, TopicJSON } from "./Topic";

export interface ProfileJSON {
  name: string;
  fromLeetcode: boolean;
  proficiencies: [TopicJSON, number][];
}

export class Profile {
  private readonly _proficiencies: Map<Topic, number>;
  public constructor(
    private readonly _name: string,
    private readonly _fromLeetcode: boolean
  ) {
    this._proficiencies = this.createDefaultProficiencies();
  }

  // ====================
  // Public API
  // ====================

  public get name(): string {
    return this._name;
  }

  public get proficiencies(): Map<Topic, number> {
    return this._proficiencies;
  }

  public get fromLeetcode(): boolean {
    return this._fromLeetcode;
  }

  // ====================
  // Domain Methods
  // ====================

  public toJSON(): ProfileJSON {
    return {
      name: this._name,
      fromLeetcode: this._fromLeetcode,
      proficiencies: Array.from(this._proficiencies.entries()).map(
        ([topic, value]) => [topic.toJSON(), value]
      ),
    };
  }

  static fromJSON(json: ProfileJSON): Profile {
    if (!json?.name || json.fromLeetcode === undefined) {
      throw new Error("Invalid Profile JSON");
    }

    const profile = new Profile(json.name, json.fromLeetcode);

    if (json.proficiencies) {
      (profile as any)._proficiencies = new Map(
        json.proficiencies.map(([topicJson, value]) => [
          Topic.fromJSON(topicJson),
          value,
        ])
      );
    }

    return profile;
  }

  public toString(): string {
    return `Profile(name:${this._name}, proficiencies:${this._proficiencies}, fromLeetcode:${this._fromLeetcode})`;
  }

  // ====================
  // Private Helpers
  // ====================

  private createDefaultProficiencies(): Map<Topic, number> {
    const defaultProficiencies = new Map<Topic, number>();
    ALL_TOPICS.forEach((topic) => defaultProficiencies.set(topic, 0));
    return defaultProficiencies;
  }
}
