"""
check that transform.py was done correctly.
"""

# b matrix is indeed 10 coins
b_mat_monthly.sum(axis=1).head()
assert b_mat.sum(axis=1).median() == nrcoins

# w matrix have rowsum = 1
assert w_mat.sum(axis=1).median() == 1

# look so it is not >100 and then delete this row.
assert len(tkr_beeninblx) > 10

# and so on... todo: more cheks

# graph
pri_mat.shape[0]
pri_mat.iloc[200:283, 1:5].plot(logy=True)

# no infinite returns
assert np.max(ret_vcc_mat).max() < 98765

# visual inspection of head and tail. do numbers appear ok?
ret_fin_mat.tail()
ret_vcc_mat.tail()
ret_vcc_mat.head()

# distributions look correct?
ret_vcc_mat.info()
ret_vcc_mat['Bitcoin'].plot.box()

volfr_vcc_mat.iloc[0:1000,0:3].plot(title='volume_fraction')
volfr_vcc_mat.tail() # check if they dont sum to a too large number

# todo: the assert statements in the creation step above can be put here.

volfr_vcc_mat.tail()
volfr_vcc_mat['Bitcoin'].plot()
volfr_vcc_mat[['BLX', 'Bitcoin']].head(500).plot(title='volume_fraction')
volfr_vcc_mat[['BLX', 'Bitcoin']].tail(500).plot(title='volume_fraction')
