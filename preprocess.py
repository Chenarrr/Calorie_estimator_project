
import pandas as pd

def load_data(path='calorie_dataset.csv') -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def preprocess_input(weight, duration):
    return [[weight, duration]]
