export enum TopicTypes {
  DataStructures,
  Algorithms,
  Concepts,
  Miscellaneous,
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

  public toString(): string {
    return `Topic(name:${this._name}, type:${this._type})`;
  }
}
