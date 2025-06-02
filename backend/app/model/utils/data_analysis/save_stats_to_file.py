import pandas as pd

from app.model.utils.data_analysis.get_statistics_about_distribution import get_max_acceptance_rate, get_mean, get_median, get_min_acceptance_rate, get_variance
from app.model.utils.data_analysis.get_ranges import get_ranges


def save_data_to_file(questions: pd.DataFrame, ranges: pd.DataFrame, all_topics, all_difficulties, output_file: str):
    data_rows = []
    for topic in all_topics:
        for difficulty in all_difficulties:
            mean = get_mean(questions=questions, topic=topic, difficulty=difficulty)
            median = get_median(questions=questions, topic=topic, difficulty=difficulty)
            var = get_variance(questions=questions, topic=topic, difficulty=difficulty)
            mini = get_min_acceptance_rate(questions=questions, topic=topic, difficulty=difficulty)
            maxi = get_max_acceptance_rate(questions=questions, topic=topic, difficulty=difficulty)
            low, typical, high = get_ranges(questions=ranges, topic=topic, difficulty=difficulty)

            if low != -1 and typical != -1 and high != -1:
                left_range_width = round((median - mini) / (high - typical + 10e-3), 4)
                right_range_width = round((maxi - median) / (typical - low + 10e-3), 4)
            else:
                left_range_width = -1
                right_range_width = -1

            data_rows.append({
                "Topic": topic,
                "Difficulty": difficulty,
                "Mean": mean,
                "Median": median,
                "Variance": var,
                "Minimum": mini,
                "Maximum": maxi,
                "Low": low,
                "Typical": typical,
                "High": high,
                "LeftRangeWidth": left_range_width,
                "RightRangeWidth": right_range_width
            })
    stats_df = pd.DataFrame(data_rows)
    stats_df.to_csv(output_file, index=False)