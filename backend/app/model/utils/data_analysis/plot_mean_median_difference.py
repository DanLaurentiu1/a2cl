import matplotlib.pyplot as plt
from pandas import DataFrame

from app.model.utils.data_analysis.get_statistics_about_distribution import (
    get_mean,
    get_median,
)


def plot_mean_vs_median(questions: DataFrame, all_topics, all_difficulties):
    means, medians = [], []
    labels = []
    colors = []

    for topic in all_topics:
        for difficulty in all_difficulties:
            median = get_median(questions=questions, topic=topic, difficulty=difficulty)
            mean = get_mean(questions=questions, topic=topic, difficulty=difficulty)

            if median != -1 and mean != -1:
                means.append(mean)
                medians.append(median)
                labels.append(f"{topic} ({difficulty})")

                if abs(mean - median) < 5:
                    colors.append("#76abae")
                else:
                    colors.append("#ffa116")

    plt.figure(figsize=(10, 8))
    max_val = max(max(means), max(medians)) * 1.1
    plt.plot(
        [0, max_val], [0, max_val], "--", color="gray", alpha=0.5, label="Median = Mean"
    )
    plt.scatter(means, medians, c=colors, alpha=0.7, s=50)
    plt.title("Mean vs. Median Acceptance Rate", fontsize=14)
    plt.xlabel("Mean Acceptance Rate (%)", fontsize=12)
    plt.ylabel("Median Acceptance Rate (%)", fontsize=12)
    plt.grid(alpha=0.2)
    from matplotlib.lines import Line2D

    legend_elements = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            label="Mean - Median < 5%",
            markerfacecolor="#76abae",
            markersize=8,
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            label="Mean - Median ≥ 5%",
            markerfacecolor="#ffa116",
            markersize=8,
        ),
    ]
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.show()
