from pathlib import Path
import gymnasium as gym
import numpy as np
from gymnasium import spaces
from collections import defaultdict
from gymnasium.utils import seeding
from app.model.utils.model.get_all_topics import get_all_topics
from app.model.utils.model.load_default_proficiencies import load_default_proficiencies
from app.model.utils.model.load_problems_from_json import load_problems_from_json

NUMBER_OF_LEETCODE_PROBLEMS = 3465
MAXIMUM_PROFICIENCY_SCORE = 100
LEETCODE_QUESTIONS_PATH = Path(__file__).parent / 'data' / 'leetcode_problems_grading.json'
LEETCODE_TOPICS_PATH = Path(__file__).parent / 'data' / 'leetcode_topics.csv'
NUMBER_OF_RANDOM_SAMPLED_TOPICS = 1
DEFAULT_SCORE = 15
THRESHOLD_FOR_PROFICIENCIES = 85
THRESHOLD_FOR_PROBLEMS_DONE = 30


class LeetcodeRecommenderEnv(gym.Env):
    def __init__(self, target_topics_list: list[str] = None):
        self.problems = load_problems_from_json(LEETCODE_QUESTIONS_PATH)
        self.current_proficiencies = load_default_proficiencies(LEETCODE_TOPICS_PATH, default_score=DEFAULT_SCORE)
        self.all_topics = get_all_topics(LEETCODE_TOPICS_PATH)
        self.done_problems: list[int] = []
        self.target_vector = np.zeros(len(self.all_topics), dtype=np.int8)
        self.given_targets = target_topics_list is not None
        self.targets = target_topics_list if self.given_targets else []
        self.np_random, _ = seeding.np_random()
        self.observation_space = spaces.Dict({
            "proficiencies": spaces.MultiDiscrete(
                [MAXIMUM_PROFICIENCY_SCORE] * len(self.all_topics)
            ),
            "targets": spaces.MultiBinary(len(self.all_topics))
        })
        self.action_space = spaces.Discrete(NUMBER_OF_LEETCODE_PROBLEMS)
        self.init_targets()

    def transition_proficiencies(self, action):
        if int(action) in self.done_problems:
            return -10

        reward = 0
        to_be_solved_problem: defaultdict[int] = self.problems[str(action)]
        for topic, score in to_be_solved_problem.items():
            if topic in self.targets: reward += 9
            current_score = self.current_proficiencies[topic]
            abs_difference = abs(current_score - score)

            if abs_difference <= 2:
                self.current_proficiencies[topic] = max(current_score, score) + 1
                reward += 3
            elif abs_difference <= 5:
                self.current_proficiencies[topic] = max(current_score, score) + 1
                if current_score < score:
                    reward += 5
                else:
                    reward += 2
            elif abs_difference <= 9:
                if current_score < score:
                    self.current_proficiencies[topic] += 5
                    reward += 1
                else:
                    reward += 0
            else:
                reward += 0
        return reward

    def get_done(self):
        if len(self.done_problems) >= THRESHOLD_FOR_PROBLEMS_DONE: return False, True
        counter = 0
        for topic in self.targets:
            if self.current_proficiencies[topic] >= THRESHOLD_FOR_PROFICIENCIES: counter += 1
        if counter == len(self.targets): return True, False
        return False, False

    def get_observation(self):
        proficiency_vector = np.array([
            self.current_proficiencies[topic] for topic in self.all_topics
        ], dtype=np.int32)

        return {
            "proficiencies": proficiency_vector,
            "targets": self.target_vector
        }

    def init_targets(self):
        if not self.given_targets:
            target_indices = self.np_random.choice(
                len(self.all_topics),
                size=NUMBER_OF_RANDOM_SAMPLED_TOPICS,
                replace=False
            )
            self.targets = [self.all_topics[i] for i in target_indices]
        self.target_vector = np.zeros(len(self.all_topics), dtype=np.int8)
        for topic in self.targets:
            idx = self.all_topics.index(topic)
            self.target_vector[idx] = 1

    def step(self, action):
        action += 1
        reward = self.transition_proficiencies(action)
        self.done_problems.append(int(action))
        terminated, truncated = self.get_done()

        if terminated: reward += 100
        observation = self.get_observation()
        return observation, reward, terminated, truncated, {}

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_proficiencies = load_default_proficiencies(LEETCODE_TOPICS_PATH, default_score=DEFAULT_SCORE)
        self.done_problems = []
        self.init_targets()
        return self.get_observation(), {}

    def close(self):
        pass