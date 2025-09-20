# CORD-19 Data Explorer

This project analyzes COVID-19 research papers from the CORD-19 dataset and visualizes patterns using Python. A simple Streamlit app is included to explore the data interactively.

---

## Project Structure
Frameworks_Assignment/
│
├── cord19_analysis.py # Main Python script for analysis
├── README.md # Project documentation
├── .gitignore # Ignores datasets like CSV
└── (other Python scripts or visualization images)


---

## Dataset

This project uses the `metadata.csv` file from the [CORD-19 Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).  

**Important:** The dataset is **not included in this repo** due to its large size.

**To run this project locally:**
1. Download `metadata.csv` from Kaggle.
2. Place it in the root of the project folder (same folder as `cord19_analysis.py`).

---

## How to Run

1. Install dependencies:

```bash
pip install pandas matplotlib seaborn streamlit

Run the analysis script:
python cord19_analysis.py

(Optional) Run the Streamlit app:
streamlit run cord19_analysis.py

Features

Load and explore the dataset using Pandas
Clean and prepare the data (handle missing values, extract publication year, etc.)
Perform basic analysis (papers by year, top journals, word frequency)
Visualize results using Matplotlib and Seaborn
Interactive exploration via Streamlit

Notes

The CSV dataset is required locally to run scripts.
This setup keeps the GitHub repo lightweight and focused on code.
Anyone cloning the repo can download the dataset from Kaggle and run the project.


---

Next Steps for You:

1. Save this `.gitignore` and `README.md` in your project folder.  
2. Stage and commit them:

```bash
git add .gitignore README.md
git commit -m "Add .gitignore and update README with dataset instructions"

Push to GitHub:
git push -u origin main
