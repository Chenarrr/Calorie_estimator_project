import streamlit as st
import pickle

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🔥 Calorie Burn Estimator")
age = st.number_input("Age", min_value=1)
weight = st.number_input("Weight (kg)", min_value=1)
duration = st.number_input("Exercise Duration (mins)", min_value=1)

if st.button("Estimate Calories Burned"):
    # Example input vector: [age, weight, duration]
    prediction = model.predict([[age, weight, duration]])  # adjust as needed
    st.success(f"Estimated Calories Burned: {prediction[0]:.2f}")
