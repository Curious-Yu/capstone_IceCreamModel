import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# One descriptive method (three visualization types)
# Methods and algorithms supporting data exploration and preparation
# Data visualization functionalities for data exploration and inspection


def plot_scatter(df: pd.DataFrame):
    """Display a basic scatter plot of Temperature vs. Revenue."""
    st.subheader("Scatter Plot: Temperature vs. Revenue")
    fig, ax = plt.subplots()
    ax.scatter(df["Temperature"], df["Revenue"], alpha=0.7, label="Data Points")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Revenue ($)")
    ax.set_title("Scatter Plot: Temperature vs. Revenue")
    ax.legend()
    st.pyplot(fig)


def plot_temperature_vs_revenue(df: pd.DataFrame):
    """
    Create a scatter plot of Temperature vs. Revenue and overlay a regression line.
    """
    st.subheader("Scatter Plot with Regression Line")
    fig, ax = plt.subplots()

    # Plot the data points
    ax.scatter(df["Temperature"], df["Revenue"], alpha=0.7, label="Data Points")

    # Fit a linear regression model to the data
    X = df[["Temperature"]]
    y = df["Revenue"]
    model = LinearRegression()
    model.fit(X, y)

    # Generate a range of temperature values for plotting the regression line
    x_range = np.linspace(
        df["Temperature"].min(), df["Temperature"].max(), 100
    ).reshape(-1, 1)
    y_range = model.predict(x_range)

    # Plot the regression line
    ax.plot(x_range, y_range, color="red", linewidth=2, label="Regression Line")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Revenue ($)")
    ax.set_title("Scatter Plot: Temperature vs. Revenue with Regression")
    ax.legend()
    st.pyplot(fig)


def plot_line_graph(df: pd.DataFrame):
    """Display a line graph of Temperature vs. Revenue."""
    st.subheader("Line Graph: Temperature vs. Revenue")
    # Sort the data by Temperature for a meaningful line graph
    df_sorted = df.sort_values("Temperature")
    fig, ax = plt.subplots()
    ax.plot(
        df_sorted["Temperature"],
        df_sorted["Revenue"],
        marker="o",
        linestyle="-",
        color="green",
    )
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Revenue ($)")
    ax.set_title("Line Graph: Temperature vs. Revenue")
    st.pyplot(fig)


def plot_histogram(df: pd.DataFrame):
    """Display a histogram of Revenue distribution."""
    st.subheader("Histogram: Revenue Distribution")
    fig, ax = plt.subplots()
    ax.hist(df["Revenue"], bins=20, edgecolor="black", alpha=0.7)
    ax.set_xlabel("Revenue ($)")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram: Revenue Distribution")
    st.pyplot(fig)
