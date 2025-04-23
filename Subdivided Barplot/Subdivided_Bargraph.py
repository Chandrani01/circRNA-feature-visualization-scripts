#This subdivided bar graph script visualizes circRNA expression patterns (upregulated and downregulated) based on their chromosomal locations.

from google.colab import files
# Upload the file
uploaded = files.upload()

import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "circRNA(Chromosomal_Loc).xlsx"  # Update file name if different
df = pd.read_excel(file_path)

# Check the first few rows to confirm the data
df.head()

# Count occurrences of Up and Down regulation per chromosome
chromosome_counts = df.groupby(["Chromosomal Location", "Expression"]).size().unstack(fill_value=0)

# Plot the subdivided bar graph
fig, ax = plt.subplots(figsize=(12, 6))
bars = chromosome_counts.plot(kind="bar", stacked=True, colormap="coolwarm", edgecolor="black", width=0.8, ax=ax)

# Add data labels
for container in bars.containers:
    ax.bar_label(container, fmt='%d', label_type='center', fontsize=10, color='white', weight='bold')

# Graph aesthetics
plt.xlabel("Chromosomal Location")
plt.ylabel("Count of circRNAs")
plt.title("Subdivided Bar Graph of Up and Down-Regulated circRNAs by Chromosomal Location")
plt.xticks(rotation=45)
plt.legend(title="Expression")

# Show plot
plt.show()
