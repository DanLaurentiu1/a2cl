import numpy as np
from pandas import DataFrame
from app.model.utils.data_analysis.find_topic_difficulty_pairs import find_topic_difficulty_pairs

def get_median(questions: DataFrame, topic: str, difficulty: int):
    acceptance_rates = find_topic_difficulty_pairs(questions=questions, topic=topic, difficulty=difficulty)
    return np.median(acceptance_rates)


def get_mean(questions: DataFrame, topic: str, difficulty: int):
    acceptance_rates = find_topic_difficulty_pairs(questions=questions, topic=topic, difficulty=difficulty)
    return np.mean(acceptance_rates)


def get_variance(questions: DataFrame, topic: str, difficulty: int):
    acceptance_rates = find_topic_difficulty_pairs(questions=questions, topic=topic, difficulty=difficulty)
    return np.var(acceptance_rates)