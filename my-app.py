import streamlit as st
import pandas as pd

# Define the path to your CSV file
data_path = "IceCream.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(data_path)

# Display the DataFrame in your app
st.write("Here is your data:", df)
