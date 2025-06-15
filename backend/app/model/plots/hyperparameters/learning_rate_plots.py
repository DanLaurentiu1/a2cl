from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt

colors = {
    "green": "#76abae",
    "orange": "#ffa116",
}
df = pd.read_csv(Path(__file__).parent.parent / "logs" / "update_metrics.csv")
fig, axs = plt.subplots(2, 2, figsize=(15, 9))
fig.suptitle("Learning Rate = 1e-3", fontsize=16)

axs[0, 0].plot(df["Timestep"], df["ActorLoss"], color=colors["green"], linewidth=2)
axs[0, 0].set_title("Actor Loss over Time")
axs[0, 0].set_xlabel("Timesteps")
axs[0, 0].set_ylabel("Loss")
axs[0, 0].grid(alpha=0.3)

axs[0, 1].plot(df["Timestep"], df["CriticLoss"], color=colors["green"], linewidth=2)
axs[0, 1].set_title("Critic Loss over Time")
axs[0, 1].set_xlabel("Timesteps")
axs[0, 1].set_ylabel("Loss")
axs[0, 1].grid(alpha=0.3)

axs[1, 0].plot(df["Timestep"], df["ActorGradNorm"], color=colors["green"], linewidth=2)
axs[1, 0].set_title("Actor Gradient Norm over Time")
axs[1, 0].set_xlabel("Timesteps")
axs[1, 0].set_ylabel("Gradient Norm")
axs[1, 0].grid(alpha=0.3)

axs[1, 1].plot(df["Timestep"], df["CriticGradNorm"], color=colors["green"], linewidth=2)
axs[1, 1].set_title("Critic Gradient Norm over Time")
axs[1, 1].set_xlabel("Timesteps")
axs[1, 1].set_ylabel("Gradient Norm")
axs[1, 1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
