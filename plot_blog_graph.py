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

# Filter for positive improvements only
df_improved = df[df['accuracy_delta'] > 0].sort_values(by='accuracy_delta', ascending=False)

# Take top 15
top_n = 15
df_top = df_improved.head(top_n)

# Plotting
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")

# Create a horizontal bar chart
barplot = sns.barplot(
    data=df_top,
    y='topic',
    x='accuracy_delta',
    palette="viridis",
    hue='topic',
    legend=False
)

plt.title(f'Top {top_n} Areas Where VaidhLLaMA Improves Over Base Model', fontsize=18, pad=20)
plt.xlabel('Accuracy Improvement (%)', fontsize=14)
plt.ylabel('Ayurvedic Topic', fontsize=14)

# Add values to the bars
for i, v in enumerate(df_top['accuracy_delta']):
    plt.text(v + 0.5, i, f'+{v:.1f}%', va='center', fontsize=12, fontweight='bold', color='#2c3e50')

plt.tight_layout()

# Save
plot_path = os.path.join(output_dir, "vaidhllama_blog_improvement.png")
plt.savefig(plot_path, dpi=300, bbox_inches='tight')
print(f"Blog-ready plot saved to {plot_path}")
