import pandas as pd

from app.model.utils.data_analysis.get_statistics_about_distribution import get_mean, get_median, get_variance


def save_stats_to_file(questions: pd.DataFrame, all_topics, all_difficulties, output_file: str):
    data_rows = []
    for topic in all_topics:
        for difficulty in all_difficulties:
            mean = get_mean(questions=questions, topic=topic, difficulty=difficulty)
            median = get_median(questions=questions, topic=topic, difficulty=difficulty)
            var = get_variance(questions=questions, topic=topic, difficulty=difficulty)

            data_rows.append({
                "Topic": topic,
                "Difficulty": difficulty,
                "Mean": mean,
                "Median": median,
                "Variance": var
            })
    stats_df = pd.DataFrame(data_rows)
    stats_df.to_csv(output_file, index=False)
