from collections import defaultdict

import csv
import os
import numpy as np
from stable_baselines3 import A2C
from stable_baselines3.common.callbacks import BaseCallback, CallbackList
from app.model.LeetcodeRecommenderEnv import LeetcodeRecommenderEnv

class TrainingMetricsCallback(BaseCallback):
    def __init__(self, log_dir="logs", verbose=0):
        super().__init__(verbose)
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self.episode_file = self._create_log_file("episode_metrics.csv", ["Episode", "Reward", "MovingAvg", "Entropy"])
        self.update_file = self._create_log_file("update_metrics.csv",["Timestep", "ActorLoss", "CriticLoss", "ActorGradNorm", "CriticGradNorm"])
        self.episode_rewards = []
        self.episode_reward = 0
        self.moving_avg_window = 100
        self.moving_avg_rewards = []
        self.episode_actions = []

    def _create_log_file(self, filename, headers):
        file_path = os.path.join(self.log_dir, filename)
        file = open(file_path, 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(headers)
        return {"file": file, "writer": writer}

    def _on_step(self) -> bool:
        rewards = self.locals.get('rewards', [0])
        dones = self.locals.get('dones', [False])
        actions = self.locals.get('actions', [None])
        self.episode_reward += rewards[0]
        self.episode_actions.append(actions[0])
        if dones[0]:
            self.episode_rewards.append(self.episode_reward)
            start_idx = max(0, len(self.episode_rewards) - self.moving_avg_window)
            moving_avg = np.mean(self.episode_rewards[start_idx:])
            self.moving_avg_rewards.append(moving_avg)
            action_counts = defaultdict(int)
            for a in self.episode_actions:
                action_counts[a] += 1
            entropy = 0.0
            total = len(self.episode_actions)
            for count in action_counts.values():
                p = count / total
                entropy -= p * np.log(p + 1e-8)
            episode_num = len(self.episode_rewards)
            self.episode_file["writer"].writerow([
                episode_num,
                self.episode_reward,
                np.round(moving_avg, 3),
                np.round(entropy, 3)
            ])
            self.episode_file["file"].flush()
            self.episode_reward = 0
            self.episode_actions = []
        if self.model and self.model.num_timesteps % 40 == 0:
            logs = self.model.logger.name_to_value
            actor_loss = logs.get("train/policy_loss", float("nan"))
            critic_loss = logs.get("train/value_loss", float("nan"))
            actor_norm, critic_norm = 0, 0
            for name, param in self.model.policy.named_parameters():
                if param.grad is not None:
                    if "policy" in name:
                        actor_norm += param.grad.data.norm(2).item() ** 2
                    elif "value" in name:
                        critic_norm += param.grad.data.norm(2).item() ** 2
            actor_norm = np.sqrt(actor_norm)
            critic_norm = np.sqrt(critic_norm)
            self.update_file["writer"].writerow([
                self.model.num_timesteps,
                np.round(actor_loss, 3),
                np.round(critic_loss, 3),
                np.round(actor_norm, 3),
                np.round(critic_norm, 3)
            ])
            self.update_file["file"].flush()
        return True

    def _on_training_end(self):
        self.episode_file["file"].close()
        self.update_file["file"].close()


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
            ent_coef=0.01,
            learning_rate=1e-3
        )

    def load_model(self, env_targets: list[str], model_path: str):
        self.env = self.create_testing_env(topics=env_targets)
        self.model = A2C.load(model_path, env=self.env, device="auto", verbose=1)
        return self.model

    def train(self):
        self.env = self.create_training_env()
        self.model = self.create_model(self.env)
        metrics_callback = TrainingMetricsCallback()
        checkpoint_callback = EpisodeCheckpointCallback(save_freq_episodes=self.save_freq_episodes, save_path=self.checkpoint_dir)

        callbacks = CallbackList([metrics_callback, checkpoint_callback])
        print(f"Starting training for {self.total_timesteps} timesteps")
        self.model.learn(
            total_timesteps=self.total_timesteps,
            callback=callbacks
        )
        final_path = os.path.join(
            self.checkpoint_dir,
            f"final_model_{self.total_timesteps}"
        )
        self.model.save(final_path)
        print(f"Training done! Final model saved to {final_path}.zip")

    def evaluate(self, env_targets: list[str], num_episodes: int = 10, load_path: str = None):
        if load_path is not None:
            self.model = self.load_model(env_targets, load_path)
        if self.model is None:
            raise ValueError("No model loaded or trained yet!")

        self.env = self.create_testing_env(topics=env_targets)
        recommended_problems_final: list[int] = []
        reward_final = 0
        print(f"Evaluating {num_episodes} episodes on targets={env_targets}")
        for episode in range(num_episodes):
            obs, _ = self.env.reset()
            done, truncated = False, False
            episode_reward, step_count = 0.0, 0
            recommended_problems: list[int] = []

            while not done and not truncated:
                action, _ = self.model.predict(obs, deterministic=False)
                recommended_problems.append(int(action))
                obs, reward, done, truncated, _ = self.env.step(action)
                episode_reward += reward
                step_count += 1
                
            if episode_reward >= reward_final:
                reward_final = episode_reward
                recommended_problems_final = recommended_problems.copy()
            print(f" Episode {episode + 1}: Steps={step_count}, Reward={episode_reward:.2f}")
        print(f"Chosen reward: {reward_final}")
        return recommended_problems_final