from pandas import DataFrame

from app.model.utils.data_analysis.get_statistics_about_distribution import get_mean, get_median


ALL_TOPICS = [
    "Binary Tree", "Matrix", "Array", "Linked List", "Monotonic Queue", "String", "Union Find",
    "Binary Search Tree", "Segment Tree", "Hash Table", "Binary Indexed Tree", "Heap (Priority Queue)",
    "Monotonic Stack", "Graph", "Tree", "Trie", "Ordered Set", "Doubly-Linked List", "Stack", "Queue",
    "Suffix Array", "Sliding Window", "Two Pointers", "Divide and Conquer", "Radix Sort", "Topological Sort",
    "Minimum Spanning Tree", "Bucket Sort", "Line Sweep", "Breadth-First Search", "Counting Sort", "Quickselect",
    "Binary Search", "Sorting", "Depth-First Search", "Merge Sort", "String Matching", "Reservoir Sampling",
    "Bit Manipulation", "Data Stream", "Randomized", "Database", "Number Theory", "Bitmask", "Math",
    "Rejection Sampling", "Iterator", "Eulerian Circuit", "Enumeration", "Biconnected Component", "Greedy",
    "Combinatorics", "Probability and Statistics", "Shortest Path", "Hash Function", "Geometry",
    "Dynamic Programming", "Counting", "Prefix Sum", "Strongly Connected Component", "Rolling Hash",
    "Recursion", "Memoization", "Backtracking", "Design", "Brainteaser", "Simulation", "Concurrency",
    "Game Theory", "Shell", "Interactive"
]


def get_mean_median_difference(questions: DataFrame, all_topics, all_difficulties):
    for topic in all_topics:
        for difficulty in all_difficulties:
            median = get_median(questions=questions, topic=topic, difficulty=difficulty)
            mean = get_mean(questions=questions, topic=topic, difficulty=difficulty)
            if abs(median - mean) >= 4:
                print(f"Topic: {topic}, Difficulty: {difficulty}")
                print(f"Mean: {mean}, Median: {median}\n\n")