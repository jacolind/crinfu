'''
this file might be a legacy file. it is the evolution of
4_trasnform.py

but i do now know if i want to limit the data so much before doin analysis (e.g. create ret_mat) maybe i want to be flexible and concatenate _vcc with _fin whenever i feel like it, on certain selected columns.

will see what i do.
'''


## choose which coins to be the selected ones in graphs.

# userinputchoice
tkr_sel = ['BTC', 'ETH']

## create ret_mat

"""
pandas will join on index.
https://pandas.pydata.org/pandas-docs/stable/merging.html#joining-on-index
"""

# create returns matrices
ret_vcc_mat = price2return(pri_vcc_mat)
ret_fin_mat = price2return(pri_fin_mat)

# step 1: merge fin with vcc.
ret_finvcc_mat = ret_fin_mat.join(ret_vcc_mat, how='inner')

# step 2: merge vcc and fin with blx
ret_mat = ret_finvcc_mat.join(blx_mat['return'], how='inner')
assert (ret_mat.index == ret_finvcc_mat.index).all()
del ret_finvcc_mat

## create pri_mat

# pri_mat is $100 invested at the startdate
pri_mat = return2aum(ret_mat.loc[start1:])
assert (pri_mat.isnull().sum() == 0).all()
# https://stackoverflow.com/questions/4359959/overflow-in-exp-in-scipy-numpy-in-python

# assert
assert set(pri_mat.index) != set(ret_mat.index)

## create MCA matrix, the matrix containing all cols we will use

mca_mat = ret_fin_mat.join(ret_vcc_mat, how='inner').join(blx_mat['return'], how='inner')

## create volume matrices

# edit vol_vcc
vol_vcc_mat.shape[1] == C # if not equal then it was imported as a csv with more cols, not a problem per se just not super nice.
vol_vcc_mat['Total'] = vol_vcc_mat.sum(axis=1)
vol_vcc_mat['Others'] = vol_vcc_mat['Total'] - vol_vcc_mat[tkr_sel].sum(axis=1)
vol_vcc_mat['BLX'] = blx_mat['volume']

# create volfr_
volfr_vcc_mat = vol_vcc_mat.div(vol_vcc_mat['Total'].values, axis=0)

# create vol_mat. keep weekdays index
vol_mat = vol_fin_mat.join(vol_vcc_mat)
assert vol_mat.shape[1] == (vol_vcc_mat.shape[1] + 3)

## create market cap matrices

# exact same code as volume matrices above

# edit mca_vcc
mca_vcc_mat.shape[1] == C
mca_vcc_mat['Total'] = mca_vcc_mat.sum(axis=1)
mca_vcc_mat['Others'] = mca_vcc_mat['Total'] - mca_vcc_mat[tkr_sel].sum(axis=1)
mca_vcc_mat['BLX'] = blx_mat['marketcap']

# create mcafr_
mcafr_vcc_mat = mca_vcc_mat.div(mca_vcc_mat['Total'].values, axis=0)

# create mca_mat. keep weekdays index
# mca_mat = mca_fin_mat.join(mca_vcc_mat)
# assert mca_mat.shape[1] == mca_vcc_mat.shape[1] + 3

# create mca_mat. keep weekdays index
# mca_mat = mca_fin_mat.join(mca_vcc_mat)
# todo simon: import market caps on the financial data and then run the code above
# above doesnt work because we dont have mcap om fin, so in the meantime:
mca_mat = mca_vcc_mat


ret_mat = pd.concat([ret_vcc_mat, ret_fin_mat, blx_mat['returns']], axis=1)
# todo do same for vol_mat and mca_mat
