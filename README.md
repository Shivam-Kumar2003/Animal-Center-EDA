# Exploratory Data Analysis on Animal Center Intakes and Outcomes
### Animal Center Data Analysis Dashboard

## Live Dashboard
🔗 https://animal-center-eda-28.streamlit.app

## Overview
This project performs **Exploratory Data Analysis (EDA)** on animal shelter datasets to understand patterns related to animal intake and their final outcomes.  
The analysis helps in identifying trends such as the types of animals entering shelters, their conditions at intake, and the outcomes after their stay at the shelter.

The project uses **Python data analysis and visualization libraries** to explore and extract meaningful insights from the dataset.

---

## Objectives
- Understand the structure of animal intake and outcome datasets
- Identify missing values and clean the data
- Analyze the types of animals entering the shelter
- Study intake conditions and intake types
- Analyze outcome types and patterns
- Visualize trends using graphs and charts

---

## Dataset Description

### Animal Center Intakes Dataset
This dataset contains information about animals entering the shelter.

Main attributes include:
- Animal ID
- Name
- DateTime
- MonthYear
- Found Location
- Intake Type
- Intake Condition
- Animal Type
- Sex upon Intake
- Age upon Intake
- Breed
- Color

Total Records: **124,120**

---

### Animal Center Outcomes Dataset
This dataset contains information about the outcomes of animals after entering the shelter.

Main attributes include:
- Animal ID
- Name
- DateTime
- MonthYear
- Date of Birth
- Outcome Type
- Outcome Subtype
- Animal Type
- Sex upon Outcome
- Age upon Outcome
- Breed
- Color

Total Records: **124,491**

---

## Technologies Used
- Python
- Jupyter Notebook
- Pandas
- Matplotlib

---

## Project Workflow

1. Import necessary Python libraries
2. Load the datasets
3. Explore dataset structure
4. Check for missing values
5. Perform basic data cleaning
6. Analyze key features in the dataset
7. Create visualizations to understand patterns
8. Interpret insights from the data

---

## Key Analysis Performed
- Dataset structure analysis
- Missing value identification
- Distribution of animal types
- Intake type analysis
- Outcome type analysis
- Data visualization using charts

---

## Project Structure
#### Run Locally

Run the Streamlit app:

streamlit run Dashboard.py

Then open in your browser:

http://localhost:8501
