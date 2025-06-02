import pandas as pd

def get_all_topics(path):
    topics_df = pd.read_csv(path)
    return topics_df["Topic"].to_list()