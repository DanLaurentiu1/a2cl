from pandas import DataFrame


def get_ranges(questions: DataFrame, topic: str, difficulty: int):
    for index, row in questions.iterrows():
        if topic == row["Topic"] and difficulty == row["Difficulty"]:
            return [row["Low"], row["Typical"], row["High"]]