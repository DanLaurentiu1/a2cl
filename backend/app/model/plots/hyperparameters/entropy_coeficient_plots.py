from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt

colors = {
    "green": "#76abae",
    "orange": "#ffa116",
}

df = pd.read_csv(Path(__file__).parent.parent / "logs" / "episode_metrics.csv")
plt.figure(figsize=(15, 9))
plt.plot(df["Episode"], df["Entropy"], color=colors["green"], label="Entropy")
plt.plot(
    df["Episode"],
    df["EntropyMovingAvg"],
    color=colors["orange"],
    label="Entropy Moving Avg",
)
plt.xlabel("Episode")
plt.ylabel("Entropy")
plt.title("Entropy and Moving Average")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
