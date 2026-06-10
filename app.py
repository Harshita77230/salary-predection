import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Data Scientist Salary Prediction")

# Experience Level
experience = st.selectbox(
    "Experience Level",
    ["EN", "MI", "SE", "EX"]
)

# Employment Type
employment = st.selectbox(
    "Employment Type",
    ["FT", "PT", "CT", "FL"]
)

# Job Title
job = st.selectbox(
    "Job Title",
    [
        "Data Scientist",
        "Data Analyst",
        "ML Engineer",
        "Data Engineer"
    ]
)

# Remote Ratio
remote = st.slider(
    "Remote Ratio",
    0, 100, 50
)

# Company Location
location = st.selectbox(
    "Company Location",
    ["US", "IN", "UK", "CA"]
)

# Company Size
company_size = st.selectbox(
    "Company Size",
    ["S", "M", "L"]
)

# Encoding dictionaries

exp_map = {
    "EN": 0,
    "MI": 1,
    "SE": 2,
    "EX": 3
}

employment_map = {
    "FT": 0,
    "PT": 1,
    "CT": 2,
    "FL": 3
}

job_map = {
    "Data Scientist": 0,
    "Data Analyst": 1,
    "ML Engineer": 2,
    "Data Engineer": 3
}

location_map = {
    "US": 0,
    "IN": 1,
    "UK": 2,
    "CA": 3
}

company_size_map = {
    "S": 0,
    "M": 1,
    "L": 2
}

# Convert text into numbers

experience = exp_map[experience]
employment = employment_map[employment]
job = job_map[job]
location = location_map[location]
company_size = company_size_map[company_size]

if st.button("Predict Salary"):

    features = np.array([[experience,
                          employment,
                          job,
                          remote,
                          location,
                          company_size]])

    prediction = model.predict(features)

    st.success(f"Predicted Salary: ${prediction[0]:,.2f}")