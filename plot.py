"""
output: interesting plots to /output/ and /output/vip/

here some objects are created, especially in the rollcor part.

not to self:
For inspiration see filestr.md
All plots here are done with a certain startdate
See html for details of inspiration. below is what i 25th of july thought was most needed.
"""

## ticker and selections

# create new ticker vectors
tkr_sel_blx = tkr_sel + ['BLX']
tkr_sel_blx_fin = tkr_sel_blx + tkr_fin
tkr_top10_blx = tkr_top10 + ['BLX']
tkr_fin_blx = tkr_fin + ['BLX']

# create color list                  ]
clr_btc = 'xkcd:greyish blue'
clr_eth = 'xkcd:slate'
clr_oth = 'xkcd:deep sea blue'
clr_blx = 'xkcd:sky blue'
alpha_ = 0.80
clr_sel = [clr_btc, clr_eth]
clr_sel_blx = [clr_btc, clr_eth, clr_blx]

## current top 10 weights

w_mat.iloc[-2,:].sort_values(ascending=True).tail(nrcoins).plot.barh()
plt.title('Top ' + str(nrcoins) + ' today')
plt.xlabel('Weight')
plt.show()

## prices: $100 investment

pri_mat[tkr_sel_blx_fin].head() # todo simon: no one not start at 100 so fix that

pri_mat[tkr_sel_blx].plot(logy=True, color=clr_sel_blx, linewidth=3)
plt.title('$100 investment a year ago')
plt.ylabel('Indexed price \n(start at $100)')
plt.savefig('output/vip/price-fund_vs_coins.png')
plt.show()
if save_large_png == True:
    plt.savefig('output/vip/price-fund_vs_coins_largesize.png', dpi=750)

## returns and sharpe, depending on startdate

# see In60 and forward in html

# define function
def returns_vol_tbl(df, assets, start, end='2018-04', T=12):
    """start with rr since it contains fund and coins returns.
    T=12 for monthly data and T=365 for daily data.
    output returnstable for a certain period.
    """
    # calc mean and vol
    returnstable = df.loc[start:end, assets].apply([np.mean, np.std])
    # sqrt T rule
    returnstable = returnstable.multiply([T, np.sqrt(T)], axis=0)
    # rename
    returnstable.index = ['Mean return', 'Historical vol']
    # add sharpe
    rett = returnstable.T
    rett['Return / Vol'] = rett['Mean return'] / rett['Historical vol']
    returnstable = rett.T
    # round
    returnstable = returnstable.round(2)
    # return
    return returnstable

# example usage. play around with the numbers and get something interesting
returns_vol_tbl(df=ret_mat, assets=tkr_sel_blx, start='2017', T=252)
returns_vol_tbl(df=ret_mat, assets=tkr_sel_blx, start='2017', T=252).plot.barh()
ret_mat_monthly = ret_mat.resample('M', convention='start').sum()
returns_vol_tbl(df=ret_mat_monthly, assets=tkr_sel_blx, start='2017', end='2018', T=12)

# compare sharpe ratios amon different years
startlist = ['2015', '2016', '2017', '2016-04', '2017-04']
for s in startlist:
    returns_vol_tbl(df=ret_mat, start=s, assets=tkr_sel_blx).plot.barh()
    plt.title("start @" + s)
    plt.show()

## returns of blx, monthly. (not important.)

# see monthly return (annualized) for blx
ret_blx_vec_monthly = price2return(pri_blx_vec.resample('M', convention='start').asfreq())
ret_blx_vec_monthly_annualized = ret_blx_vec_monthly * 12
ret_blx_vec_monthly_annualized.plot(style='.')
plt.axhline(y=ret_blx_vec_monthly_annualized.mean(), ls='--')
plt.title('BLX returns (3.2 means 320%)')
plt.ylabel('Monthly return \n annualized')
plt.show()

## correlation matrices

# chose dates for corr matrices. userinputchoice
start3 = '2015-04'
end3 = '2018-04'
title_corr = 'Correlation matrix - daily data \n from ' + start3 + ' to ' + end3

