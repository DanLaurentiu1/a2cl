from sqlalchemy.orm import Session
from app.core.database.models.DB_Topic import DB_Topic
from app.api.schemas.schemas import TopicTypes

class TopicSeeder:
    @staticmethod
    def seed_data() -> list[dict]:
        return [
            # Data Structures
            {"name": "Binary Tree", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Matrix", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Array", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Linked List", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Monotonic Queue", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "String", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Union Find", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Binary Search Tree", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Segment Tree", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Hash Table", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Binary Indexed Tree", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Heap (Priority Queue)", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Monotonic Stack", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Graph", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Tree", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Trie", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Ordered Set", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Doubly-Linked List", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Stack", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Queue", "type": TopicTypes.DATA_STRUCTURES},
            {"name": "Suffix Array", "type": TopicTypes.DATA_STRUCTURES},
            
            # Algorithms
            {"name": "Sliding Window", "type": TopicTypes.ALGORITHMS},
            {"name": "Two Pointers", "type": TopicTypes.ALGORITHMS},
            {"name": "Divide and Conquer", "type": TopicTypes.ALGORITHMS},
            {"name": "Radix Sort", "type": TopicTypes.ALGORITHMS},
            {"name": "Topological Sort", "type": TopicTypes.ALGORITHMS},
            {"name": "Minimum Spanning Tree", "type": TopicTypes.ALGORITHMS},
            {"name": "Bucket Sort", "type": TopicTypes.ALGORITHMS},
            {"name": "Line Sweep", "type": TopicTypes.ALGORITHMS},
            {"name": "Breadth-First Search", "type": TopicTypes.ALGORITHMS},
            {"name": "Counting Sort", "type": TopicTypes.ALGORITHMS},
            {"name": "Quickselect", "type": TopicTypes.ALGORITHMS},
            {"name": "Binary Search", "type": TopicTypes.ALGORITHMS},
            {"name": "Sorting", "type": TopicTypes.ALGORITHMS},
            {"name": "Depth-First Search", "type": TopicTypes.ALGORITHMS},
            {"name": "Merge Sort", "type": TopicTypes.ALGORITHMS},
            
            # Concepts
            {"name": "String Matching", "type": TopicTypes.CONCEPTS},
            {"name": "Reservoir Sampling", "type": TopicTypes.CONCEPTS},
            {"name": "Bit Manipulation", "type": TopicTypes.CONCEPTS},
            {"name": "Data Stream", "type": TopicTypes.CONCEPTS},
            {"name": "Randomized", "type": TopicTypes.CONCEPTS},
            {"name": "Database", "type": TopicTypes.CONCEPTS},
            {"name": "Number Theory", "type": TopicTypes.CONCEPTS},
            {"name": "Bitmask", "type": TopicTypes.CONCEPTS},
            {"name": "Math", "type": TopicTypes.CONCEPTS},
            {"name": "Rejection Sampling", "type": TopicTypes.CONCEPTS},
            {"name": "Iterator", "type": TopicTypes.CONCEPTS},
            {"name": "Eulerian Circuit", "type": TopicTypes.CONCEPTS},
            {"name": "Enumeration", "type": TopicTypes.CONCEPTS},
            {"name": "Biconnected Component", "type": TopicTypes.CONCEPTS},
            {"name": "Greedy", "type": TopicTypes.CONCEPTS},
            {"name": "Combinatorics", "type": TopicTypes.CONCEPTS},
            {"name": "Probability and Statistics", "type": TopicTypes.CONCEPTS},
            {"name": "Shortest Path", "type": TopicTypes.CONCEPTS},
            {"name": "Hash Function", "type": TopicTypes.CONCEPTS},
            {"name": "Geometry", "type": TopicTypes.CONCEPTS},
            {"name": "Dynamic Programming", "type": TopicTypes.CONCEPTS},
            {"name": "Counting", "type": TopicTypes.CONCEPTS},
            {"name": "Prefix Sum", "type": TopicTypes.CONCEPTS},
            {"name": "Strongly Connected Component", "type": TopicTypes.CONCEPTS},
            {"name": "Rolling Hash", "type": TopicTypes.CONCEPTS},
            {"name": "Recursion", "type": TopicTypes.CONCEPTS},
            {"name": "Memoization", "type": TopicTypes.CONCEPTS},
            {"name": "Backtracking", "type": TopicTypes.CONCEPTS},
            
            # Miscellaneous
            {"name": "Design", "type": TopicTypes.MISCELLANEOUS},
            {"name": "Brainteaser", "type": TopicTypes.MISCELLANEOUS},
            {"name": "Simulation", "type": TopicTypes.MISCELLANEOUS},
            {"name": "Concurrency", "type": TopicTypes.MISCELLANEOUS},
            {"name": "Game Theory", "type": TopicTypes.MISCELLANEOUS},
            {"name": "Shell", "type": TopicTypes.MISCELLANEOUS},
            {"name": "Interactive", "type": TopicTypes.MISCELLANEOUS}
        ]

    @staticmethod
    def run(db: Session):
        existing_topics = {t.name for t in db.query(DB_Topic).all()}
        
        for topic_data in TopicSeeder.seed_data():
            if topic_data["name"] not in existing_topics:
                db.add(DB_Topic(
                    name=topic_data["name"],
                    type=topic_data["type"]
                ))
        
        db.commit()