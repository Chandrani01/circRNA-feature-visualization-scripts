#This grouped bar graph script visualizes three features — GC Content, Localization, and circRNA Type — for circRNAs that are upregulated.

from google.colab import files
# Upload the file
uploaded = files.upload()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Excel file
file_path = "AD(Percentage).xlsx"  # Update file name if different
df = pd.read_excel(file_path)

# Check the first few rows to confirm the data
df.head()

# Define categories and data
labels = ['GC Content', 'Localization', 'circRNA Type']
subcategories = [['GC>50%', 'GC<50%'], ['Cytoplasm', 'Extracellular Vesicle'], ['ciRNA', 'ecircRNA']]
values = [
    [16.66, 83.33],     # GC content
    [22.22, 72.22],     # Localization
    [11.11, 83.33]      # circRNA type
]

# Bar width and positions
x = np.arange(len(labels))
width = 0.35

# Color palette (distinct for each subcategory)
colors = [['blue', 'red'], ['blue', 'red'], ['blue', 'red']]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars with labels and colors
for i in range(len(subcategories)):
    for j in range(len(subcategories[i])):
        xpos = x[i] + (j - 0.5) * width
        value = values[i][j]
        color = colors[i][j]
        label = subcategories[i][j]

        # Draw bar
        bar = ax.bar(xpos, value, width,
                     label=label if i == 0 else "",
                     edgecolor='black',
                     color=color)

        # Add data value on top of the bar
        ax.text(xpos, value + 1, f'{value:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

        # Add category label inside the bar
        ax.text(xpos, value / 2, label, ha='center', va='center', fontsize=6, color='white', weight='bold')

# Configure axes and labels
ax.set_ylabel('Percentage')
ax.set_title('Bar Graph for Upregulated circRNAs')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(title="Subcategories")

# Neaten layout
plt.tight_layout()
plt.show()
