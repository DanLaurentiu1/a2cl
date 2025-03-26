import { Problem } from "../domain/Problem";
import { topicRepository, TopicRepository } from "./TopicRepository";

export class ProblemRepository {
  private _topicRepository: TopicRepository;
  private _problems: Map<String, Problem>;

  constructor() {
    this._problems = new Map();
    this._topicRepository = topicRepository;
    this.initialiseProblems();
  }

  public getProblemByName(name: String): Problem | undefined {
    return this._problems.get(name);
  }

  public initialiseProblems() {
    this._problems.set(
      "Two Sum",
      new Problem(
        1,
        "Two Sum",
        [
          this._topicRepository.getTopicByName("Array")!,
          this._topicRepository.getTopicByName("Hash Table")!,
        ],
        0,
        55
      )
    );
    this._problems.set(
      "Add Two Numbers",
      new Problem(
        2,
        "Add Two Numbers",
        [
          this._topicRepository.getTopicByName("Linked List")!,
          this._topicRepository.getTopicByName("Math")!,
          this._topicRepository.getTopicByName("Recursion")!,
        ],
        1,
        45
      )
    );
    this._problems.set(
      "Longest Substring Without Repeating Characters",
      new Problem(
        3,
        "Longest Substring Without Repeating Characters",
        [
          this._topicRepository.getTopicByName("Hash Table")!,
          this._topicRepository.getTopicByName("String")!,
          this._topicRepository.getTopicByName("Sliding Window")!,
        ],
        1,
        36
      )
    );
    this._problems.set(
      "Median Of Two Sorted Arrays",
      new Problem(
        4,
        "Median Of Two Sorted Arrays",
        [
          this._topicRepository.getTopicByName("Array")!,
          this._topicRepository.getTopicByName("Divide And Conquer")!,
          this._topicRepository.getTopicByName("Binary Search")!,
        ],
        2,
        43
      )
    );
    this._problems.set(
      "Longest Palindromic Substring",
      new Problem(
        5,
        "Longest Palindromic Substring",
        [
          this._topicRepository.getTopicByName("Dynamic Programming")!,
          this._topicRepository.getTopicByName("Two Pointers")!,
          this._topicRepository.getTopicByName("String")!,
        ],
        1,
        35
      )
    );
    this._problems.set(
      "Zigzag Conversion",
      new Problem(
        6,
        "Zigzag Conversion",
        [this._topicRepository.getTopicByName("String")!],
        1,
        50
      )
    );
  }
}
export let problemRepository = new ProblemRepository();
