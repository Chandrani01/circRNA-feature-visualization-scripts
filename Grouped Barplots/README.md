# circRNA Feature Visualization – Grouped Bar Plot

This repository contains a Python script for generating grouped bar plots to visualize categorized circRNA data. It is particularly suited for comparing percentage-based distributions across different circRNA-related features.

Features
> Grouped bar plot for multiple circRNA features.
> Percentage values shown above each bar.
> Subcategory labels embedded inside the bars.
> Customizable labels, colors, and layout.
> Ready-to-use for visual summaries of binary feature distributions.

There are 3 types of grouped barplots shown here:
> circRNA Counts of on any one circRNA Feature based on expression: This grouped bar plot illustrates the distribution of circRNAs categorized by a single selected feature (e.g., GC content, localization, etc.) according to their expression status (Upregulated/Downregulated). The exact count of circRNAs is labeled on each bar.

> Grouped Bar Chart of circRNA Expression Distribution by any one circRNA Feature: This grouped bar chart visualizes the distribution of circRNAs based on a single selected feature (such as GC content, localization, or type) and their expression status (Upregulated or Downregulated). Each bar represents the number of circRNAs in a specific category, with counts labeled directly on the bars for clarity. The values are presented as percentages to allow normalization and comparison across categories.

> Grouped Bar Chart Representing Multiple circRNA Features and Their Subcategories:
This grouped bar chart displays the distribution of circRNAs across multiple features and their respective subcategories (e.g., GC content: High/Low, Localization: Cytoplasm/EV, Type: ciRNA/ecircRNA). The chart focuses on one expression group (e.g., Upregulated) and shows how circRNAs are distributed among different biological attributes. Percentages are used for normalization, allowing visual comparison between features with varying total counts.
