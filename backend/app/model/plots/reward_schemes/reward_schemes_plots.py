from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

colors = {
    'green': '#76abae',
    'orange': '#ffa116',
}

episode_df = pd.read_csv(Path(__file__).parent.parent / 'logs' / 'episode_metrics.csv')
update_df = pd.read_csv(Path(__file__).parent.parent / 'logs' / 'update_metrics.csv')
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(18, 15))

ax = axes[0, 0]
ax.plot(
    episode_df["Episode"],
    episode_df["Reward"],
    linewidth=1,
    label="Reward",
    color=colors["green"]
)
ax.plot(
    episode_df["Episode"],
    episode_df["RewardMovingAvg"],
    linewidth=2,
    label="Reward Moving Avg",
    color=colors["orange"]
)
ax.set_xlabel("Episode")
ax.set_ylabel("Reward")
ax.set_title("Reward vs Episode")
ax.grid(True)
ax.legend()

ax = axes[0, 1]
ax.plot(
    episode_df["Episode"],
    episode_df["Entropy"],
    linewidth=1,
    label="Entropy",
    color=colors["green"]
)
ax.plot(
    episode_df["Episode"],
    episode_df["EntropyMovingAvg"],
    linewidth=2,
    label="Entropy Moving Avg",
    color=colors["orange"]
)
ax.set_xlabel("Episode")
ax.set_ylabel("Entropy")
ax.set_title("Entropy vs Episode")
ax.grid(True)
ax.legend()

ax = axes[1, 0]
ax.plot(
    update_df["Timestep"],
    update_df["ActorLoss"],
    linewidth=1,
    label="Actor Loss",
    color=colors["green"]
)
ax.plot(
    update_df["Timestep"],
    update_df["ActorLossMovingAvg"],
    linewidth=2,
    label="Actor Loss Moving Avg",
    color=colors["orange"]
)
ax.set_xlabel("Timestep")
ax.set_ylabel("Actor Loss")
ax.set_title("Actor Loss vs Timestep")
ax.grid(True)
ax.legend()

ax = axes[1, 1]
ax.plot(
    update_df["Timestep"],
    update_df["CriticLoss"],
    linewidth=1,
    label="Critic Loss",
    color=colors["green"]
)
ax.plot(
    update_df["Timestep"],
    update_df["CriticLossMovingAvg"],
    linewidth=2,
    label="Critic Loss Moving Avg",
    color=colors["orange"]
)
ax.set_xlabel("Timestep")
ax.set_ylabel("Critic Loss")
ax.set_title("Critic Loss vs Timestep")
ax.grid(True)
ax.legend()

ax = axes[2, 0]
ax.plot(
    update_df["Timestep"],
    update_df["ActorGradNorm"],
    linewidth=1,
    label="Actor Grad Norm",
    color=colors["green"]
)
ax.plot(
    update_df["Timestep"],
    update_df["ActorGradNormMovingAvg"],
    linewidth=2,
    label="Actor Grad Norm Moving Avg",
    color=colors["orange"]
)
ax.set_xlabel("Timestep")
ax.set_ylabel("Actor Grad Norm")
ax.set_title("Actor Grad Norm vs Timestep")
ax.grid(True)
ax.legend()

ax = axes[2, 1]
ax.plot(
    update_df["Timestep"],
    update_df["CriticGradNorm"],
    linewidth=1,
    label="Critic Grad Norm",
    color=colors["green"]
)
ax.plot(
    update_df["Timestep"],
    update_df["CriticGradNormMovingAvg"],
    linewidth=2,
    label="Critic Grad Norm Moving Avg",
    color=colors["orange"]
)
ax.set_xlabel("Timestep")
ax.set_ylabel("Critic Grad Norm")
ax.set_title("Critic Grad Norm vs Timestep")
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()