# define help-function
def show_corr_plot(cols, start, end, df, title=title_corr):
    """
    input a return matrix df (eg monthly or daily returns)
    slice the df by startdate, enddate and columns.
    output a correlation matrix plot.
    """
    corrplot(df.loc[start:end, cols].corr())
    plt.title(title_corr)
    plt.show()

# see corr matrices
tkr_corr1 = tkr_top10 + tkr_fin + ['BLX']
show_corr_plot(tkr_corr1, start3, end3, ret_mat)
show_corr_plot(tkr_corr1, start3, end3, ret_mat_monthly)
show_corr_plot(tkr_top10, start3, end3)
tkr_corr2 = tkr_fin + tkr_top10
show_corr_plot(tkr_corr2, start3, end3)

# todo: read html file and see if any important matrix is missed.
# See coins2_20180415_1017.html In [81] and forward, as well as [107] and [108]

## correlation over time

# create cor_mat
cor_mat = pd.rolling_corr(ret_mat['Bitcoin'],
                          ret_mat.drop('Bitcoin', axis=1),
                          window = 360)
title_rollcorr = 'Rolling 1y correlation \n All vs BTC'

# def plot help-function
def show_rollcorr_plot(cols, start, end, df=cor_mat, legend=False, title=title_rollcorr):
    cor_mat.loc[start:end, cols].plot(legend=legend)
    plt.ylabel('Correlation vs BTC')
    plt.title(title_rollcorr)
    plt.axhline(y=0, color='k', ls='-')
    plt.show()

# see corr matrices
show_rollcorr_plot(tkr_top10_blx, start3, end3)
show_rollcorr_plot(tkr_sel_blx, start3, end3, legend=True)
show_rollcorr_plot(tkr_fin_blx, start3, end3)


## market cap of coins vs BLX

# todo jacob run code below one last time and see it works

title_mca = 'BLX captures market capitalization'
start2 = '2015'

# plot _1
tkr_mcafr = tkr_sel + ['Others']
mcafr_vcc_mat.loc[start2:, tkr_mcafr
                 ].plot.area(color=[clr_btc, clr_eth, clr_blx])
mcafr_vcc_mat.loc[start2:, 'BLX'].plot(color=clr_blx)
plt.title(title_mca)
plt.ylabel('Fraction of total \n market capitalization')
plt.savefig('output/vip/mcap-fund_vs_coins_1.png')

# plot _2
mcafr_vcc_mat.loc[start2:, ['Bitcoin', 'Ethereum', 'BLX']
                 ].plot(color=['Orange', 'Green', 'Blue'])
plt.title(title_mca)
plt.ylabel('Fraction of total \n market capitalization')
plt.savefig('output/vip/mcap-fund_vs_coins_2.png')

# plot _3
mca_vcc_mat.loc[start2:, ['Bitcoin', 'Ethereum', 'BLX']
                ].plot(logy=True, color=['Orange', 'Green', 'Blue'])
plt.title(title_mca)
plt.ylabel('Market capitalization in USD')
plt.savefig('output/vip/mcap-fund_vs_coins_3.png')



## trading volume of coins vs BLX

# similar fashion to how you did with marketcap

title_vol = 'BLX captures more trading volume'

# plot _1
tkr_volfr = tkr_sel + ['Others']
clr_volfr = clr_sel + [clr_oth]# + [clr_blx]
volfr_vcc_mat.loc[start2:, tkr_volfr].plot.area(color=clr_volfr)
volfr_vcc_mat.loc[start2:, 'BLX'].plot(color=clr_blx)
plt.title(title_vol)
plt.ylabel('Fraction of total trading volume')
plt.savefig('output/vip/volume-fund_vs_coins_1.png')

# plot _2
volfr_vcc_mat.loc[start2:, ['Bitcoin', 'Ethereum', 'BLX']
                 ].plot(color=['Orange', 'Green', 'Blue'])
plt.title(title_vol)
plt.ylabel('Fraction of total \n trading volume')
plt.savefig('output/vip/volume-fund_vs_coins_2.png')

