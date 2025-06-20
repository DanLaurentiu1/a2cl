from collections import defaultdict

import pandas as pd


def load_default_proficiencies(path, default_score: int):
    default_proficiencies = defaultdict(int)
    topics_df = pd.read_csv(path)
    topics = topics_df["Topic"].to_list()
    for topic in topics:
        default_proficiencies[str(topic)] = default_score
    return default_proficiencies
