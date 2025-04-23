{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "x5AkzRf775Nc"
      },
      "outputs": [],
      "source": [
        "#This subdivided bar graph script visualizes circRNA expression patterns (upregulated and downregulated) based on their chromosomal locations.\n",
        "\n",
        "from google.colab import files\n",
        "# Upload the file\n",
        "uploaded = files.upload()\n",
        "\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Load the Excel file\n",
        "file_path = \"circRNA(Chromosomal_Loc).xlsx\"  # Update file name if different\n",
        "df = pd.read_excel(file_path)\n",
        "\n",
        "# Check the first few rows to confirm the data\n",
        "df.head()\n",
        "\n",
        "# Count occurrences of Up and Down regulation per chromosome\n",
        "chromosome_counts = df.groupby([\"Chromosomal Location\", \"Expression\"]).size().unstack(fill_value=0)\n",
        "\n",
        "# Plot the subdivided bar graph\n",
        "fig, ax = plt.subplots(figsize=(12, 6))\n",
        "bars = chromosome_counts.plot(kind=\"bar\", stacked=True, colormap=\"coolwarm\", edgecolor=\"black\", width=0.8, ax=ax)\n",
        "\n",
        "# Add data labels\n",
        "for container in bars.containers:\n",
        "    ax.bar_label(container, fmt='%d', label_type='center', fontsize=10, color='white', weight='bold')\n",
        "\n",
        "# Graph aesthetics\n",
        "plt.xlabel(\"Chromosomal Location\")\n",
        "plt.ylabel(\"Count of circRNAs\")\n",
        "plt.title(\"Subdivided Bar Graph of Up and Down-Regulated circRNAs by Chromosomal Location\")\n",
        "plt.xticks(rotation=45)\n",
        "plt.legend(title=\"Expression\")\n",
        "\n",
        "# Show plot\n",
        "plt.show()"
      ]
    }
  ]
}