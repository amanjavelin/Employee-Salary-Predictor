import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model/SalaryClassifier.pkl')
# Load default values
default_values = joblib.load('model/DefaultValues.pkl')
# Load label encoder
encoder = joblib.load('model/LabelEncoder.pkl')    

st.set_page_config(page_title="Employee Salary Prediction", layout="centered")

# App title
st.title(" Employee Salary Class Predictor")
st.markdown("Predict if an employee's salary is **High** (> USD 7000) or **Low** (< USD 7000) based on selected features.")

# Sidebar
# Sidebar - About Section
st.sidebar.title('Model Info')
st.sidebar.markdown("""
This is an **Employee Salary Predictor** that uses Light GBM Classifier to classify an employee's salary based on their details.
- Built with Scikit-learn & Pandas  
- UI by Streamlit  
""")
st.sidebar.markdown("**Developed by:** Aman Kumar")
st.sidebar.markdown("---")
st.sidebar.info("Modify the inputs and click **Predict** to see results.")

# Input form
st.subheader(" Enter Employee Details")

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

# Make prediction
if st.button(" Predict Salary Class"):

    # Prepare input with default values
    input_data = default_values.copy()
    input_data.update({
        'Age': age,
        'Gender': gender,
        'Education Level': education_level,
        'Job Level': job_level,
        'Job Role': job_role,
        'Years at Company': years_at_company,
        'Overtime': overtime,
        'Performance Rating': performance_rating,
    })

    input_df = pd.DataFrame([input_data])

    try:
        prediction = model.predict(input_df)
        salary_class = encoder.inverse_transform(prediction)[0]

        if salary_class == 'High':
            st.success("The predicted salary class is **High** (more than USD 7,000).")
        else:
            st.warning("The predicted salary class is **Low** (less than USD 7,000).")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
