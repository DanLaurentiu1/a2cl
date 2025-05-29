from matplotlib import pyplot as plt
from pandas import DataFrame

from backend.app.model.utils.data_analysis.find_topic_difficulty_pairs import find_topic_difficulty_pairs


def plot_problem_distributions(questions: DataFrame, topic: str, difficulty: int):
    acceptance_rates = find_topic_difficulty_pairs(questions=questions, topic=topic, difficulty=difficulty)
    plt.figure(figsize=(10, 6))
    plt.hist(acceptance_rates, bins=25, edgecolor='black', alpha=0.7)
    plt.title(f"Acceptance Rate Distribution\nTopic: {topic} | Difficulty: {difficulty}")
    plt.xlabel("Acceptance Rate (%)")
    plt.ylabel("Number of Questions")
    # plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.show()
