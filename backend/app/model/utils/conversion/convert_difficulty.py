def convert_difficulty(difficulty_str: str):
    difficulty_map = {
        'Easy': 0,
        'Medium': 1,
        'Hard': 2
    }
    return difficulty_map.get(difficulty_str, 0)