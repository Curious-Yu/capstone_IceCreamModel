import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# One predictive method
# Methods and algorithms supporting data exploration and preparation
# Implementation of machine-learning methods and algorithms (scikit-learn)
# Functionalities to evaluate the accuracy of the data product


def evaluate_model(df: pd.DataFrame):
    """
    Evaluates the linear regression model using Temperature as the feature and Revenue as the target.

    Returns:
        mse: Mean Squared Error
        mae: Mean Absolute Error
        r2: R-squared score
    """
    X = df[["Temperature"]]
    y = df["Revenue"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return mse, mae, r2
