from app.core.data.topics import get_topic_by_name
from app.core.domain import Problem


ALL_PROBLEMS = [
    Problem(1, "Two Sum", [get_topic_by_name("Array"), get_topic_by_name("Hash Table")], 0, 54.1),
    Problem(2, "Add Two Numbers", [get_topic_by_name("Linked List"), get_topic_by_name("Math"), get_topic_by_name("Recursion")], 1, 44.5),
    Problem(3, "Longest Substring Without Repeating Characters", [get_topic_by_name("Hash Table"), get_topic_by_name("String"), get_topic_by_name("Sliding Window")], 1, 35.7),
    Problem(4, "Median of Two Sorted Arrays", [get_topic_by_name("Array"), get_topic_by_name("Binary Search"), get_topic_by_name("Divide and Conquer")], 2, 41.8),
    Problem(5, "Longest Palindromic Substring", [get_topic_by_name("Two Pointers"), get_topic_by_name("String"), get_topic_by_name("Dynamic Programming")], 1, 34.7),
    Problem(6, "Zigzag Conversion", [get_topic_by_name("String")], 1, 49.7),
    Problem(7, "Reverse Integer", [get_topic_by_name("Math")], 1, 29.3),
    Problem(8, "String to Integer (atoi)", [get_topic_by_name("String")], 1, 18.1),
    Problem(9, "Palindrome Number", [get_topic_by_name("Math")], 0, 57.8),
    Problem(10, "Regular Expression Matching", [get_topic_by_name("String"), get_topic_by_name("Dynamic Programming"), get_topic_by_name("Recursion")], 2, 28.5),
    Problem(11, "Container With Most Water", [get_topic_by_name("Array"), get_topic_by_name("Two Pointers"), get_topic_by_name("Greedy")], 1, 56.4),
    Problem(12, "Integer to Roman", [get_topic_by_name("Hash Table"), get_topic_by_name("Math"), get_topic_by_name("String")], 1, 66.7),
    Problem(13, "Roman to Integer", [get_topic_by_name("Hash Table"), get_topic_by_name("Math"), get_topic_by_name("String")], 0, 63.1),
    Problem(14, "Longest Common Prefix", [get_topic_by_name("String"), get_topic_by_name("Trie")], 0, 44.1),
    Problem(15, "3Sum", [get_topic_by_name("Array"), get_topic_by_name("Two Pointers"), get_topic_by_name("Sorting")], 1, 35.6),
    Problem(16, "3Sum Closest", [get_topic_by_name("Array"), get_topic_by_name("Two Pointers"), get_topic_by_name("Sorting")], 1, 46.2),
    Problem(17, "Letter Combinations of a Phone Number", [get_topic_by_name("Hash Table"), get_topic_by_name("String"), get_topic_by_name("Backtracking")], 1, 62.1),
    Problem(18, "4Sum", [get_topic_by_name("Array"), get_topic_by_name("Two Pointers"), get_topic_by_name("Sorting")], 1, 36.9),
    Problem(19, "Remove Nth Node From End of List", [get_topic_by_name("Linked List"), get_topic_by_name("Two Pointers")], 1, 47.1),
    Problem(20, "Valid Parentheses", [get_topic_by_name("String"), get_topic_by_name("Stack")], 0, 41.3),
    Problem(21, "Merge Two Sorted Lists", [get_topic_by_name("Linked List"), get_topic_by_name("Recursion")], 0, 65.6),
    Problem(22, "Generate Parentheses", [get_topic_by_name("String"), get_topic_by_name("Dynamic Programming"), get_topic_by_name("Backtracking")], 1, 75.8),
    Problem(23, "Merge k Sorted Lists", [get_topic_by_name("Linked List"), get_topic_by_name("Divide and Conquer"), get_topic_by_name("Heap (Priority Queue)"), get_topic_by_name("Merge Sort")], 2, 54.6),
    Problem(24, "Swap Nodes in Pairs", [get_topic_by_name("Linked List"), get_topic_by_name("Recursion")], 1, 65.6),
    Problem(25, "Reverse Nodes in k-Group", [get_topic_by_name("Linked List"), get_topic_by_name("Recursion")], 2, 60.8),
    Problem(26, "Remove Duplicates from Sorted Array", [get_topic_by_name("Array"), get_topic_by_name("Two Pointers")], 0, 58.1),
    Problem(27, "Remove Element", [get_topic_by_name("Array"), get_topic_by_name("Two Pointers")], 0, 58.6),
    Problem(28, "Find the Index of the First Occurrence in a String", [get_topic_by_name("Two Pointers"), get_topic_by_name("String"), get_topic_by_name("String Matching")], 0, 43.7),
    Problem(29, "Divide Two Integers", [get_topic_by_name("Math"), get_topic_by_name("Bit Manipulation")], 1, 17.8),
    Problem(30, "Substring with Concatenation of All Words", [get_topic_by_name("Hash Table"), get_topic_by_name("String"), get_topic_by_name("Sliding Window")], 2, 32.5),
]


def get_problem_by_id(id: int) -> Problem:
    for problem in ALL_PROBLEMS:
        if problem.id == id:
            return problem
    raise ValueError(f"No problem found with id={id}")


def get_problem_by_name(name: str) -> Problem:
    for problem in ALL_PROBLEMS:
        if problem.name == name:
            return problem
    raise ValueError(f"No problem found with name='{name}'")
