import pandas as pd

# Ability to support featurizing, parsing, cleaning, and wrangling datasets


def load_data(filepath: str) -> pd.DataFrame:
    """Load the CSV data into a DataFrame."""
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess the data (e.g., remove missing values)."""
    df = df.dropna()
    return df
