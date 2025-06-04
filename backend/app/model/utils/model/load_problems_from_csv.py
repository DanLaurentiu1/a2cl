import pandas as pd
from collections import defaultdict


def load_problems_from_csv(path):
    problems = defaultdict(list)
    questions_df = pd.read_csv(path)
    for problem in questions_df.values:
        problem_number, problem_name, topics, acceptance_rate, difficulty = problem
        problems[problem_number] = [problem_name, parse_topics(topics), parse_acceptance_rate(acceptance_rate), transform_difficulty(difficulty)]
    return problems


def parse_topics(topics):
    topics_set = set()
    temp_topic = ""
    for character in topics.replace("'", "").replace("[", "").replace("]", ""):
        if character != ",":
            temp_topic += character
        else:
            if "+" not in temp_topic:
                topics_set.add(temp_topic.strip())
            temp_topic = ""
    if "+" not in temp_topic:
        topics_set.add(temp_topic.strip())
    return topics_set


def parse_acceptance_rate(acceptance_rate):
    return float(acceptance_rate[0:len(acceptance_rate) - 1])


def transform_difficulty(difficulty):
    difficulty_map = {"Easy": 0, "Medium": 1, "Hard": 2}
    return difficulty_map[difficulty]
