
import joblib
from preprocess import preprocess_input

model = joblib.load('model.pkl')

# Example test
weight = 75
duration = 45

X = preprocess_input(weight, duration)
predicted_calories = model.predict(X)
print(f"Predicted calories burned: {predicted_calories[0]:.2f} kcal")
