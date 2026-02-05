import streamlit as st
import pandas as pd
import joblib

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Employee Salary Prediction", layout="centered")

# -------------------- LOAD PIPELINE --------------------
model = joblib.load("model/salary_pipeline.pkl")

# -------------------- APP TITLE --------------------
st.title("Employee Salary Class Predictor")
st.markdown(
    "Predict whether an employee's salary is **High** (> USD 7,000) "
    "or **Low** (< USD 7,000) based on their details."
)

# -------------------- SIDEBAR --------------------
st.sidebar.title("Model Info")
st.sidebar.markdown("""
This is an **Employee Salary Predictor** built using a  
**scikit-learn Pipeline** with preprocessing and classification.

- Model: Random Forest (Pipeline-based)
- Tech: Scikit-learn, Pandas
- UI: Streamlit
""")
st.sidebar.markdown("**Developed by:** Aman Kumar")
st.sidebar.markdown("---")
st.sidebar.info("Fill the details and click **Predict**.")

# -------------------- INPUT FORM --------------------
st.subheader("Enter Employee Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 18, 60, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    education_level = st.selectbox("Education Level", ["High School", "Associate Degree", "Bachelor’s Degree", "Master’s Degree", "PhD"])
    

with col2:
    job_role = st.selectbox("Job Role", ['Technology', 'Healthcare', 'Education', 'Media', 'Finance'])
    job_level = st.selectbox("Job Level", ["Entry", "Mid", "Senior"])
    years_at_company = st.slider("Years at Company", 1, 60, 5)

with col3:
    overtime = st.selectbox("Overtime", ["Yes", "No"])
    overtime = 1 if overtime == "Yes" else 0
    performance_rating = st.selectbox("Performance Rating", ['Low', 'Below Average', 'Average', 'High'])


# -------------------- PREDICTION --------------------
if st.button("Predict Salary Class"):

    input_df = pd.DataFrame([{
        "Age": age,
        "Years at Company": years_at_company,
        "Number of Promotions": promotions,
        "Company Tenure": years_at_company,   # reasonable proxy
        "Overtime": 1 if overtime == "Yes" else 0,
        "Remote Work": 0,
        "Leadership Opportunities": 0,
        "Innovation Opportunities": 0,
        "Education Level": education_level,
        "Job Level": job_level,
        "Work-Life Balance": "Good",
        "Job Satisfaction": "Medium",
        "Performance Rating": performance_rating,
        "Company Reputation": "Good",
        "Employee Recognition": "Medium",
        "Gender": gender,
        "Job Role": job_role,
        "Marital Status": "Single",
        "Company Size": "Medium"
    }])

    try:
        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.success("Predicted Salary Class: **High (> USD 7,000)**")
        else:
            st.warning("Predicted Salary Class: **Low (< USD 7,000)**")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
