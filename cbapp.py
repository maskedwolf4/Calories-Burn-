import streamlit as st
import pickle
import pandas as pd

# Load the model
model = pickle.load(open("calories_burn_model.pkl", "rb"))

# App title and layout
st.set_page_config(page_title="Calorie Burn Prediction App", layout="centered")

# Input features with validation
st.header("Enter Your Information:")

age = st.number_input("Age", min_value=1, max_value=120)
height = st.number_input("Height (cm)", min_value=100, max_value=300)
weight = st.number_input("Weight (kg)", min_value=30, max_value=250)
duration = st.number_input("Duration (minutes)", min_value=1)
heart_rate = st.number_input("Heart Rate (BPM)", min_value=40, max_value=250)
body_temp = st.number_input("Body Temperature (°C)", min_value=35, max_value=42)

# Create a DataFrame with input features
df = pd.DataFrame({
    "Age": [age],
    "Height": [height],
    "Weight": [weight],
    "Duration": [duration],
    "Heart_Rate": [heart_rate],
    "Body_Temp": [body_temp]
})

# Predict when button is clicked
if st.button("Predict Calories Burned"):
    prediction = model.predict(df)[0]
    st.header("Predicted Calories Burned:")
    st.subheader(f"{prediction:.1f} calories")

