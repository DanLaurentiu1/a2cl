import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("path")
df["Acceptance_rate"] = df["Acceptance_rate"].str.replace("%", "").astype(float)

bin_size = 3
df["Binned_rate"] = (df["Acceptance_rate"] // bin_size) * bin_size
rate_counts = df["Binned_rate"].value_counts().sort_index()
plt.figure(figsize=(12, 6))
bars = plt.bar(
    rate_counts.index, rate_counts.values, width=bin_size * 0.8, color="#76abae"
)

plt.title(f"Acceptance Rate Distribution ({bin_size}% bins)", fontsize=14)
plt.xlabel("Acceptance Rate (%)", fontsize=12)
plt.ylabel("Number of Questions", fontsize=12)
plt.xticks(np.arange(0, 101, 10))
plt.xlim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.legend()
for x, y in zip(rate_counts.index, rate_counts.values):
    plt.text(x, y + 1, f"{int(y)}", ha="center", va="bottom")
plt.tight_layout()
plt.show()
