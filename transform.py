"""
before reading the code, it will help if you have read the file
naming-convention-objects.md

transform.py applies functions to the data.
the script transform the input data into objects we will use for calculations.

example objects are:
* W matrix
* B matrix
* market cap matrix
* volume matrix
* returns matrix.
"""

## chose the number of coins in the index

nrcoins = 10

## choose startdate. used for $100 plot and more.

start1 = '2017-03'

## create B and W matrix, important object

# monthly B matrix
mca_vcc_mat_monthly = mca_vcc_mat.resample('M', convention='start').asfreq()
b_mat_monthly = mca_vcc_mat_monthly.apply(top_binarizer, p=nrcoins, axis=1)

#  monthly W matrix
mca_chosen_mat_monthly = b_mat_monthly * mca_vcc_mat_monthly
w_mat_monthly = mca_chosen_mat_monthly.div(mca_chosen_mat_monthly.sum(axis=1), axis=0)

# daily W and B matrix
w_mat = w_mat_monthly.reindex(dtindex_vcc, method='ffill')
b_mat = b_mat_monthly.reindex(dtindex_vcc, method='ffill')

# note
"""
note that the w mat and b mat have a daily index, not weekdays.
then when we do an inner join with vcc and end up with an index of weekdays.
"""

## create ticker lists of coins in the fund

# current top 10 coins
tkr_top10 = b_mat_monthly.columns[b_mat_monthly.iloc[-2] == 1]
tkr_top10 = tkr_top10.tolist()

# coins that has been a member of the index at some date
tkr_beeninblx = b_mat_monthly.columns[b_mat_monthly.sum() > 0]

## create returns from prices, on fin and vcc

ret_vcc_mat = price2return(pri_vcc_mat)
ret_fin_mat = price2return(pri_fin_mat)

## create vector for our ETN: market cap, return, price, volume

# create blx vector
ret_blx_vec = (ret_vcc_mat * w_mat).sum(axis=1)
pri_blx_vec = return2aum(ret_blx_vec[start1:])
mca_blx_vec = (mca_vcc_mat * b_mat).sum(axis=1)
vol_blx_vec = (vol_vcc_mat * b_mat).sum(axis=1)

# rename
ret_blx_vec.name = 'BLX'
mca_blx_vec.name = 'BLX'
pri_blx_vec.name = 'BLX'
vol_blx_vec.name = 'BLX'

## choose which coins to be the selected ones in graphs.

# userinputchoice
tkr_sel = ['Bitcoin', 'Ethereum']

## create ret_mat

"""
ret_mat is the matrix containing all cols we will use
nts: compare with In[99]
pandas will join on index.
https://pandas.pydata.org/pandas-docs/stable/merging.html#joining-on-index
"""

# step 1: merge fin with vcc.
ret_finvcc_mat = ret_fin_mat.join(ret_vcc_mat, how='inner')

# step 2: merge vcc and fin with blx
ret_mat = ret_finvcc_mat.join(ret_blx_vec, how='inner')
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

mca_mat = ret_fin_mat.join(ret_vcc_mat, how='inner').join(ret_blx_vec, how='inner')

## create volume matrices

# edit vol_vcc
assert vol_vcc_mat.shape[1] == C
vol_vcc_mat['Total'] = vol_vcc_mat.sum(axis=1)
vol_vcc_mat['Others'] = vol_vcc_mat['Total'] - vol_vcc_mat[tkr_sel].sum(axis=1)
vol_vcc_mat['BLX'] = vol_blx_vec

# create volfr_
volfr_vcc_mat = vol_vcc_mat.div(vol_vcc_mat['Total'].values, axis=0)

# create vol_mat. keep weekdays index
vol_mat = vol_fin_mat.join(vol_vcc_mat)
assert vol_mat.shape[1] == vol_vcc_mat.shape[1] + 3

## create market cap matrices

# exact same code as volume matrices above

# edit mca_vcc
assert mca_vcc_mat.shape[1] == C
mca_vcc_mat['Total'] = mca_vcc_mat.sum(axis=1)
mca_vcc_mat['Others'] = mca_vcc_mat['Total'] - mca_vcc_mat[tkr_sel].sum(axis=1)
mca_vcc_mat['BLX'] = mca_blx_vec

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
