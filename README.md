# capstone_IceCreamModel

# Ice Cream Sales Forecasting Based on Weather Temperature

## Overview

This project will forecast ice cream sales based on weather temperature using a predictive linear regression model. The final product will feature an interactive dashboard built with Streamlit that displays various visualizations—including scatter plots, scatter plots with regression & prediction, line graphs, and histograms—to support data-driven decision-making and optimize inventory management.

## Features

- **Accurate Sales Forecasts:** Predictions will be generated using a linear regression model.
- **Intuitive Visualizations:** Visualizations such as scatter plots, line graphs, and histograms will be provided.
- **Toggleable User Interface:** Users will be able to switch between visualization types.
- **Interactive Predictions:** Users can input a temperature value to receive a revenue forecast.

## Software Requirements

### Windows 10

- **Operating System:** Windows 10
- **Python:** Python 3.7 or later (download from [python.org](https://www.python.org/downloads/))
- **Command Prompt or PowerShell:** For running commands

### macOS

- **Operating System:** macOS (10.14 or later recommended)
- **Python:** Python 3.7 or later (download from [python.org](https://www.python.org/downloads/) or install via Homebrew)
- **Terminal:** For running commands

## Library Requirements (Applicable to both Windows 10 and macOS)

This project will use the following Python libraries:

- **Streamlit** – for building the interactive dashboard
- **pandas** – for data parsing, cleaning, and manipulation
- **matplotlib** – for generating visualizations
- **scikit-learn** – for implementing and evaluating the predictive linear regression model
- **numpy** – for numerical operations

You can install these libraries via `pip` as described below.

## Installation and Setup

### Step 1: Clone the Repository

### Step 2: Create a Virtual Environment (Optional but Recommended)

Windows 10 User

```
python -m venv venv
venv\Scripts\activate
```

macOS User

```
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Libraries

Make sure you have a requirements.txt file with the following content:

```
streamlit
pandas
matplotlib
scikit-learn
numpy
```

Then, install the libraries:

```
pip install -r requirements.txt
```

Step 4: Prepare the Dataset

Make sure the IceCream.csv file in the same directory as my-app.py or adjust the file path in the code accordingly. The dataset will contain two variables:
• Temperature: Ranging from -0°C to 45°C
• Revenue: Ranging from \$10 to $1,000

Running the Application

On Windows 10:

1. Open Command Prompt or PowerShell.
2. Navigate to the project directory.
3. Activate the virtual environment (if using one): `venv\Scripts\activate`
4. Run the Streamlit application: `streamlit run my-app.py`
5. The application will open automatically in your default web browser.

On macOS:

1. Open Terminal.
2. Navigate to the project directory.
3. Activate the virtual environment (if using one): `source venv/bin/activate`
4. Run the Streamlit application: `streamlit run my-app.py`
5. The application will open automatically in your default web browser.

### Troubleshooting

• Streamlit Not Recognized:

If you encounter an error stating that streamlit is not recognized, try running: `python -m streamlit run my-app.py` or `python3 -m streamlit run my-app.py`

• Library Installation Issues:

Ensure that your virtual environment is activated and that all libraries listed in requirements.txt are installed.

### Data Source

The raw data can be obtained from the publicly available “Ice Cream Sales Dataset” on Kaggle (Satre, n.d.).

Reference:

Satre, S. (n.d.). Ice Cream Sales Dataset [Data set]. Kaggle. Retrieved February 22, 2025, from https://www.kaggle.com/datasets/sakshisatre/ice-cream-sales-dataset/data
