from typing import List

from app.api.schemas.schemas import TopicTypes
from app.core.domain import Topic

ALL_TOPICS: List[Topic] = [
    # Data Structures
    Topic("Binary Tree", TopicTypes.DATA_STRUCTURES),
    Topic("Matrix", TopicTypes.DATA_STRUCTURES),
    Topic("Array", TopicTypes.DATA_STRUCTURES),
    Topic("Linked List", TopicTypes.DATA_STRUCTURES),
    Topic("Monotonic Queue", TopicTypes.DATA_STRUCTURES),
    Topic("String", TopicTypes.DATA_STRUCTURES),
    Topic("Union Find", TopicTypes.DATA_STRUCTURES),
    Topic("Binary Search Tree", TopicTypes.DATA_STRUCTURES),
    Topic("Segment Tree", TopicTypes.DATA_STRUCTURES),
    Topic("Hash Table", TopicTypes.DATA_STRUCTURES),
    Topic("Binary Indexed Tree", TopicTypes.DATA_STRUCTURES),
    Topic("Heap (Priority Queue)", TopicTypes.DATA_STRUCTURES),
    Topic("Monotonic Stack", TopicTypes.DATA_STRUCTURES),
    Topic("Graph", TopicTypes.DATA_STRUCTURES),
    Topic("Tree", TopicTypes.DATA_STRUCTURES),
    Topic("Trie", TopicTypes.DATA_STRUCTURES),
    Topic("Ordered Set", TopicTypes.DATA_STRUCTURES),
    Topic("Doubly-Linked List", TopicTypes.DATA_STRUCTURES),
    Topic("Stack", TopicTypes.DATA_STRUCTURES),
    Topic("Queue", TopicTypes.DATA_STRUCTURES),
    Topic("Suffix Array", TopicTypes.DATA_STRUCTURES),
    
    # Algorithms
    Topic("Sliding Window", TopicTypes.ALGORITHMS),
    Topic("Two Pointers", TopicTypes.ALGORITHMS),
    Topic("Divide and Conquer", TopicTypes.ALGORITHMS),
    Topic("Radix Sort", TopicTypes.ALGORITHMS),
    Topic("Topological Sort", TopicTypes.ALGORITHMS),
    Topic("Minimum Spanning Tree", TopicTypes.ALGORITHMS),
    Topic("Bucket Sort", TopicTypes.ALGORITHMS),
    Topic("Line Sweep", TopicTypes.ALGORITHMS),
    Topic("Breadth-First Search", TopicTypes.ALGORITHMS),
    Topic("Counting Sort", TopicTypes.ALGORITHMS),
    Topic("Quickselect", TopicTypes.ALGORITHMS),
    Topic("Binary Search", TopicTypes.ALGORITHMS),
    Topic("Sorting", TopicTypes.ALGORITHMS),
    Topic("Depth-First Search", TopicTypes.ALGORITHMS),
    Topic("Merge Sort", TopicTypes.ALGORITHMS),
    
    # Concepts
    Topic("String Matching", TopicTypes.CONCEPTS),
    Topic("Reservoir Sampling", TopicTypes.CONCEPTS),
    Topic("Bit Manipulation", TopicTypes.CONCEPTS),
    Topic("Data Stream", TopicTypes.CONCEPTS),
    Topic("Randomized", TopicTypes.CONCEPTS),
    Topic("Database", TopicTypes.CONCEPTS),
    Topic("Number Theory", TopicTypes.CONCEPTS),
    Topic("Bitmask", TopicTypes.CONCEPTS),
    Topic("Math", TopicTypes.CONCEPTS),
    Topic("Rejection Sampling", TopicTypes.CONCEPTS),
    Topic("Iterator", TopicTypes.CONCEPTS),
    Topic("Eulerian Circuit", TopicTypes.CONCEPTS),
    Topic("Enumeration", TopicTypes.CONCEPTS),
    Topic("Biconnected Component", TopicTypes.CONCEPTS),
    Topic("Greedy", TopicTypes.CONCEPTS),
    Topic("Combinatorics", TopicTypes.CONCEPTS),
    Topic("Probability and Statistics", TopicTypes.CONCEPTS),
    Topic("Shortest Path", TopicTypes.CONCEPTS),
    Topic("Hash Function", TopicTypes.CONCEPTS),
    Topic("Geometry", TopicTypes.CONCEPTS),
    Topic("Dynamic Programming", TopicTypes.CONCEPTS),
    Topic("Counting", TopicTypes.CONCEPTS),
    Topic("Prefix Sum", TopicTypes.CONCEPTS),
    Topic("Strongly Connected Component", TopicTypes.CONCEPTS),
    Topic("Rolling Hash", TopicTypes.CONCEPTS),
    Topic("Recursion", TopicTypes.CONCEPTS),
    Topic("Memoization", TopicTypes.CONCEPTS),
    Topic("Backtracking", TopicTypes.CONCEPTS),
    
    # Miscellaneous
    Topic("Design", TopicTypes.MISCELLANEOUS),
    Topic("Brainteaser", TopicTypes.MISCELLANEOUS),
    Topic("Simulation", TopicTypes.MISCELLANEOUS),
    Topic("Concurrency", TopicTypes.MISCELLANEOUS),
    Topic("Game Theory", TopicTypes.MISCELLANEOUS),
    Topic("Shell", TopicTypes.MISCELLANEOUS),
    Topic("Interactive", TopicTypes.MISCELLANEOUS)
]

def get_topic_by_name(name: str) -> Topic:
    topic = next((t for t in ALL_TOPICS if t.name == name), None)
    if topic is None:
        raise ValueError(f"Topic '{name}' not found")
    return topic