# circRNA Feature Visualization (Subdivided Barplot)

This repository contains a Python script for visualizing the distribution of circRNA features using subdivided barplot. The visualization helps researchers distinguish categories (e.g., upregulated vs downregulated) across various feature values such as chromosomal location, localization, or circRNA type.

Features:
> Subdivided barplot to compare two categories across feature values.
> Automatic count labeling for clear, informative plots.
> Easy-to-modify code for different circRNA features.
> Output suitable for reports or publications.

Input Format:
The input file should be in .xlsx format and contain at least three columns:
> circRNA_ID/circRNA Name
> Feature: Any categorical feature of circRNAs (e.g., Chromosomal location, Cellular Localization, circRNA Type)
> Expression: The category you want to compare (e.g., Up, Down)
