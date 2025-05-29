import ast
import numpy as np
from pandas import DataFrame

from app.model.utils.conversion import convert_difficulty


def find_topic_difficulty_pairs(questions: DataFrame, topic: str, difficulty: int):
    acceptance_rates = []
    for index, row in questions.iterrows():
        try:
            topics_list = ast.literal_eval(row["Topic_tags"])
        except (ValueError, SyntaxError):
            topics_list = []
        if topic in topics_list and difficulty == convert_difficulty(row["Difficulty"]):
            acceptance_rates.append(row["Acceptance_rate"])
    return np.char.replace(np.array(acceptance_rates), '%', '').astype(float) if acceptance_rates else np.array([])