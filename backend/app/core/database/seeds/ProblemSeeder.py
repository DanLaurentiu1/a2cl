from sqlalchemy.orm import Session
from app.core.database.models.DB_Problem import DB_Problem
from app.core.database.models.DB_Topic import DB_Topic
from typing import List, Dict

from app.api.schemas.schemas import TopicTypes

class ProblemSeeder:
    @staticmethod
    def seed_data() -> List[Dict]:
        return [
            {
                "id": 1,
                "name": "Two Sum",
                "difficulty": 0,
                "acceptance_rate": 54.1,
                "topics": [
                    {"name": "Array", "type": TopicTypes.DATA_STRUCTURES},
                    {"name": "Hash Table", "type": TopicTypes.DATA_STRUCTURES}
                ]
            },
    {
        "id": 2,
        "name": "Add Two Numbers",
        "difficulty": 1,
        "acceptance_rate": 44.5,
        "topics": [
            {"name": "Linked List", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Math", "type": TopicTypes.CONCEPTS},
            {"name": "Recursion", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 3,
        "name": "Longest Substring Without Repeating Characters",
        "difficulty": 1,
        "acceptance_rate": 35.7,
        "topics": [
            {"name": "Hash Table", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Sliding Window", "type": TopicTypes.ALGORITHMS}
        ]
    },
    {
        "id": 4,
        "name": "Median of Two Sorted Arrays",
        "difficulty": 2,
        "acceptance_rate": 41.8,
        "topics": [
            {"name": "Array", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Binary Search", "type": TopicTypes.ALGORITHMS},
            {"name": "Divide and Conquer", "type": TopicTypes.ALGORITHMS}
        ]
    },
    {
        "id": 5,
        "name": "Longest Palindromic Substring",
        "difficulty": 1,
        "acceptance_rate": 34.7,
        "topics": [
            {"name": "Two Pointers", "type": TopicTypes.ALGORITHMS},
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Dynamic Programming", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 6,
        "name": "Zigzag Conversion",
        "difficulty": 1,
        "acceptance_rate": 49.7,
        "topics": [
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES}
        ]
    },
    {
        "id": 7,
        "name": "Reverse Integer",
        "difficulty": 1,
        "acceptance_rate": 29.3,
        "topics": [
            {"name": "Math", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 8,
        "name": "String to Integer (atoi)",
        "difficulty": 1,
        "acceptance_rate": 18.1,
        "topics": [
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES}
        ]
    },
    {
        "id": 9,
        "name": "Palindrome Number",
        "difficulty": 0,
        "acceptance_rate": 57.8,
        "topics": [
            {"name": "Math", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 10,
        "name": "Regular Expression Matching",
        "difficulty": 2,
        "acceptance_rate": 28.5,
        "topics": [
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Dynamic Programming", "type": TopicTypes.ALGORITHMS},
            {"name": "Recursion", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 11,
        "name": "Container With Most Water",
        "difficulty": 1,
        "acceptance_rate": 56.4,
        "topics": [
            {"name": "Array", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Two Pointers", "type": TopicTypes.ALGORITHMS},
            {"name": "Greedy", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 12,
        "name": "Integer to Roman",
        "difficulty": 1,
        "acceptance_rate": 66.7,
        "topics": [
            {"name": "Hash Table", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Math", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES}
        ]
    },
    {
        "id": 13,
        "name": "Roman to Integer",
        "difficulty": 0,
        "acceptance_rate": 63.1,
        "topics": [
            {"name": "Hash Table", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Math", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES}
        ]
    },
    {
        "id": 14,
        "name": "Longest Common Prefix",
        "difficulty": 0,
        "acceptance_rate": 44.1,
        "topics": [
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Trie", "type": TopicTypes.DATA_STRUCTURES}
        ]
    },
    {
        "id": 15,
        "name": "3Sum",
        "difficulty": 1,
        "acceptance_rate": 35.6,
        "topics": [
            {"name": "Array", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Two Pointers", "type": TopicTypes.ALGORITHMS},
            {"name": "Sorting", "type": TopicTypes.ALGORITHMS}
        ]
    },
    {
        "id": 16,
        "name": "3Sum Closest",
        "difficulty": 1,
        "acceptance_rate": 46.2,
        "topics": [
            {"name": "Array", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Two Pointers", "type": TopicTypes.ALGORITHMS},
            {"name": "Sorting", "type": TopicTypes.ALGORITHMS}
        ]
    },
    {
        "id": 17,
        "name": "Letter Combinations of a Phone Number",
        "difficulty": 1,
        "acceptance_rate": 62.1,
        "topics": [
            {"name": "Hash Table", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Backtracking", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 18,
        "name": "4Sum",
        "difficulty": 1,
        "acceptance_rate": 36.9,
        "topics": [
            {"name": "Array", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Two Pointers", "type": TopicTypes.ALGORITHMS},
            {"name": "Sorting", "type": TopicTypes.ALGORITHMS}
        ]
    },
    {
        "id": 19,
        "name": "Remove Nth Node From End of List",
        "difficulty": 1,
        "acceptance_rate": 47.1,
        "topics": [
            {"name": "Linked List", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Two Pointers", "type": TopicTypes.ALGORITHMS}
        ]
    },
    {
        "id": 20,
        "name": "Valid Parentheses",
        "difficulty": 0,
        "acceptance_rate": 41.3,
        "topics": [
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Stack", "type": TopicTypes.DATA_STRUCTURES}
        ]
    },
    {
        "id": 21,
        "name": "Merge Two Sorted Lists",
        "difficulty": 0,
        "acceptance_rate": 65.6,
        "topics": [
            {"name": "Linked List", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Recursion", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 22,
        "name": "Generate Parentheses",
        "difficulty": 1,
        "acceptance_rate": 75.8,
        "topics": [
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Dynamic Programming", "type": TopicTypes.CONCEPTS},
            {"name": "Backtracking", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 23,
        "name": "Merge k Sorted Lists",
        "difficulty": 2,
        "acceptance_rate": 54.6,
        "topics": [
            {"name": "Linked List", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Divide and Conquer", "type": TopicTypes.CONCEPTS},
            {"name": "Heap (Priority Queue)", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Merge Sort", "type": TopicTypes.ALGORITHMS}
        ]
    },
    {
        "id": 24,
        "name": "Swap Nodes in Pairs",
        "difficulty": 1,
        "acceptance_rate": 65.6,
        "topics": [
            {"name": "Linked List", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Recursion", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 25,
        "name": "Reverse Nodes in k-Group",
        "difficulty": 2,
        "acceptance_rate": 60.8,
        "topics": [
            {"name": "Linked List", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Recursion", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 26,
        "name": "Remove Duplicates from Sorted Array",
        "difficulty": 0,
        "acceptance_rate": 58.1,
        "topics": [
            {"name": "Array", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Two Pointers", "type": TopicTypes.ALGORITHMS}
        ]
    },
    {
        "id": 27,
        "name": "Remove Element",
        "difficulty": 0,
        "acceptance_rate": 58.6,
        "topics": [
            {"name": "Array", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Two Pointers", "type": TopicTypes.ALGORITHMS}
        ]
    },
    {
        "id": 28,
        "name": "Find the Index of the First Occurrence in a String",
        "difficulty": 0,
        "acceptance_rate": 43.7,
        "topics": [
            {"name": "Two Pointers", "type": TopicTypes.ALGORITHMS},
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "String Matching", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 29,
        "name": "Divide Two Integers",
        "difficulty": 1,
        "acceptance_rate": 17.8,
        "topics": [
            {"name": "Math", "type": TopicTypes.CONCEPTS},
            {"name": "Bit Manipulation", "type": TopicTypes.CONCEPTS}
        ]
    },
    {
        "id": 30,
        "name": "Substring with Concatenation of All Words",
        "difficulty": 2,
        "acceptance_rate": 32.5,
        "topics": [
            {"name": "Hash Table", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Sliding Window", "type": TopicTypes.ALGORITHMS}
        ]
    }        
    ]

    @staticmethod
    def run(db: Session):
        existing_ids = {p.id for p in db.query(DB_Problem).all()}
        for problem_data in ProblemSeeder.seed_data():
            if problem_data["id"] not in existing_ids:
                db_problem = DB_Problem(
                    id=problem_data["id"],
                    name=problem_data["name"],
                    difficulty=problem_data["difficulty"],
                    acceptance_rate=problem_data["acceptance_rate"],
                    topics=problem_data["topics"]
                )
                db.add(db_problem)
        
        db.commit()