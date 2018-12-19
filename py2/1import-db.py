import sqlite3
from sqlite3 import Error
import time

## IndexComposition table

# Create our connection to coinmarketcap data connection and extract data.
marketcap = sqlite3.connect('input/coinmarketcap.db')
df1 = pd.read_sql_query("SELECT * FROM coinmarketcap_coin", marketcap)
df2 = pd.read_sql_query("SELECT * FROM coinmarketcap_coin_data", marketcap)
df1.info()
df2.info()