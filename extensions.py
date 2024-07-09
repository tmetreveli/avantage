import requests
import pandas as pd
import matplotlib.pyplot as plt

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'
# key = "U1ZI8FRKEWU6LR4U"
key = "P0Z2ABYO32MIB5QM"
def fetch_data(symbol):
    global url
    url += f'&symbol={symbol}' + f"&apikey=key"
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame(data)
    return df

def clean_data(df):
    df_filled = df.fillna('')
    return df_filled

def convert_to_timestamp(df):
    df['Meta Data'] = pd.to_datetime(df['Meta Data'], errors='ignore')
    return df

def plot_prepare(df):
    values = []
    for i in df["Weekly Time Series"]:
        if i != "":
            value = (i["1. open"])
            values.append(float(value))
    return values
def plot(values):
    plt.hist(values, bins=30, edgecolor='black')
    plt.xlabel('Time Series Weekly')
    plt.ylabel('Price')
    plt.title('Histogram of Stock market')
    plt.grid(True)
    plt.show()

def add_price_column(df):
    # List to store extracted values
    values = []

    # Update DataFrame with extracted values
    for index, row in df.iterrows():
        i = row["Weekly Time Series"]
        if i != "":
            value = float(i["1. open"])
            values.append(value)
        else:
            values.append(None)  # or any default value you prefer

    # Add the extracted values as a new column to the DataFrame
    df['Extracted Values'] = values
    return df

symbol = "AAPL"
url += f'&symbol={symbol}' + f"&apikey={key}"
print(url)
r = requests.get(url)
data = r.json()
print(data)