export enum TopicTypes {
  DataStructures,
  Algorithms,
  Concepts,
  Miscellaneous,
}

export class Topic {
  private _name: string;
  private _type: TopicTypes;

  constructor(name: string, type: TopicTypes) {
    this._name = name;
    this._type = type;
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

  public get type(): TopicTypes {
    return this._type;
  }

  public set type(newType: TopicTypes) {
    this._type = newType;
  }

  public toString(): string {
    return `Topic(name:${this._name}, type:${this._type})`;
  }
}
