#This grouped bar graph script visualizes the features — Cellular Localization, based on their expression.

from google.colab import files
# Upload the file
uploaded = files.upload()

# Load the Excel file
file_path = "GC(Percentage_Localization).xlsx"  # Update file name if different
df = pd.read_excel(file_path)

# Check the first few rows to confirm the data
df.head()

import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Cytoplasm', 'Extracellular Vesicle']
upregulated = [40.55, 59.45]
downregulated = [26.31, 73.68]

x = np.arange(len(labels))  # Label locations
width = 0.35  # Width of bars

fig, ax = plt.subplots(figsize=(8, 6))

# Create bars
bars1 = ax.bar(x - width/2, upregulated, width, label='Upregulated', color='blue', edgecolor='black')
bars2 = ax.bar(x + width/2, downregulated, width, label='Downregulated', color='red', edgecolor='black')

# Add data labels
for bar in bars1:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height:.2f}%', ha='center', va='bottom', fontsize=9, weight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height:.2f}%', ha='center', va='bottom', fontsize=9, weight='bold')

# Titles and labels
ax.set_ylabel('Percentage', fontsize=12)
ax.set_xlabel('Localization', fontsize=12)
ax.set_title('Localization Distribution in Upregulated and Downregulated circRNAs', fontsize=14, weight='bold')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.tight_layout()
plt.show()
