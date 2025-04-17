export interface TopicJSON {
  name: string;
  type: TopicTypes;
}

export enum TopicTypes {
  DataStructures = "DataStructures",
  Algorithms = "Algorithms",
  Concepts = "Concepts",
  Miscellaneous = "Miscellaneous",
}

export class Topic {
  public constructor(
    private readonly _name: string,
    private readonly _type: TopicTypes
  ) {}

  // ====================
  // Public API
  // ====================

  public get name(): string {
    return this._name;
  }

  public get type(): TopicTypes {
    return this._type;
  }

  // ====================
  // Domain Methods
  // ====================

  public toJSON(): TopicJSON {
    return {
      name: this._name,
      type: this._type,
    };
  }

  static fromJSON(json: TopicJSON): Topic {
    if (!json?.name || json.type === undefined) {
      throw new Error("Invalid Topic JSON");
    }
    return new Topic(json.name, json.type);
  }

  public toString(): string {
    return `Topic(name:${this._name}, type:${this._type})`;
  }
}
