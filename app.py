import streamlit as st
import pandas as pd

st.title("Car Price Prediction – Demo")

@st.cache_data
def load_data():
    try:
        return pd.read_csv("data/quikr_car.csv")
    except FileNotFoundError:
        return pd.read_csv("quikr_car.csv")

df = load_data()
st.write("Dataset preview:", df.head())

st.subheader("Quick Filters")
brand = st.selectbox("Brand", ["All"] + sorted([str(b) for b in df['brand'].dropna().unique()]) if 'brand' in df.columns else ["All"])
if brand != "All" and 'brand' in df.columns:
    st.write(df[df['brand'] == brand].head())
else:
    st.write(df.head())
