"""
check that transform.py was done correctly.
"""

# check if we need to re index 
# it must be Day or Month in order for plot to show correctly

vip_objects = [pri_mat, 
               ret_mat, 
               vol_mat, 
               mca_mat, 
               bmc_mat, 
               wmc_mat, 
               bmc_mat_mthly
               ]

for d in vip_objects:
    # should be same/similar nr of rows and cols
    print(d.shape)
    # all should be day or mont 
    print(d.index.freq) 

for d in vip_objects:
    # should start/end on roughly the same dates 
    print(d.index[0], d.index[-1])
        

# see current top 10 and the date 
print("top 10", tkr_top10)
print("date", bmc_mat_mthly.index[-2])

# b matrix is indeed 10 coins
print(bmc_mat_mthly.sum(axis=1).head())
assert bmc_mat.sum(axis=1).median() == nrcoins

# w matrix have rowsum = 1
assert wmc_mat.sum(axis=1).median() == 1

# look so it is not >100 and then delete this row.
assert len(tkr_beeninblx) > 10

# and so on... todo: more cheks

# graph
pri_mat.shape[0]
tkr_sel_2 = ['Stocks', 'Bonds']
tkr_sel_3 = ['BTC', 'ETH', 'XRP']
price2aum(pri_mat.loc['2016':'2018', tkr_sel_2]).plot()
price2aum(pri_mat.loc['2016':'2018', tkr_sel_3]).plot(logy=True)

# no infinite returns
assert np.max(ret_vcc_mat).max() < 98765

# visual inspection of head and tail. do numbers appear ok?
ret_fin_mat.tail()
ret_vcc_mat.tail()
ret_vcc_mat.head()

# distributions look correct?
ret_vcc_mat.info()
if False:
    ret_vcc_mat['BTC'].plot.box()

volfr_vcc_mat.tail() # check if they dont sum to a too large number
#volfr_vcc_mat.loc['2013':'2016', tkr_sel_3].plot(title='volume_fraction')

# todo: the assert statements in the creation step above can be put here.

# plot fraction of volume 
if False:
    volfr_vcc_mat.tail()
    volfr_vcc_mat['BTC'].plot()
    volfr_vcc_mat[['BLX', 'BTC']].head(500).plot(title='volume_fraction')
    volfr_vcc_mat[['BLX', 'BTC']].tail(500).plot(title='volume_fraction')


# see how many has been top 50 
len(tkr_beentop50)
