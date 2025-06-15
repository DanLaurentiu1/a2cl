import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import ast

df = pd.read_csv("path")

all_tags = []
for tags_str in df["Topic_tags"]:
    tags_list = ast.literal_eval(tags_str)
    all_tags.extend(tags_list)

tag_counts = Counter(all_tags)
tags = list(tag_counts.keys())
counts = list(tag_counts.values())

sorted_tags = [tag for tag, _ in sorted(zip(tags, counts), key=lambda x: -x[1])]
sorted_counts = sorted(counts, reverse=True)

plt.figure(figsize=(10, 6))
plt.bar(sorted_tags[:15], sorted_counts[:15], color="#76abae")
plt.title("Most Frequent Topic Tags", fontsize=14)
plt.xlabel("Topic Tags", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
