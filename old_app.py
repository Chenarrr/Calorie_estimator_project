
import streamlit as st

# Title and description
st.markdown("""
<h1 style='text-align: center;'>🏋️ Fitness Calorie Burn Estimator</h1>
<p style='text-align: center;'>Enter your workout details below to estimate the calories burned 🔥</p>
""", unsafe_allow_html=True)

# User inputs
weight = st.slider("Weight (kg)", 40, 150, 70)
age = st.slider("Age", 10, 80, 25)
gender = st.selectbox("Gender", ["Male", "Female"])
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

# Extra info
st.markdown("""
<p style='font-size: 12px;'>Note: This is an estimate based on MET values and may vary based on individual metabolism.</p>
""", unsafe_allow_html=True)


# Display sample data
st.markdown("---")
st.subheader("Sample Dataset")
df = pd.read_csv("calorie_dataset.csv")
st.dataframe(df.head())
