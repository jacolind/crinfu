"""
create a bunch of different indexes using ggindex() and compare their properties.
"""


# set start end date
ret_bsk_mat.index[0]
ret_bsk_mat.index[-1]

# corr
ret_bsk_mat.corr().round(4)
ret_bsk_mat.corr().round(4).to_csv('output/corr_1.csv')

# sharpe
sharpe_1 = sharpe(ret_bsk_mat, showall=True).round(2)
sharpe_1.to_csv('output/sharpe_1.csv')
sharpe_1

# price
return2aum(ret_bsk_mat).plot(logy=True)
plt.title('$100 Investment')
plt.ylabel('Value')
plt.savefig('output/pri_bsk_a.png')

# corr over time
cor90_bsk_mat = ret_bsk_mat.rolling(365).corr(ret_bsk_mat[r1.name])
cor90_bsk_mat = cor90_bsk_mat.drop(r1.name, axis=1)
cor90_bsk_mat.plot()
plt.ylabel('Correlation vs t10-wm-rm')
plt.title('Rolling 1y correlation \n All vs t10-wm-rm')
plt.savefig('output/bsk-rollcorr-1.png')

# see corr matrices
show_rollcorr_plot(tkr_top10_blx, start3, end3)
show_rollcorr_plot(tkr_sel_blx, start3, end3, legend=True)

# choose a few baskets
retmat1 = pd.concat([r1, r2, r3, r8,
                     ret_vcc_mat.BTC], axis=1)
retmat1.isnull().sum()

# describe. how does ithandla na?
retmat1.describe()

# sharpe
sharpe(retmat1, showall=True)

ret_bsk_mat.columns
ret_bsk_mat.columns[-1+3]


# inforatio
information_ratio(retmat1)


# risk return
pd.concat([sharpe(retmat1, showall=True),
           information_ratio(retmat1),
           tracking_error(retmat1)],
          axis=1).T.round(2).to_csv('output/riskret1.csv')

# ret and vol by year
retmat1_yearly_mean = (retmat1.groupby(retmat1.index.year)).mean().round(2)*365
retmat1_yearly_mean.to_csv('output/retmat1_yearly_mean.csv')
retmat1_yearly_vol = (retmat1.groupby(retmat1.index.year)).std().round(2)*np.sqrt(365)
retmat1_yearly_vol.to_csv('output/retmat1_yearly_vol.csv')


# rolling sharpe
retmat1.rolling(365).apply(sharpe).rolling(30).mean().plot()
plt.title('Sharpe ratio rolling 1y')
plt.ylabel('Sharpe ratio \n (Smoothed with 30d mean)')
plt.savefig('output/retmat1_rolling_sharpe_1.png')


# describe
