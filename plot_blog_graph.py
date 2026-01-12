import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define paths
output_dir = "analysis"
csv_path = os.path.join(output_dir, "vaidhllama_improvement.csv")

if not os.path.exists(csv_path):
    print(f"Error: {csv_path} not found. Run analyze_improvement.py first.")
    exit(1)

# Load data
df = pd.read_csv(csv_path)

# Filter for top 10 improvements and top 10 regressions
df_improved = df.sort_values(by='accuracy_delta', ascending=False).head(10)
df_regressed = df.sort_values(by='accuracy_delta', ascending=True).head(10)

# Combine them
df_plot = pd.concat([df_improved, df_regressed]).sort_values(by='accuracy_delta', ascending=False)

# Plotting
plt.figure(figsize=(14, 10))
sns.set_theme(style="whitegrid")

# Create colors based on value
colors = ['#2ecc71' if x >= 0 else '#e74c3c' for x in df_plot['accuracy_delta']]

# Create a horizontal bar chart
barplot = sns.barplot(
    data=df_plot,
    y='topic',
    x='accuracy_delta',
    palette=colors,
    hue='topic',
    legend=False
)

plt.title('VaidhLLaMA Impact Analysis: Where it Wins & Loses', fontsize=18, pad=20)
plt.xlabel('Accuracy Difference (%)', fontsize=14)
plt.ylabel('Ayurvedic Topic', fontsize=14)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)

# Add values to the bars
for i, v in enumerate(df_plot['accuracy_delta']):
    offset = 1 if v >= 0 else -1
    ha = 'left' if v >= 0 else 'right'
    color = '#27ae60' if v >= 0 else '#c0392b'
    plt.text(v + offset, i, f'{v:+.1f}%', va='center', ha=ha, fontsize=11, fontweight='bold', color=color)

plt.tight_layout()

# Save
plot_path = os.path.join(output_dir, "vaidhllama_blog_improvement.png")
plt.savefig(plot_path, dpi=300, bbox_inches='tight')
print(f"Blog-ready plot with Wins/Losses saved to {plot_path}")
