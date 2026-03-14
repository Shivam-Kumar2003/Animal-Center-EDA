import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Animal Center Data Analysis Dashboard")

# Load datasets
intakes = pd.read_csv("DataSet_Animal_Center_Intakes.csv")
outcomes = pd.read_csv("DataSet_Animal_Center_Outcomes.csv")

# Convert DateTime safely
intakes["DateTime"] = pd.to_datetime(intakes["DateTime"], errors="coerce")
outcomes["DateTime"] = pd.to_datetime(outcomes["DateTime"], errors="coerce")

# Sidebar filter
st.sidebar.header("Filter Data")
animal_filter = st.sidebar.selectbox(
    "Select Animal Type",
    ["All"] + list(intakes["Animal Type"].dropna().unique())
)

if animal_filter != "All":
    intakes = intakes[intakes["Animal Type"] == animal_filter]
    outcomes = outcomes[outcomes["Animal Type"] == animal_filter]

# Dataset Preview
st.header("Dataset Preview")
st.write(intakes.head())

# Dataset info
st.header("Dataset Information")
st.write("Intakes Dataset Shape:", intakes.shape)
st.write("Outcomes Dataset Shape:", outcomes.shape)

# Missing values
st.header("Missing Values Summary")
st.write(intakes.isnull().sum())

# Animal Type Distribution
st.header("Animal Type Distribution")
animal_counts = intakes["Animal Type"].value_counts()

fig, ax = plt.subplots()
animal_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Animal Type")
ax.set_ylabel("Count")
st.pyplot(fig)

# Animal Type Pie Chart
st.header("Animal Type Share")

fig2, ax2 = plt.subplots()
animal_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

# Outcome Type Distribution
st.header("Outcome Type Distribution")

outcome_counts = outcomes["Outcome Type"].value_counts()

fig3, ax3 = plt.subplots()
outcome_counts.plot(kind="bar", ax=ax3)
ax3.set_xlabel("Outcome Type")
ax3.set_ylabel("Count")
st.pyplot(fig3)

# Outcome Pie Chart
st.header("Outcome Type Share")

fig4, ax4 = plt.subplots()
outcome_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax4)
ax4.set_ylabel("")
st.pyplot(fig4)

# Top 10 Breeds
st.header("Top 10 Most Common Breeds")

top_breeds = intakes["Breed"].value_counts().head(10)

fig5, ax5 = plt.subplots()
top_breeds.plot(kind="barh", ax=ax5)
ax5.set_xlabel("Count")
st.pyplot(fig5)

# Monthly Intake Trend
st.header("Monthly Intake Trend")

monthly = intakes["DateTime"].dt.month.value_counts().sort_index()

fig6, ax6 = plt.subplots()
monthly.plot(kind="line", marker="o", ax=ax6)
ax6.set_xlabel("Month")
ax6.set_ylabel("Number of Intakes")
st.pyplot(fig6)
