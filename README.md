# 🌍 CO₂ Emission Forecasting using Machine Learning

This project involves building a machine learning model to **forecast CO₂ emissions** based on historical data. The goal is to enable **data-driven climate action** by predicting emission trends, aiding in policy design, industrial planning, and environmental research.


## 📁 Project Structure

├── data_cleaned.csv               # Cleaned dataset used for modeling
├── data_week1.ipynb               # Data analysis and cleaning (Week 1)
├── data_week2.ipynb               # Feature selection, exploration (Week 2)
├── data_week3.ipynb               # Model building, evaluation & saving (Week 3)
├── forecasting_co2_emmision.pkl   # Trained ML model (saved using joblib)
├── Week_3_Project_PPT_Template1.pptx  # Project presentation


# 🎯 Project Goal

To develop an accurate and reliable forecasting model for predicting future CO₂ emission levels using historical data and machine learning techniques. This supports proactive environmental planning and climate policy-making.


# 🛠️ Tools and Technologies

Python (Pandas, NumPy, Matplotlib, Seaborn)

Scikit-learn (regression models, metrics)

Jupyter Notebooks

Joblib (for saving the model)

Git & GitHub (version control)


# 📊 Methodology

**Data Cleaning (data_week1.ipynb)**

Removed null values and outliers

Handled missing data

**Feature Engineering & EDA (data_week2.ipynb)**

Correlation analysis

Feature selection

Visualizations

**Modeling & Evaluation (data_week3.ipynb)**

Trained regression models (e.g., Linear Regression)

Evaluated using MAE, RMSE

Saved the final model (forecasting_co2_emmision.pkl)


# 📈 How to Use the Model

import pandas as pd
import joblib

# Load cleaned data and model
df = pd.read_csv('data_cleaned.csv')
model = joblib.load('forecasting_co2_emmision.pkl')

# Prepare input features (replace with actual feature names)
X = df[['feature1', 'feature2', 'feature3']]  # Update this line

# Predict CO₂ emissions
predictions = model.predict(X)

print(predictions)


# 📷 Screenshots & Outputs

![Screenshot 2025-07-01 221243](https://github.com/user-attachments/assets/0ae27073-06aa-45d5-b2df-6c4b4e836c2c)


# 🚀 Future Scope

Integrate live emission data sources (e.g., satellite data).

Deploy as a web app using Streamlit or Flask.

Use advanced models like LSTM or Prophet for time-series forecasting.




