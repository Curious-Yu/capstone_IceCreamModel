"""
Data Range:
Temperature: -0°C to 45°C
Revenue: $10 to $1,000

Data Source:
Satre, S. (n.d.). Ice Cream Sales Dataset [Data set]. Kaggle. Retrieved February 22, 2025, from https://www.kaggle.com/datasets/sakshisatre/ice-cream-sales-dataset/data
"""

import streamlit as st
import pandas as pd
from descriptive import (
    plot_scatter,
    plot_temperature_vs_revenue,
    plot_line_graph,
    plot_histogram,
)
from predictive import evaluate_model
from sklearn.linear_model import LinearRegression

# Set up page configuration
st.set_page_config(page_title="Ice Cream Sales Forecasting", layout="wide")
st.title("Ice Cream Sales Forecasting Based on Temperature")

# Inform the user about the data range and data source
st.info(
    """
    **Data Range Information:**
    - **Temperature:** -0°C to 45°C  
    - **Revenue:** $10 to $1,000

    **Data Source:**  
    Satre, S. (n.d.). *Ice Cream Sales Dataset* [Data set]. Kaggle.  
    Retrieved February 22, 2025, from [https://www.kaggle.com/datasets/sakshisatre/ice-cream-sales-dataset/data](https://www.kaggle.com/datasets/sakshisatre/ice-cream-sales-dataset/data)
    """
)

# Load your dataset
# Collected or available datasets - the IceCream.csv
# Decision support functionality - there summaries that explain how each visualization informs decisions to support operational choices
data_path = "IceCream.csv"
try:
    df = pd.read_csv(data_path)
except Exception as e:
    st.error(f"Failed to load data: {e}")
    df = None

if df is not None:
    df = df.dropna()

    # Sidebar: Let user select which visualization to view
    # Implementation of interactive queries - allowing user to toggle between visualization types
    viz_option = st.sidebar.selectbox(
        "Choose Visualization Type",
        [
            "Scatter Plot",
            "Scatter Plot with Regression & Prediction",
            "Line Graph",
            "Histogram",
        ],
    )

    if viz_option == "Scatter Plot":
        st.write(
            """
            **Scatter Plot Summary:**  
            This visualization displays individual data points of Temperature versus Revenue, enabling a quick visual assessment of their direct relationship.  
            It aids decision-makers by highlighting patterns, clusters, or outliers that may influence inventory or pricing strategies.
            """
        )
        plot_scatter(df)

    elif viz_option == "Scatter Plot with Regression & Prediction":
        st.write(
            """
            **Scatter Plot with Regression & Prediction Summary:**  
            By overlaying a regression line on the scatter plot, this visualization quantifies the relationship between Temperature and Revenue.  
            The prediction feature allows for forecasting future revenue based on a given temperature, providing actionable insights for inventory and promotional planning.
            """
        )
        plot_temperature_vs_revenue(df)

        # Add prediction input below the visualization
        st.subheader("Make a Prediction")
        temperature_input = st.number_input("Enter Temperature (°C)", value=25.0)

        # Fit the model for prediction
        X = df[["Temperature"]]
        y = df["Revenue"]
        model = LinearRegression()
        model.fit(X, y)
        predicted_revenue = model.predict([[temperature_input]])
        st.write(f"Predicted Revenue ($): {predicted_revenue[0]:.2f}")

        # Evaluate model performance and display metrics
        mse, mae, r2 = evaluate_model(df)
        st.subheader("Model Evaluation Metrics")
        st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")
        st.write(f"**Mean Absolute Error (MAE):** {mae:.2f}")
        st.write(f"**R-squared (R²):** {r2:.2f}")

    elif viz_option == "Line Graph":
        st.write(
            """
            **Line Graph Summary:**  
            This line graph connects data points in sequence by Temperature, highlighting the overall trend in Revenue.  
            It supports decision-making by revealing seasonal patterns and trends that can be leveraged for resource allocation and strategic planning.
            """
        )
        plot_line_graph(df)

    elif viz_option == "Histogram":
        st.write(
            """
            **Histogram Summary:**  
            The histogram shows the frequency distribution of Revenue, offering insights into the central tendency and spread of sales figures.  
            This information assists in assessing sales performance and understanding revenue variability for risk management.
            """
        )
        plot_histogram(df)
else:
    st.error("Data is not available.")
