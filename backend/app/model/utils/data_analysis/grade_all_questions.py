import pickle
from collections import defaultdict
import io
import pandas as pd

from backend.app.model.utils.model.load_problems_from_csv import load_problems_from_csv


def create_inner_dict():
    return defaultdict(int)


def grade_all_questions(questions_file, questions_distributions_file, output_file):
    graded_questions = defaultdict(create_inner_dict)
    questions = load_problems_from_csv(questions_file)
    questions_distributions = pd.read_csv(questions_distributions_file)
    for question in questions.items():
        question_id = question[0]
        question_name, question_topics, question_acceptance_rate, question_difficulty = question[1]
        for topic in question_topics:
            for index, row in questions_distributions.iterrows():
                if row["Topic"] == topic and row["Difficulty"] == question_difficulty:
                    median = row["Median"]
                    if question_acceptance_rate > median:
                        maximum = row["Maximum"]
                        grade = row["Low"]
                        right_width = row["RightRangeWidth"]
                        while maximum > question_acceptance_rate:
                            maximum -= right_width
                            grade += 1
                        graded_questions[question_id][topic] = grade
                    else:
                        minimum = row["Minimum"]
                        grade = row["High"]
                        left_width = row["LeftRangeWidth"]
                        while minimum < question_acceptance_rate:
                            minimum += left_width
                            grade -= 1
                        graded_questions[question_id][topic] = grade
                    break
    with io.open(output_file, 'wb') as f:
        pickle.dump(graded_questions, f)