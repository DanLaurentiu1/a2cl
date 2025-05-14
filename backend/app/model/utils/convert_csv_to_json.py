import ast
import pandas as pd

from app.model.utils.convert_difficulty import convert_difficulty
from app.model.utils.topic_name_to_type import topic_type_dict
from app.model.utils.clean_acceptance_rate import clean_acceptance_rate

def convert_csv_to_json(path: str):
    df = pd.read_csv(path)

    output = []

    for index, row in df.iterrows():
        topics = []
        try:
            topics_list = ast.literal_eval(row["Topic_tags"])
        except (ValueError, SyntaxError):
            topics_list = []

        for topic in topics_list:
            topics.append({"name" : str(topic), "type" : topic_type_dict[str(topic)]})
            
        question_obj = {
            "id": row['Question_No'],
            "name": row['Name'],
            "difficulty": convert_difficulty(row['Difficulty']),
            "acceptance_rate": clean_acceptance_rate(row['Acceptance_rate']),
            "topics": topics
        }
        output.append(question_obj)
    return output