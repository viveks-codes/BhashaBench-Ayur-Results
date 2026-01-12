import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

# Define paths
base_dir = "raw_results"
output_dir = "analysis"
os.makedirs(output_dir, exist_ok=True)

# Define models to compare
vaidh_model_name = "VaidhLLaMA-3.2-3B"
base_model_name = "Llama-3.2-3B"

def load_and_agg(model_name):
    files = glob.glob(os.path.join(base_dir, f"results_{model_name}_run*.csv"))
    if not files:
        print(f"No files found for {model_name}")
        return None
    
    dfs = []
    for f in files:
        dfs.append(pd.read_csv(f))
    
    df = pd.concat(dfs)
    # Convert is_correct to boolean if it's string
    if df['is_correct'].dtype == object:
         df['is_correct'] = df['is_correct'].apply(lambda x: str(x).lower() == 'true')
    
    # Group by topic and calculate mean accuracy
    topic_acc = df.groupby('topic')['is_correct'].mean() * 100
    return topic_acc

# Load data
vaidh_acc = load_and_agg(vaidh_model_name)
base_acc = load_and_agg(base_model_name)

if vaidh_acc is None or base_acc is None:
    print("Error loading data.")
    exit(1)

# specific fix for topic names if they differ slighty or to ensure alignment
# We do an inner join or outer join? Standard topics should be same.
# Let's align them.
topics = vaidh_acc.index.union(base_acc.index)
vaidh_acc = vaidh_acc.reindex(topics)
base_acc = base_acc.reindex(topics)

# Calculate difference
diff = vaidh_acc - base_acc
diff = diff.sort_values(ascending=False)

# Save to CSV
diff.to_csv(os.path.join(output_dir, "vaidhllama_improvement.csv"), header=["accuracy_delta"])

# Plotting
plt.figure(figsize=(12, 10))
# Create colors: Green for positive, Red for negative
colors = ['#2ecc71' if x >= 0 else '#e74c3c' for x in diff.values]

sns.barplot(x=diff.values, y=diff.index, palette=colors)

plt.title(f'Performance Improvement: {vaidh_model_name} vs {base_model_name}', fontsize=16)
plt.xlabel('Accuracy Difference (%)', fontsize=12)
plt.ylabel('Topic', fontsize=12)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add values on bars
for i, v in enumerate(diff.values):
    offset = 0.5 if v >= 0 else -0.5
    ha = 'left' if v >= 0 else 'right'
    plt.text(v + offset, i, f'{v:+.2f}%', va='center', ha=ha, fontsize=10)

plt.tight_layout()
plot_path = os.path.join(output_dir, "vaidhllama_vs_llama_improvement.png")
plt.savefig(plot_path, dpi=300)
print(f"Plot saved to {plot_path}")
