Python Frameworks Assignment: CORD-19 Data Explorer
Overview

This project explores the CORD-19 research dataset and creates a simple Streamlit app to display insights. The goal is to practice data loading, cleaning, analysis, and visualization using Python.

The assignment focuses on:

1. Loading and exploring a dataset
2. Cleaning and preparing the data
3. Performing basic analysis
4. Creating visualizations
   5.Building a simple interactive web app with Streamlit

Dataset

The dataset used is metadata.csv from the CORD-19 dataset, which contains information about COVID-19 research papers:

Paper titles and abstracts
Publication dates
Authors and journals
Source information

Note: The full dataset is large. In this project, I worked with a subset of the metadata file.

Dataset source: CORD-19 on Kaggle

Tools & Libraries

Python 3.7+
pandas – for data manipulation
matplotlib / seaborn – for visualizations
Streamlit – for interactive web app

Install required packages:
pip install pandas matplotlib seaborn streamlit

Project Structure
Frameworks_Assignment/
├─ cord19_analysis.py # Main Python script for analysis
├─ cord19_app.py # Streamlit app script
├─ README.md # This file
├─ .gitignore # Ignore large files like CSV

Note: The metadata.csv dataset is not included in this repository due to its size. Download it from Kaggle if needed.

Features

Data Loading & Exploration
Load CSV into a pandas DataFrame
Inspect the first few rows using .head()
Check data types and missing values
Data Cleaning & Preparation
Handle missing data by removing or filling values
Convert date columns to datetime
Extract publication year and create additional columns if needed
Analysis & Visualization
Count papers by year
Identify top journals
Explore frequent words in paper titles

Visualize:

Number of publications over time (line chart)
Top journals (bar chart)Word cloud of titles
Distribution of paper counts by source
Streamlit Application
Interactive layout with title and description
Slider to filter by publication year
Display visualizations based on user selection
Show a sample of the dataset

How to Run

Run the analysis script:

python cord19_analysis.py

Run the Streamlit app:

streamlit run cord19_app.py

Make sure metadata.csv is in the same folder or update the script path accordingly.

Notes & Reflection
Large datasets are not included in the repo to prevent push errors.
Using .gitignore helps avoid pushing unnecessary files.
This assignment helped practice data manipulation, visualization, and building simple interactive apps.
