import pandas as pd
import numpy as np
import requests

ticker = "AMD"
APIKey = "98P8LGMO7KPBYGBL"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={APIKey}&datatype=csv'
response = requests.get(url)

if response.status_code == 200:
    with open('data.csv', 'w') as f:
        f.write(response.text)