import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Animal Center Data Analysis Dashboard")

# Load datasets
intakes = pd.read_csv("DataSet_Animal_Center_Intakes.csv")
outcomes = pd.read_csv("DataSet_Animal_Center_Outcomes.csv")

st.header("Dataset Preview")
st.write(intakes.head())

st.header("Animal Type Distribution")

animal_counts = intakes["Animal Type"].value_counts()

fig, ax = plt.subplots()
animal_counts.plot(kind="bar", ax=ax)
st.pyplot(fig)

st.header("Outcome Type Distribution")

outcome_counts = outcomes["Outcome Type"].value_counts()

fig2, ax2 = plt.subplots()
outcome_counts.plot(kind="bar", ax=ax2)
st.pyplot(fig2)
