
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Animal Shelter Dashboard", layout="wide")

st.title("Animal Center Data Analysis Dashboard")

st.markdown("""
### Project Overview
This dashboard analyzes animal shelter intake and outcome data to identify
patterns in animal types, adoption rates, and breed distributions.
""")

# Load datasets
intakes = pd.read_csv("DataSet_Animal_Center_Intakes.csv")
outcomes = pd.read_csv("DataSet_Animal_Center_Outcomes.csv")

# Convert DateTime safely
intakes["DateTime"] = pd.to_datetime(intakes["DateTime"], errors="coerce")
outcomes["DateTime"] = pd.to_datetime(outcomes["DateTime"], errors="coerce")

# Sidebar
st.sidebar.title("Dashboard Filters")

animal_filter = st.sidebar.selectbox(
    "Select Animal Type",
    ["All"] + list(intakes["Animal Type"].dropna().unique())
)

if animal_filter != "All":
    intakes = intakes[intakes["Animal Type"] == animal_filter]
    outcomes = outcomes[outcomes["Animal Type"] == animal_filter]

st.sidebar.markdown("---")
st.sidebar.markdown("Developed by **Shivam Kumar**")
st.sidebar.markdown("[GitHub](https://github.com/)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/)")

# KPI Metrics
st.header("Key Statistics")

col1, col2, col3, col4 = st.columns(4)

total_animals = intakes.shape[0]
dogs = intakes[intakes["Animal Type"] == "Dog"].shape[0]
cats = intakes[intakes["Animal Type"] == "Cat"].shape[0]
adoptions = outcomes[outcomes["Outcome Type"] == "Adoption"].shape[0]

col1.metric("Total Animals", total_animals)
col2.metric("Total Dogs", dogs)
col3.metric("Total Cats", cats)
col4.metric("Total Adoptions", adoptions)

st.markdown("---")

# Dataset preview
st.header("Dataset Preview")
st.dataframe(intakes.head())

# Download data
st.download_button(
    label="Download Intakes Dataset",
    data=intakes.to_csv(index=False),
    file_name="animal_intakes.csv",
    mime="text/csv"
)

st.markdown("---")

# Animal Type Distribution
st.header("Animal Type Distribution")

animal_counts = intakes["Animal Type"].value_counts()

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    animal_counts.plot(kind="bar", ax=ax)
    ax.set_title("Distribution of Animal Types")
    ax.set_xlabel("Animal Type")
    ax.set_ylabel("Count")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

with col2:
    fig2, ax2 = plt.subplots()
    animal_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
    ax2.set_title("Animal Type Share")
    ax2.set_ylabel("")
    st.pyplot(fig2)

st.info("Insight: Dogs and cats represent the majority of animals entering the shelter.")

st.markdown("---")

# Outcome Type Distribution
st.header("Outcome Type Distribution")

outcome_counts = outcomes["Outcome Type"].value_counts()

col3, col4 = st.columns(2)

with col3:
    fig3, ax3 = plt.subplots()
    outcome_counts.plot(kind="bar", ax=ax3)
    ax3.set_title("Outcome Type Distribution")
    ax3.set_xlabel("Outcome Type")
    ax3.set_ylabel("Count")
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
    st.pyplot(fig3)

with col4:
    fig4, ax4 = plt.subplots()
    outcome_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax4)
    ax4.set_title("Outcome Type Share")
    ax4.set_ylabel("")
    st.pyplot(fig4)

st.info("Insight: Adoption is the most common positive outcome for animals in the shelter.")

st.markdown("---")

# Top Breeds
st.header("Top 10 Most Common Breeds")

top_breeds = intakes["Breed"].value_counts().head(10)

fig5, ax5 = plt.subplots()
top_breeds.plot(kind="barh", ax=ax5)
ax5.set_title("Top 10 Breeds")
ax5.set_xlabel("Count")
st.pyplot(fig5)

st.info("Insight: Certain breeds appear more frequently in shelters, indicating breed popularity or overpopulation.")

st.markdown("---")

# Monthly Intake Trend
st.header("Monthly Intake Trend")

monthly = intakes["DateTime"].dt.month.value_counts().sort_index()

fig6, ax6 = plt.subplots()
monthly.plot(kind="line", marker="o", ax=ax6)
ax6.set_title("Monthly Intake Trend")
ax6.set_xlabel("Month")
ax6.set_ylabel("Number of Intakes")
st.pyplot(fig6)

st.info("Insight: Animal intake varies across months, showing seasonal patterns.")

st.markdown("---")

# Footer
st.markdown("Developed by **Shivam Kumar** | Data Analyst Project")

