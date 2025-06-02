from collections import defaultdict

import os
from stable_baselines3 import A2C
from stable_baselines3.common.callbacks import BaseCallback

from app.model import LeetcodeRecommenderEnv

def create_inner_dict():
    return defaultdict(int)


class EpisodeCheckpointCallback(BaseCallback):
    def __init__(self, save_freq_episodes: int, save_path: str, verbose=0):
        super().__init__(verbose)
        self.save_freq_episodes = save_freq_episodes
        self.save_path = save_path
        self.episode_count = 0

    def _on_step(self) -> bool:
        dones = self.locals.get("dones")
        if dones is not None:
            for done in dones:
                if done:
                    self.episode_count += 1
                    if self.episode_count % self.save_freq_episodes == 0:
                        path = os.path.join(self.save_path, f"checkpoint_{self.episode_count}")
                        self.model.save(path)
        return True


class LeetcodeTrainer:
    def __init__(self, total_timesteps=200_000, save_freq_episodes=10, checkpoint_dir="./checkpoints"):
        self.total_timesteps = total_timesteps
        self.save_freq_episodes = save_freq_episodes
        self.checkpoint_dir = checkpoint_dir
        os.makedirs(checkpoint_dir, exist_ok=True)
        self.env = None
        self.model = None

    @staticmethod
    def create_training_env():
        return LeetcodeRecommenderEnv()

    @staticmethod
    def create_testing_env(topics: list[str]):
        return LeetcodeRecommenderEnv(target_topics_list=topics)

    @staticmethod
    def create_model(env):
        return A2C(
            "MultiInputPolicy",
            env,
            verbose=1,
            device="auto",
            ent_coef=0.07,
            learning_rate=3e-4
        )

    def load_model(self, env_targets: list[str], model_path: str):
        self.env = self.create_testing_env(topics=env_targets)
        self.model = A2C.load(model_path, env=self.env, device="auto", verbose=1)
        return self.model

    def train(self):
        self.env = self.create_training_env()
        self.model = self.create_model(self.env)
        checkpoint_callback = EpisodeCheckpointCallback(
            save_freq_episodes=self.save_freq_episodes,
            save_path=self.checkpoint_dir
        )

        print(f"Starting training for {self.total_timesteps} timesteps")
        self.model.learn(
            total_timesteps=self.total_timesteps,
            callback=checkpoint_callback
        )
        final_path = os.path.join(
            self.checkpoint_dir,
            f"final_model_{self.total_timesteps}"
        )
        self.model.save(final_path)
        print(f"Training done! Final model saved to {final_path}.zip")

    def evaluate(self, env_targets: list[str], num_episodes: int = 1, load_path: str = None):
        if load_path is not None:
            self.model = self.load_model(env_targets, load_path)
        if self.model is None:
            raise ValueError("No model loaded or trained yet!")

        self.env = self.create_testing_env(topics=env_targets)
        recommended_problems: list[int] = []
        print(f"Evaluating {num_episodes} episodes on targets={env_targets}")
        for episode in range(num_episodes):
            obs, _ = self.env.reset()
            done, truncated = False, False
            episode_reward, step_count = 0.0, 0

            while not done and not truncated:
                action, _ = self.model.predict(obs, deterministic=False)
                recommended_problems.append(int(action))
                obs, reward, done, truncated, info = self.env.step(action)
                episode_reward += reward
                step_count += 1
            print(f" Episode {episode + 1}: Steps={step_count}, Reward={episode_reward:.2f}")
        return recommended_problems