import numpy as np
from pandas import DataFrame
from app.model.utils.data_analysis.find_topic_difficulty_pairs import find_topic_difficulty_pairs

def get_median(questions: DataFrame, topic: str, difficulty: int):
    acceptance_rates = find_topic_difficulty_pairs(questions=questions, topic=topic, difficulty=difficulty)
    return np.round(np.median(acceptance_rates), 2) if acceptance_rates.size != 0 else -1


def get_mean(questions: DataFrame, topic: str, difficulty: int):
    acceptance_rates = find_topic_difficulty_pairs(questions=questions, topic=topic, difficulty=difficulty)
    return np.round(np.mean(acceptance_rates), 2) if acceptance_rates.size != 0 else -1


def get_variance(questions: DataFrame, topic: str, difficulty: int):
    acceptance_rates = find_topic_difficulty_pairs(questions=questions, topic=topic, difficulty=difficulty)
    return np.round(np.var(acceptance_rates), 2) if acceptance_rates.size != 0 else -1


def get_max_acceptance_rate(questions: DataFrame, topic: str, difficulty: int):
    acceptance_rates = find_topic_difficulty_pairs(questions=questions, topic=topic, difficulty=difficulty)
    return np.max(acceptance_rates) if acceptance_rates.size != 0 else -1


def get_min_acceptance_rate(questions: DataFrame, topic: str, difficulty: int):
    acceptance_rates = find_topic_difficulty_pairs(questions=questions, topic=topic, difficulty=difficulty)
    return np.min(acceptance_rates) if acceptance_rates.size != 0 else -1