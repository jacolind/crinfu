# either use this file or use the ones with name 4b- as aprefix

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

# start0 is the first day of vcc data
start1 = start0 + 2*365
# start1 = '2017-03'

# above this line = user input
# -----------------------------------------------------------------------------

## create dimensions

T = pri_vcc_mat.shape[0]
C = pri_vcc_mat.shape[1]

## create binary market cap matrix (rank method)

# monthly market cap
mca_vcc_mat_mthly = mca_vcc_mat.resample('M', convention='start').asfreq()
# ranked market caps (rmc). 1 is highest market cap.
rmc_vcc_mat_mthly = mca_vcc_mat_mthly.rank(axis=1, method='first',
                                               ascending=False)
rmc_vcc_mat_mthly.tail()
# binary market cap. True if it is in top10. False if it is outside.
bmc_mat_mthly = rmc_vcc_mat_mthly < 1 + nrcoins
# last date (on monthly freq) is
bmc_mat_mthly.index[-1]
# compare last day for monthly vs daily freq. todo: problem?
bmc_mat_mthly.index[-1] < pri_vcc_mat.index[-1]
# create daily b matrix
bmc_mat = bmc_mat_mthly.reindex(pri_vcc_mat.index, method='ffill')

## create weigth matrix

WEIGHTING = 'marketcap'

WEIGHTING == 'marketcap'

# monthly W matrix: B * M (element wise mult; "hadamard product")
b_times_m = bmc_mat_mthly * mca_vcc_mat_mthly

if WEIGHTING == 'equal':
    # update B * M: if it is positive return 1 else 0.
    b_times_m = (b_times_m > 0)

# normalize so weight sum to 1
wmc_mat_mthly = b_times_m.div(b_times_m.sum(axis=1), axis=0)

del b_times_m

# convert freq to daily
wmc_mat = wmc_mat_mthly.reindex(pri_vcc_mat.index, method='ffill')


# note
"""
note that the w mat and b mat have a daily index, not weekdays.
fin assets trade on weekdays. vcc trade every day.
=> when we do an inner join with vcc and end up with an index of weekdays.
"""


## create ticker lists  out of columns

# tkr fins is stocks, bonds, gold
tkr_fin
# all vcc tickers, over 1000
tkr_vcc = pri_vcc_mat.columns

# tkr all contain: vcc + fin + blx
# tkr_finvccblx = pri_mat.columns 3have not created that object yet!
#  # bmc include cols: vcc, Total, Others
#assert pri_vcc_mat.shape[1] < bmc_mat.shape[1]
#tkr_all = bmc_mat.columns
#assert len(tkr_all) == len(tkr_vcc) + len(tkr_fin) + 1

## create ticker lists of coins in the fund

# current top 10 coins
# binary == True, but remove BLX etc.
# must use monthly bmc.
tkr_top10 = bmc_mat_mthly.columns[bmc_mat_mthly.iloc[-2].values]
tkr_top10 = set(tkr_top10).intersection(tkr_vcc)
tkr_top10 = list(tkr_top10)
tkr_top10

# coins that has been a member of the index at some date
tkr_beeninblx = bmc_mat.columns[bmc_mat.sum() > 0]

# coins that has been in top 50 at some point
bmc_top50 = rmc_vcc_mat_mthly < 51
tkr_beentop50 = bmc_top50.columns[bmc_top50.sum() > 0]
del bmc_top50
len(tkr_beentop50)

# todo: maybe use the tkr_beentop50 to slice out and recude nr of cols in ret_mat
# since it increases efficiency. by cutting out many cols.

## create returns from prices, on fin and vcc

ret_vcc_mat = price2return(pri_vcc_mat)
pri_vcc_mat.to_csv('object/pri_vcc_mat.csv')
ret_vcc_mat.to_csv('object/ret_vcc_mat.csv')
ret_fin_mat = price2return(pri_fin_mat)

## create vector for our ETN: market cap, return, price, volume

# create blx vector
ret_blx_vec = (ret_vcc_mat * wmc_mat).sum(axis=1)
pri_blx_vec = return2aum(ret_blx_vec[start1:])
mca_blx_vec = (mca_vcc_mat * bmc_mat).sum(axis=1)
vol_blx_vec = (vol_vcc_mat * bmc_mat).sum(axis=1)

# rename
ret_blx_vec.name = 'BLX'
mca_blx_vec.name = 'BLX'
pri_blx_vec.name = 'BLX'
vol_blx_vec.name = 'BLX'

## choose which coins to be the selected ones in graphs.

# userinputchoice
tkr_sel = ['BTC', 'ETH']

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
vol_vcc_mat.shape[1] == C # if not equal then it was imported as a csv with more cols, not a problem per se just not super nice.
vol_vcc_mat['Total'] = vol_vcc_mat.sum(axis=1)
vol_vcc_mat['Others'] = vol_vcc_mat['Total'] - vol_vcc_mat[tkr_sel].sum(axis=1)
vol_vcc_mat['BLX'] = vol_blx_vec

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



# get error below i do not know what it means
#==============================================================================
# C:\Program Files\anaconda2\lib\site-packages\pandas\formats\format.py:2191: RuntimeWarning: invalid value encountered in greater
#   has_large_values = (abs_vals > 1e6).any()
# C:\Program Files\anaconda2\lib\site-packages\pandas\formats\format.py:2192: RuntimeWarning: invalid value encountered in less
#   has_small_values = ((abs_vals < 10**(-self.digits)) &
# C:\Program Files\anaconda2\lib\site-packages\pandas\formats\format.py:2193: RuntimeWarning: invalid value encountered in greater
#   (abs_vals > 0)).any()
#==============================================================================
