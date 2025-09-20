import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers")

# Load data
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df = df.dropna(subset=['publish_time'])
df['year'] = df['publish_time'].dt.year

# Interactive year selection
year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020,2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Display table
st.subheader("Sample Papers")
st.dataframe(filtered[['title','journal','year']].head(10))

# Plot papers per year
papers_per_year = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.lineplot(x=papers_per_year.index, y=papers_per_year.values, marker="o", ax=ax)
ax.set_title("Papers per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)
