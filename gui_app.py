import streamlit as st
import pandas as pd

# Title and description
st.markdown("""
<h1 style='text-align: center;'>🏋️ Fitness Calorie Burn Estimator</h1>
<p style='text-align: center;'>Enter your workout details below to estimate the calories burned 🔥 and get health suggestions!</p>
""", unsafe_allow_html=True)

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 10, 80, 25)
weight = st.slider("Weight (kg)", 40, 150, 70)
exercise_type = st.selectbox("Exercise Type", ["Running", "Cycling", "Swimming", "Walking", "Jump Rope", "Yoga"])
duration = st.slider("Duration (minutes)", 5, 180, 30)
intensity = st.selectbox("Intensity Level", ["Low", "Medium", "High"])

# MET values (Metabolic Equivalent of Task)
met_table = {
    "Running": {"Low": 7, "Medium": 11, "High": 16},
    "Cycling": {"Low": 4, "Medium": 8, "High": 12},
    "Swimming": {"Low": 6, "Medium": 10, "High": 14},
    "Walking": {"Low": 2.5, "Medium": 3.5, "High": 5},
    "Jump Rope": {"Low": 8, "Medium": 12, "High": 16},
    "Yoga": {"Low": 2, "Medium": 3, "High": 4}
}

met = met_table[exercise_type][intensity]

# Calories burned formula
# Calories = MET x weight(kg) x duration(hr)
calories_burned = met * weight * (duration / 60)

# Output result
st.markdown("---")
st.subheader("Estimated Calories Burned:")
st.success(f"🔥 {calories_burned:.2f} kcal")

# Health Suggestions
suggestion = ""
if calories_burned < 100:
    suggestion = "This activity session is light. Try to increase your duration or intensity for better health benefits."
elif 100 <= calories_burned < 250:
    suggestion = "Good job! You’re doing moderate physical activity. Try to reach 250+ kcal per session for more significant health effects."
else:
    suggestion = "Great effort! You’re burning a high amount of calories. Make sure to hydrate and balance your nutrition."

# Extra info based on age/gender
if gender == "Male":
    recommended = 2500
else:
    recommended = 2000

age_info = ""
if age < 18:
    age_info = "As a young person, regular activity is great for growth and health. Always exercise safely."
elif age >= 60:
    age_info = "Staying active as you age is excellent! Adjust intensity to your comfort and consult your doctor if needed."

# Display suggestions
st.info(f"Suggestion: {suggestion}")
if age_info:
    st.warning(age_info)

st.markdown(f"""
<p style='font-size: 14px;'>Typical daily calorie needs: <b>{recommended} kcal</b> ({gender}).</p>
""", unsafe_allow_html=True)

# Optional: Display sample dataset
if st.checkbox("Show Sample Dataset"):
    df = pd.read_csv("calorie_dataset.csv")
    st.dataframe(df.head())

st.markdown("---")
st.caption("Note: Estimates are based on MET values and standard health recommendations. For personalized advice, consult a healthcare provider.")