"""
import data from coins, which has previously been extracted using HH's R script.
saves the imported objects in memory as pandas dataframes.
"""

## virtual currencies

# read file
filepath1 = '../../data/other/raw/CryptoDataWide.csv'
df_vcc = pd.read_csv(filepath1, parse_dates=True)

# i get an error of mixed types. it is merely a warning however.
# I tried using pd.read_csv("data.csv", dtype={"CallGuid": np.int64}) but it didnt work

# index date
df_vcc['date'] = pd.to_datetime(df_vcc.date)
df_vcc.set_index('date', inplace=True)

# set index freq to daily
dtindex_vcc = pd.date_range(df_vcc.index[0], df_vcc.index[-1], freq='D')
df_vcc = df_vcc.reindex(dtindex_vcc, method='ffill')
# todo hakan, this is needed because pandas complained dates are not regular.
# this led the .freq to not be daily which we need!
# please double check the data you gave me so that this resampling does not render calculations incorrect.

# create matrices: price, marketcap, volume
pri_vcc_mat = df_vcc.filter(regex='^open.').fillna(0)
mca_vcc_mat = df_vcc.filter(regex='^market').fillna(0)
vol_vcc_mat = df_vcc.filter(regex='^volume').fillna(0)

# rename
tkr_vcc = [n.replace('open.', '') for n in pri_vcc_mat.columns]
pri_vcc_mat.columns = tkr_vcc
mca_vcc_mat.columns = tkr_vcc
vol_vcc_mat.columns = tkr_vcc

# dimensions
T = pri_vcc_mat.shape[0]
C = pri_vcc_mat.shape[1]

## traditional assets

# financial tickers
tkr_fin = ['Stocks', 'Bonds', 'Gold']

# choose start date = first day of vcc datetime index
start0 = dtindex_vcc[0]

# background information on stocks bonds gold
name_bonds = "Vanguard Total Bond Market ETF"
url_bonds = "https://www.morningstar.com/etfs/ARCX/BND/quote.html"
name_stocks = "SP500"
url_stocks = "https://stooq.pl/q/?s=^spx"
name_gold = "Commodity Futures Price Quotes for Gold (COMEX)"
url_gold = "https://www.nasdaq.com/markets/gold.aspx"
# https://stooq.pl/q/?s=iau.us is another possibel choihce for gold

# download data either online or offline
online_download = False
offline_download = not online_download

if offline_download:
    pri_fin_mat = pd.read_csv('pri_fin_mat.csv', index_col = 'Date', parse_dates=True)
    vol_fin_mat = pd.read_csv('vol_fin_mat.csv', index_col = 'Date', parse_dates=True)

if online_download:
    # download from stooql. example: https://stooq.pl/q/?s=^spx
    stocks = web.DataReader('^SPX', 'stooq', start0)
    bonds = web.DataReader('BND.US', 'stooq', start0)
    gold = web.DataReader('GC.F', 'stooq', start0)
    # concat price and volume matrix
    pri_fin_mat = pd.concat([stocks.Close, bonds.Close, gold.Close], axis=1)
    vol_fin_mat = pd.concat([stocks.Volume, bonds.Volume, gold.Volume], axis=1)
    # trim size
    pri_fin_mat = np.round(pri_fin_mat, 4)
    pri_fin_mat = pri_fin_mat[start0:]
    vol_fin_mat = vol_fin_mat[start0:]
    # rename
    pri_fin_mat.columns = tkr_fin
    vol_fin_mat.columns = tkr_fin
    # save to csv
    pri_fin_mat.to_csv('pri_fin_mat.csv')
    vol_fin_mat.to_csv('vol_fin_mat.csv')

# create new datetime index, of finance dates (weekdays)
dtindex_fin = pri_fin_mat.index
