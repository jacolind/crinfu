'''
file has note been updated like _ret have.
i will do that if graphs in  folder regarding volume is interesting enough
'''

# ticker
tkr_t3 = ['ETH', 'BTC', 'XRP']

## market cap of coins vs BLX

title_mca = 'Market capture'
ylabel_mca = 'Fraction of total market capitalization'

# mcafr vcc
mcafr_vcc_mat = mca_vcc_mat.div(mca_vcc_mat.sum(1), axis=0)

# create matrixes
mca_1 = pd.concat([m1, mca_vcc_mat[tkr_t3]], 1)
mcafr_1 = mca_1.div(mca_vcc_mat.sum(1), axis=0)
mca_1 = mca_1.loc[START2:]
mcafr_1 = mcafr_1.loc[START2:]

# plot 1
mcafr_1.plot()
plt.title(title_mca)
plt.ylabel(ylabel_mca)
plt.savefig('output/vcc/mca/mca_vcc_bsk1.png')

# plot 2
mcafr_1[tkr_t3].plot()
plt.title(title_mca)
plt.ylabel(ylabel_mca)
plt.savefig('output/vcc/mca/mca_vcc.png')

## trading volume of coins vs BLX

# same as above but find "mca" replace "vol"

title_vol = 'Trading volume'
ylabel_vol = 'Fraction of total trading volume'


# create matrixes
vol_1 = pd.concat([m1, vol_vcc_mat[tkr_t3]], 1)
volfr_1 = vol_1.div(vol_vcc_mat.sum(1), axis=0)
vol_1 = vol_1.loc[START2:]
volfr_1 = volfr_1.loc[START2:]

# plot 1
volfr_1.rolling(20).mean().plot()
plt.title(title_vol)
plt.ylabel(ylabel_vol)
plt.savefig('output/vcc/vol/volfr_vcc_bsk1_smooth20.png')

# plot 2
volfr_1[tkr_t3].rolling(20).mean().plot()
plt.title(title_vol)
plt.ylabel(ylabel_vol)
plt.savefig('output/vcc/vol/volfr_vcc_smooth20.png')

# plot 3
vol_1[tkr_t3].rolling(20).mean().plot()
plt.title(title_vol)
plt.ylabel('Trading volume')
plt.savefig('output/vcc/vol/vol_vcc_smooth20.png')


