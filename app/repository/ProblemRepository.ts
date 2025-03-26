import { Problem } from "../domain/Problem";
import { topicRepository, TopicRepository } from "./TopicRepository";

export class ProblemRepository {
  private _topicRepository: TopicRepository;
  private _problems: Map<number, Problem>;

  constructor() {
    this._problems = new Map();
    this._topicRepository = topicRepository;
    this.initialiseProblems();
  }

  public getProblemByNumber(number: number): Problem | undefined {
    return this._problems.get(number);
  }

  public initialiseProblems() {
    this._problems.set(
      1,
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
      2,
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
      3,
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
      4,
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
      5,
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
      6,
      new Problem(
        6,
        "Zigzag Conversion",
        [this._topicRepository.getTopicByName("String")!],
        1,
        50
      )
    );
    this._problems.set(
      7,
      new Problem(
        7,
        "Reverse Integer",
        [this._topicRepository.getTopicByName("Math")!],
        1,
        29
      )
    );
    this._problems.set(
      8,
      new Problem(
        8,
        "String to Integer (atoi)",
        [this._topicRepository.getTopicByName("String")!],
        1,
        18
      )
    );
  }
}
export let problemRepository = new ProblemRepository();
