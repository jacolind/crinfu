'''
create output that is wanted by slides.

the file might get merger with some other script that analyzes risk and return
'''


## ret vol tbl

retvol_t10 = retvol(ret_vcc_mat[tkr_t10now])
retvol(ret_vcc_mat[tkr_t5hist]).round(2).\
  to_csv('output/retvol_t5.csv')
(ret_vcc_mat[tkr_t10now].mean() * 365).round(2).\
  to_csv('output/ret_t10.csv')

## ret vol scatter

retvol_t10['Sharpe'] = retvol_t10.Return / retvol_t10.Volatility
#retvol_t10.plot.scatter(x='Volatility', y='Return', c='Sharpe')

## sns scatter

retvol_t10['Symbol'] = retvol_t10.index
clinux = False
if clinux:
  sns.relplot(x='Volatility', y='Return', hue='Symbol', size='Sharpe',
              data=retvol_t10)

## ret vol scatter, w text

y = retvol_t10.Return
z = retvol_t10.Volatility
n = retvol_t10.index

fig, ax = plt.subplots()
ax.scatter(z, y, alpha=0.1)

plt.ylabel('Return')
plt.xlabel('Volatility')

for i, txt in enumerate(n):
    ax.annotate(txt, (z[i], y[i]), size=8)
plt.savefig('output/vcc/ret/retvol_scatter_text.png')

## ret vol scatter, vcc and fin

# todo make a scatter plot where col AssetClass = [vcc, fin] and then make df.plot(x, y, c='AssetClass')

## $100 invested in each of top 5

START3 = '2017-10'
pri_t5 = return2aum(ret_vcc_mat.loc[START3:, tkr_t5hist])
tkr_3 = ['BTC', 'XRP', 'ETH']
pri_tkr3 = return2aum(ret_vcc_mat.loc[START3:, tkr_3])
pri_t5.plot(logy=True)
plt.title('$100 investment')
plt.ylabel('Value')
plt.savefig('output/vcc/ret/pri_t5.png')

pri_mrkt = return2aum(r0[START3:])
pd.concat([pri_tkr3, pri_mrkt], axis=1).max()
pri_tkr3.plot(logy=True)
pri_mrkt.plot(logy=True, color='black', linewidth=2, legend=True)
plt.title('$100 investment')
plt.ylabel('Value')
plt.savefig('output/vcc/ret/pri_tkr3_market.png')

## total market cap

mca_vcc_mat.sum(1).plot(logy=True, color='black')
plt.title('Total market captalization on a log scale')
plt.ylabel('Market cap in USD')
plt.savefig('output/vcc/ret/total_marketcap.png')

## total market cap vs owning the market

mcatot = mca_vcc_mat.sum(1)
mcaret = mcatot.div(mcatot.shift(1))-1
pd.concat([mcaret, r0], axis=1).loc['2017':, :].corr()
# todo check if they are different

## create TRD and BAL

ret_fin_mat = price2return(pri_fin_mat)
TRD = 0.40 * ret_fin_mat.Stocks + 0.60 * ret_fin_mat.Bonds
TRD.name = 'TRD'
BAL = 0.05 * r1 + 0.95 * TRD
BAL.name = 'BAL'

## todo plot price of TRD, BL10, BAL

# create
retmat2 = pd.concat([TRD, r1, BAL], axis=1)
retmat2.columns = ['TRD', 'BL10', 'BAL']
retmat2 = retmat2.loc['2017-03':'2018-03', :]
retmat2.describe()

# plot
BOTTOM = 90
TOP = 130
primat2 = return2aum(retmat2.loc[START3:])
primat2.plot()
plt.title('$100 Invested')
plt.ylabel('USD')
plt.gca().set_ylim(bottom=BOTTOM, top=TOP)
plt.savefig('output/vcc/ret/pri_portfolios.png')
# table
final_prices = primat2.iloc[-1,:]
final_shrp = sharpe(retmat2.loc[START3:])
final_vol = retmat2.loc[START3:].std()*np.sqrt(365)
tbl1 = pd.concat([final_prices, final_shrp, final_vol], 1)
tbl1 = tbl1.round(2)
tbl1.columns = ['Value', 'Volatility', 'Sharpe']
tbl1.to_csv('output/vcc/ret/pri_portfolios.csv')
START3
# todo later use https://pypi.org/project/tabulate/ to export md table
retmat2.index[-1]

# plot
return2aum(retmat2)[['TRD', 'BAL']].plot()
plt.title('$100 Invested')
plt.ylabel('USD')
plt.gca().set_ylim(bottom=BOTTOM, top=TOP)
plt.savefig('output/vcc/ret/pri_portfolios_2.png')


## corr

# 5+1+5+1=12 st cols is max i think
tkr_t5hist

tkr_t5hist
tkr_sp500_top5 = ['AAPL', 'MSFT', 'AMZN', 'JNJ', 'JPM']


