import pandas as pd

# Load CSV
df = pd.read_csv("metadata.csv")

# Quick overview
print("Rows and Columns:", df.shape)
print(df.info())
print(df.head())
print(df.isnull().sum())

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Remove rows without publish_time
df = df.dropna(subset=['publish_time'])

# Add a column for year
df['year'] = df['publish_time'].dt.year

# Add a column for abstract word count
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# Papers by year
papers_per_year = df['year'].value_counts().sort_index()
print(papers_per_year)

# Top journals
top_journals = df['journal'].value_counts().head(10)
print(top_journals)

import matplotlib.pyplot as plt
import seaborn as sns

# Line chart: papers by year
plt.figure(figsize=(8,5))
sns.lineplot(x=papers_per_year.index, y=papers_per_year.values, marker="o")
plt.title("COVID-19 Papers by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# Bar chart: top journals
plt.figure(figsize=(10,6))
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title("Top 10 Journals Publishing COVID-19 Papers")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.show()