# plot _2rm
volfr_vcc_mat.loc[start2:, ['Bitcoin', 'Ethereum', 'BLX']
                  ].rolling(window=30).mean().plot(color=['Orange', 'Green', 'Blue'])
plt.title(title_vol + '\n smoothed with one month rolling mean')
plt.ylabel('Fraction of total \n trading volume')
plt.savefig('output/vip/volume-fund_vs_coins_2rm.png')

# plot _3
vol_vcc_mat.loc[start2:, ['Bitcoin', 'Ethereum', 'BLX']
                ].plot(logy=True, color=[clr_btc, clr_eth, clr_blx])
plt.title(title_vol)
plt.ylabel('Trading volume')
plt.savefig('output/vip/volume-fund_vs_coins_3.png')

# todo decide _1 or _2 or _# above? me, jacob, think

## coins in and out of top 10. and position changes within the top 10.

"""
definition: A coin shift has occured in month t+1 if
the set of selected coins for month t is not the same as month t+1.
This is calculated by comparing the B matrix with the lagged B matrix.
The more coinswitches the harder it would be to do it yourself.
Main goal is to see how it impacts our trading.
"""

# create vector measing nr of in/out events
b_vs_bshift_mat = b_mat_monthly.shift(1) != b_mat_monthly
nr_inout_vec = b_vs_bshift_mat.sum(axis=1)
# delete first row
nr_inout_vec = nr_inout_vec[1:]
# Coin A in and coin B out is 1 switch not 2.
nr_inout_vec = nr_inout_vec / 2

# nr of coin switches
nr_inout_vec.median()
nr_inout_vec.mean()

# plot
nr_inout_vec['2014':].plot(style='.')
plt.title('Nr of coin switches in the fund')
plt.ylabel('Coin switches')
plt.savefig('output/vip/coinswitches.png')

# summarystats
print("Nr of months with an in/out happening:",
      sum(nr_inout_vec > 0),
      "out of", len(nr_inout_vec))
print("Median nr of in/out events during a month:", nr_inout_vec.median())

# check
print("example of a shift: NEM out, IOTA in")
print(b_mat_monthly[b_mat_monthly>0].iloc[-3,].sort_values()[0:11])
print(b_mat_monthly[b_mat_monthly>0].iloc[-4,].sort_values()[0:11])

## delta weights: how much trading on each rebalancing date

# create
dw_mat_monthly = w_mat_monthly - w_mat_monthly.shift(1)
dw_mat_monthly = np.absolute(dw_mat_monthly)

# plot
dw_mat_monthly.sum(axis=1).plot(style='.', legend=False)
plt.title('How much is traded @ rebalancing date, each month?')
plt.ylabel('Percentage of AUM \n that is traded')
plt.savefig('output/vip/trading_rebalancedate.png')
plt.show()

# dw discussion
# for a description about delta weights see trading_rebalanc.txt


## woobull

"""
do like this one https://woobull.com/data-visualisation-alt-coins-that-achieved-5m-market-cap-vs-bitcoin/
https://woobull.com/data-visualisation-118-coins-plotted-over-time-this-is-why-hodl-alt-coin-indexes-dont-work/

take tkr_beeninblx, the coins that has been in the fund once. graph their price.
adjust the color of the line so that it is more transparent when it is not in the fund,
this information is inside b_mat. would be a nice graph. below is some proxy code:
"""

# trying to make a figure like woobull, attempt 1
price2aum(pri_mat.loc['2015':, tkr_top10]).plot(logy=True, legend=False)
plt.axhline(y=100, ls='--')
plt.title('Coins currently in top 10')
plt.ylabel('Price (start at 100)')
plt.savefig('output/woobull_1.png')
# todo: now edit the transpancy, see url:
# https://stackoverflow.com/questions/51841146/time-series-plot-of-assets-change-transparency-based-on-another-matrix

# attempt 2
price2aum(pri_mat.loc[:, tkr_beeninblx]).plot(logy=True, legend=False, ylim=(0, 100000000000))
plt.axhline(y=100, ls='--')
plt.title('Coins that have been in BLX')
plt.ylabel('Price (start at 100)')
plt.savefig('output/woobull_2.png')
