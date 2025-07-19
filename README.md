## Employee Salary Prediction App 💼

This project is a **machine learning web app** built with **Streamlit** that predicts whether an employee's monthly income is considered **High** or **Low**, based on several features like age, education, job role, performance rating, and more.

It uses a trained classification model with a preprocessing pipeline for accurate predictions. The app allows users to input some or all feature values, while the remaining fields are automatically filled using default values calculated from the training dataset.

## Features

- Binary classification: **High Salary** vs **Low Salary**
- Custom user input form with default values fallback
- Preprocessing pipeline using `ColumnTransformer`
- Model trained with:
  - Label encoding for target variable
  - Ordinal encoding for ordered categorical features
  - One-hot encoding for nominal features
  - Standard scaling for numerical features
- Auto-fills missing inputs with mean/mode defaults
- Fully interactive UI built with Streamlit

## Tech Stack

- 🧠 **Modeling**: Scikit-learn, XGBoost, LightGBM
- 📊 **Data Processing**: Pandas, NumPy
- 🌐 **Web UI**: Streamlit
- 🔐 **Serialization**: Joblib
