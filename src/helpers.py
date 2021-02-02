"""Helps for the simulations."""

import pandas as pd
import matplotlib.pyplot as plt

import os


def get_df(data):
    """Create a Pandas Dataframe from the rolls data."""
    df = pd.DataFrame({
        'Dice Rolls': list(data.keys()),
        'Rolls': list(data.values())
    })
    df.sort_values(by=['Dice Rolls'], inplace=True)
    return df


def write_csv(df, mode, number_of_rolls):
    """Write the rolls data to a CSV file."""
    if not os.path.exists('results/csv'):
        os.makedirs('results/csv')
    df.to_csv(f'results/csv/{mode}-mode-{number_of_rolls}.csv', index=False)


def write_chart(df, mode, number_of_rolls):
    """Plot the rolls data as a chart."""
    if not os.path.exists('results/png'):
        os.makedirs('results/png')
    df.plot(x ='Dice Rolls', y='Rolls', kind = 'bar')
    plt.savefig(f'results/png/{mode}-mode-{number_of_rolls}.png')


def plot_chart(df):
    """Plot the rolls data as a chart."""
    df.plot(x ='Dice Rolls', y='Rolls', kind = 'bar')
    plt.show()
