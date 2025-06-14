
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

def train_model(data_path='calorie_dataset.csv'):
    df = pd.read_csv(data_path)
    X = df[['Weight_kg', 'Duration_min']]
    y = df['Calories_burned']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'model.pkl')
    print("Model trained and saved as model.pkl")
