import { ALL_TOPICS } from "../shared/data/topics";
import { Topic } from "./Topic";

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
