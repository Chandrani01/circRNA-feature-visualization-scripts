from google.colab import files
# Upload the file
uploaded = files.upload()

import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "testfile(GC) (3).xlsx"  # Update file name if different
df = pd.read_excel(file_path)

# Check the first few rows to confirm the data
df.head()

#  Create GC content categories based on a threshold (use this line only if you're applying a cutoff, e.g., 50%)
df['GC_Category'] = df['GC Content'].apply(lambda x: 'High GC' if x >= 50 else 'Low GC')

# Group and count circRNAs by Cellular Localization and Expression
grouped_data = df.groupby(['GC_Category', 'expression']).size().unstack(fill_value=0)

# Define bar width and positions for grouped bar chart
bar_width = 0.35
index = range(len(grouped_data))

# Plot the bars for Upregulated and Downregulated circRNAs
fig, ax = plt.subplots(figsize=(8, 6))

# Plot Upregulated
upregulated_bars = ax.bar(
    [i - bar_width / 2 for i in index],
    grouped_data['Up'],
    bar_width,
    label='Up',
    color='blue'
)

# Plot Downregulated
downregulated_bars = ax.bar(
    [i + bar_width / 2 for i in index],
    grouped_data['Down'],
    bar_width,
    label='Down',
    color='red'
)

# Add data labels
for container in [upregulated_bars, downregulated_bars]:
    ax.bar_label(container, fmt='%d', label_type='center', fontsize=10, color='white', weight='bold')

# Add plot details
ax.set_title('Bar Graph of Up and Down-Regulated circRNAs by GC Content', fontsize=14)
ax.set_xlabel('GC Content', fontsize=12)
ax.set_ylabel('Gene Count', fontsize=12)
ax.set_xticks(index)
ax.set_xticklabels(grouped_data.index, rotation=45, ha='right', fontsize=10)

# Add a legend
ax.legend(title='expression')

# Adjust layout and save the plot
plt.tight_layout()
plt.show()
