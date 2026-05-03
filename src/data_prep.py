"""Data preparation helpers for the used car pricing analysis."""

import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')


def load_vehicle_data(path='../data/vehicles.csv'):
    """Load the used car dataset from the repository data folder."""
    return pd.read_csv(path)


def display_dataset_overview(df):
    """Print the first rows, info, and numeric summary for a DataFrame."""
    print('Data sample:')
    print(df.head(), '\n')
    print('Data info:')
    print(df.info(), '\n')
    print('Numeric summary:')
    print(df.describe(), '\n')


def get_missing_values(df):
    """Return a DataFrame summarizing missing-value counts and percentages."""
    missing = pd.DataFrame({
        'Missing Count': df.isnull().sum(),
        'Missing %': (df.isnull().sum() / len(df) * 100).round(2)
    })
    return missing.query('`Missing Count` > 0').sort_values('Missing %', ascending=False)


def clean_vehicle_data(df):
    """Clean the dataset with basic filtering and drop columns not used in analysis."""
    df = df.copy()

    df = df[(df['price'] >= 500) & (df['price'] <= 150_000)]
    df = df[(df['odometer'] >= 0) & (df['odometer'] <= 500_000)]
    df = df[(df['year'] >= 1990) & (df['year'] <= 2024)]

    df = df.drop(columns=['size', 'cylinders', 'id'], errors='ignore')
    df = df.dropna(subset=['price', 'year', 'manufacturer', 'odometer', 'transmission', 'fuel'])

    return df.reset_index(drop=True)
