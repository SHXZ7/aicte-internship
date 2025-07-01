import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load(r'C:\Users\chach\OneDrive\Documents\try\aicte_internship\week3\forecasting_co2_emmision.pkl')

st.title("CO₂ Emission Forecaster")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 👇 Use actual feature columns used in training
    features = ['cereal_yield','fdi_perc_gdp','gni_per_cap', 'en_per_cap',
                'pop_urb_aggl_perc', 'prot_area_perc', 'pop_growth_perc']
    
    # ✅ Ensure all required columns exist
    if all(col in df.columns for col in features):
        X = df[features]
        predictions = model.predict(X)
        df['Predicted CO2 Emission'] = predictions
        st.write(df)

        st.download_button(
    "Download Predictions as CSV",
    df.to_csv(index=False).encode("utf-8"),
    file_name="predicted_co2.csv",
    mime="text/csv"
)
        
        
    else:
        st.error("CSV file is missing one or more required columns: " + ", ".join(features))
