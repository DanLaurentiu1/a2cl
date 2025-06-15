import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("path")

difficulty_counts = df["Difficulty"].value_counts()

difficulty_order = ["Easy", "Medium", "Hard"]
difficulty_counts = difficulty_counts.reindex(difficulty_order)

plt.figure(figsize=(8, 6))
plt.pie(
    difficulty_counts,
    labels=difficulty_counts.index,
    autopct="%1.1f%%",
    colors=["#4CAF50", "#FFC107", "#F44336"],
    startangle=90,
)

plt.title("Difficulty Level Distribution", fontsize=14)
plt.tight_layout()
plt.show()
