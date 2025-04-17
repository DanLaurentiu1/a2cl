import { Problem } from "../../domain/Problem";
import { getTopicByName } from "./topics";

export const ALL_PROBLEMS: readonly Problem[] = [
  new Problem(
    1,
    "Two Sum",
    [getTopicByName("Array"), getTopicByName("Hash Table")],
    0,
    54.1
  ),
  new Problem(
    2,
    "Add Two Numbers",
    [
      getTopicByName("Linked List"),
      getTopicByName("Math"),
      getTopicByName("Recursion"),
    ],
    1,
    44.5
  ),
  new Problem(
    3,
    "Longest Substring Without Repeating Characters",
    [
      getTopicByName("Hash Table"),
      getTopicByName("String"),
      getTopicByName("Sliding Window"),
    ],
    1,
    35.7
  ),
  new Problem(
    4,
    "Median of Two Sorted Arrays",
    [
      getTopicByName("Array"),
      getTopicByName("Binary Search"),
      getTopicByName("Divide and Conquer"),
    ],
    2,
    41.8
  ),
  new Problem(
    5,
    "Longest Palindromic Substring",
    [
      getTopicByName("Two Pointers"),
      getTopicByName("String"),
      getTopicByName("Dynamic Programming"),
    ],
    1,
    34.7
  ),
  new Problem(6, "Zigzag Conversion", [getTopicByName("String")], 1, 49.7),
  new Problem(7, "Reverse Integer", [getTopicByName("Math")], 1, 29.3),
  new Problem(
    8,
    "String to Integer (atoi)",
    [getTopicByName("String")],
    1,
    18.1
  ),
  new Problem(9, "Palindrome Number", [getTopicByName("Math")], 0, 57.8),
  new Problem(
    10,
    "Regular Expression Matching",
    [
      getTopicByName("String"),
      getTopicByName("Dynamic Programming"),
      getTopicByName("Recursion"),
    ],
    2,
    28.5
  ),
  new Problem(
    11,
    "Container With Most Water",
    [
      getTopicByName("Array"),
      getTopicByName("Two Pointers"),
      getTopicByName("Greedy"),
    ],
    1,
    56.4
  ),
  new Problem(
    12,
    "Integer to Roman",
    [
      getTopicByName("Hash Table"),
      getTopicByName("Math"),
      getTopicByName("String"),
    ],
    1,
    66.7
  ),
  new Problem(
    13,
    "Roman to Integer",
    [
      getTopicByName("Hash Table"),
      getTopicByName("Math"),
      getTopicByName("String"),
    ],
    0,
    63.1
  ),
  new Problem(
    14,
    "Longest Common Prefix",
    [getTopicByName("String"), getTopicByName("Trie")],
    0,
    44.1
  ),
  new Problem(
    15,
    "3Sum",
    [
      getTopicByName("Array"),
      getTopicByName("Two Pointers"),
      getTopicByName("Sorting"),
    ],
    1,
    35.6
  ),
  new Problem(
    16,
    "3Sum Closest",
    [
      getTopicByName("Array"),
      getTopicByName("Two Pointers"),
      getTopicByName("Sorting"),
    ],
    1,
    46.2
  ),
  new Problem(
    17,
    "Letter Combinations of a Phone Number",
    [
      getTopicByName("Hash Table"),
      getTopicByName("String"),
      getTopicByName("Backtracking"),
    ],
    1,
    62.1
  ),
  new Problem(
    18,
    "4Sum",
    [
      getTopicByName("Array"),
      getTopicByName("Two Pointers"),
      getTopicByName("Sorting"),
    ],
    1,
    36.9
  ),
  new Problem(
    19,
    "Remove Nth Node From End of List",
    [getTopicByName("Linked List"), getTopicByName("Two Pointers")],
    1,
    47.1
  ),
  new Problem(
    20,
    "Valid Parentheses",
    [getTopicByName("String"), getTopicByName("Stack")],
    0,
    41.3
  ),
  new Problem(
    21,
    "Merge Two Sorted Lists",
    [getTopicByName("Linked List"), getTopicByName("Recursion")],
    0,
    65.6
  ),
  new Problem(
    22,
    "Generate Parentheses",
    [
      getTopicByName("String"),
      getTopicByName("Dynamic Programming"),
      getTopicByName("Backtracking"),
    ],
    1,
    75.8
  ),
  new Problem(
    23,
    "Merge k Sorted Lists",
    [
      getTopicByName("Linked List"),
      getTopicByName("Divide and Conquer"),
      getTopicByName("Heap (Priority Queue)"),
      getTopicByName("Merge Sort"),
    ],
    2,
    54.6
  ),
  new Problem(
    24,
    "Swap Nodes in Pairs",
    [getTopicByName("Linked List"), getTopicByName("Recursion")],
    1,
    65.6
  ),
  new Problem(
    25,
    "Reverse Nodes in k-Group",
    [getTopicByName("Linked List"), getTopicByName("Recursion")],
    2,
    60.8
  ),
  new Problem(
    26,
    "Remove Duplicates from Sorted Array",
    [getTopicByName("Array"), getTopicByName("Two Pointers")],
    0,
    58.1
  ),
  new Problem(
    27,
    "Remove Element",
    [getTopicByName("Array"), getTopicByName("Two Pointers")],
    0,
    58.6
  ),
  new Problem(
    28,
    "Find the Index of the First Occurrence in a String",
    [
      getTopicByName("Two Pointers"),
      getTopicByName("String"),
      getTopicByName("String Matching"),
    ],
    0,
    43.7
  ),
  new Problem(
    29,
    "Divide Two Integers",
    [getTopicByName("Math"), getTopicByName("Bit Manipulation")],
    1,
    17.8
  ),
  new Problem(
    30,
    "Substring with Concatenation of All Words",
    [
      getTopicByName("Hash Table"),
      getTopicByName("String"),
      getTopicByName("Sliding Window"),
    ],
    2,
    32.5
  ),
] as const;

export function getProblemById(id: number): Problem {
  const result = ALL_PROBLEMS.find((problem) => problem.id === id);
  if (result === undefined) {
    throw new Error();
  }
  return result;
}

export function getProblemByName(name: string): Problem {
  const result = ALL_PROBLEMS.find((problem) => problem.name === name);
  if (result === undefined) {
    throw new Error();
  }
  return result;
}
