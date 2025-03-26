import { Topic, TopicTypes } from "../domain/Topic";

export class TopicRepository {
  private _topics: Map<String, Topic>;

  constructor() {
    this._topics = new Map();
    this.initialiseTopics();
  }

  public getTopicByName(name: String): Topic | undefined {
    return this._topics.get(name);
  }

  public getAllTopics(): Array<Topic> {
    return Array.from(this._topics.values());
  }

  public initialiseTopics() {
    this._topics.set("Array", new Topic("Array", TopicTypes.DataStructures));
    this._topics.set(
      "Hash Table",
      new Topic("Hash Table", TopicTypes.DataStructures)
    );
    this._topics.set(
      "Linked List",
      new Topic("Linked List", TopicTypes.DataStructures)
    );
    this._topics.set("Math", new Topic("Math", TopicTypes.Concepts));
    this._topics.set(
      "Recursion",
      new Topic("Recursion", TopicTypes.Algorithms)
    );
    this._topics.set("String", new Topic("String", TopicTypes.DataStructures));
    this._topics.set(
      "Sliding Window",
      new Topic("Sliding Window", TopicTypes.Algorithms)
    );
    this._topics.set(
      "Divide And Conquer",
      new Topic("Divide And Conquer", TopicTypes.Algorithms)
    );
    this._topics.set(
      "Binary Search",
      new Topic("Binary Search", TopicTypes.Algorithms)
    );
    this._topics.set(
      "Two Pointers",
      new Topic("Two Pointers", TopicTypes.Algorithms)
    );
    this._topics.set(
      "Dynamic Programming",
      new Topic("Dynamic Programming", TopicTypes.Concepts)
    );
  }
}
export let topicRepository = new TopicRepository();
