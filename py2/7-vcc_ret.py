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
tkr_sel = ['BTC', 'ETH']
tkr_fin = ['Stocks', 'Bonds'] #not gold
tkr_sel_blx = tkr_sel + ['BLX']
tkr_sel_blx_fin = tkr_sel_blx + tkr_fin
tkr_t10now_blx = tkr_t10now + ['BLX']
tkr_fin_blx = tkr_fin + ['BLX']

# create color list           
# http://www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/
#clr_btc = 'xkcd:greyish blue'
#clr_eth = 'xkcd:slate'
#clr_oth = 'xkcd:deep sea blue'
#clr_blx = 'xkcd:sky blue'
clr_btc = '#0000cd'
clr_eth = '#006400'
clr_oth = '#2f4f4f'
clr_blx = '#483d8b'
alpha_ = 0.80
clr_sel = [clr_btc, clr_eth]
clr_sel_blx = [clr_btc, clr_eth, clr_blx]




## prices: $100 investment a year ago 


# start a year ago
ret_vcc_mat.index[-1] - DateOffset(years=1)
START2 = '2015-04'
END2 = '2018-04'
pri_vcc_mat_2 = return2aum(ret_vcc_mat.loc[START2:, tkr_t5now])
pri_vcc_mat_2.plot(logy=True)
plt.title('$100 investment a year ago')
plt.ylabel('Indexed price \n(start at $100)')
plt.savefig('output/vcc/ret/price-fund_vs_coins.png')
if save_large_png == True:
    plt.savefig('output/vcc/ret/price-fund_vs_coins_largesize.png', dpi=750)

## returns and sharpe, depending on startdate

retvol(ret_vcc_mat[tkr_t10now])
sharpe(ret_vcc_mat[tkr_t10now], showall=True)

# vary the start date
plot_many_sharpe = False
if plot_many_sharpe:
  startlist = ['2015', '2016', '2017', '2016-04', '2017-04']
  for s in startlist:
    sharpe(ret_vcc_mat.loc[s:, tkr_t10now], showall=True).plot.barh()
    plt.title("start @" + s)
    plt.show()


## correlation matrices

# chose dates for corr matrices. userinputchoice
title_corr = 'Correlation matrix - daily data \n from ' + START2 + ' to ' + END2

# by the way, here is a ret mat given this choice 
# returns_vol_tbl(df=ret_mat, assets=tkr_sel_blx,
#                 start=START2, end=END2,
#                 T=252).to_csv('output/returns_vol_tbl.csv')

# todo seaborn does not exists here.



# see corr matricesS
if False:
  tkr_corr1 = tkr_t10now + tkr_fin + r0.name
  ret_all_mat = pd.concat([ret_vcc_mat, r0, ret_fin_mat])
  ret_all_mat_mthly = ret_all_mat.resample('MS').sum()
  show_corr_plot(tkr_corr1, START2, END2, ret_all_mat)
  show_corr_plot(tkr_corr1, START2, END2, ret_all_mat_mthly)
  show_corr_plot(tkr_t10now, START2, END2, ret_all_mat)
  tkr_corr2 = tkr_fin + tkr_t10now
  show_corr_plot(tkr_corr2, START2, END2, ret_all_mat)

## correlation over time

# create matrix 
ret_vcc_mat2 = ret_vcc_mat[tkr_t10now]

# corr over time top 10
cor90_vcc_mat2 = ret_vcc_mat2.rolling(365).\
  corr(ret_vcc_mat2.BTC).\
  drop('BTC', axis=1)
cor90_vcc_mat2.rolling(20).mean().plot()
plt.ylabel('Correlation vs BTC')
plt.gca().set_ylim(top=1.01)
plt.title('Rolling 1y correlation \n All vs BTC')
plt.savefig('output/vcc/ret/vcc-rollcorr-t10_smooth20.png')

# top 5
tkr_t5woBTC = tkr_t5now[1:]
cor90_vcc_mat2[tkr_t5woBTC].rolling(20).mean().plot()
plt.ylabel('Correlation vs BTC')
plt.title('Rolling 1y correlation \n All vs BTC')
plt.savefig('output/vcc/ret/vcc-rollcorr-t5_smooth20.png')


## woobull

"""
do like this one https://woobull.com/data-visualisation-alt-coins-that-achieved-5m-market-cap-vs-bitcoin/
https://woobull.com/data-visualisation-118-coins-plotted-over-time-this-is-why-hodl-alt-coin-indexes-dont-work/

take tkr_beeninblx, the coins that has been in the fund once. graph their price.
adjust the color of the line so that it is more transparent when it is not in the fund,
this information is inside b_mat. would be a nice graph. below is some proxy code:
"""

return2aum(ret_vcc_mat.loc['2016':, tkr_t10hasbeen]).\
  plot(logy=True, legend=False, alpha=0.5)
plt.title('$100 Investment')
plt.ylabel('USD value after $100 investment \n on the day it first appears on coinmarketcap.com')
plt.savefig('output/vcc/ret/woobull.png')
# todo: now edit the transpancy, see url:
# https://stackoverflow.com/questions/51841146/time-series-plot-of-assets-change-transparency-based-on-another-matrix
