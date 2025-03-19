export enum TopicTypes {
  DataStructures,
  Algorithms,
  Concepts,
  Miscellaneous,
}

export class Topic {
  private _id: number;
  private _name: string;
  private _type: TopicTypes;

  constructor(id: number, name: string, type: TopicTypes) {
    this._id = id;
    this._name = name;
    this._type = type;
  }

  public get id(): number {
    return this._id;
  }

  public set id(newId: number) {
    if (newId < 0) {
      throw new Error("Id cannot be negative");
    }
    this._id = newId;
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
    return `Topic(id:${this._id}, name:${this._name}, type:${this._type})`;
  }
}
