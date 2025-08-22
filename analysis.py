import pandas as pd

# Load data (adjust path if you placed it in /data)
try:
    df = pd.read_csv("data/quikr_car.csv")
except FileNotFoundError:
    df = pd.read_csv("quikr_car.csv")

print("Rows, Cols:", df.shape)
print(df.head(10))
