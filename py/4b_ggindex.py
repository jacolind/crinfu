"""
let us do more functions and less crating objects!

currently i do this:
import data from web or long.csv
def transform function
tranform to new objects
check transform is ok and export to new objects

now i want to do this
import data from web or long.csv
def function that completes transform, check it is ok, and export to new object. all in one script.
transform to new objects and update the objects themselves, using classes (eg an index class).
"""

def create_weights(binary_matrix, marketcap_matrix, weighting_equal,
                   weight_max=1, weight_min=0):
  assert weight_min >= 0
  assert weight_max <= 1
  assert weight_max > 0
  # monthly W matrix: B * M (element wise mult; "hadamard product")
  b_times_m = binary_matrix * marketcap_matrix
  if weighting_equal:
    # update B * M: if it is positive return 1 else 0.
    b_times_m = (b_times_m > 0)
  # normalize so weight sum to 1
  weights_matrix = b_times_m.div(b_times_m.sum(axis=1), axis=0)

  limits_imposed = (weight_max < 1) | (weight_min > 0)
  if limits_imposed:
      # todo write function here
      # impose weight limits.xlsx 
  return weights_matrix


def matrices2index(returns, tradingvolume, marketcap,
                    weights, binary_marketcap):
    """
    input pd dataframes (all are matrices).
    check they are compatible.
    output an index dataframe with three cols: ret vol mcap.
    """

    # todo make assertions below more efficient

    # returns
    assert returns.shape == weights.shape
    assert returns.index == weights.index
    assert returns.index.freq == weights.index.freq
    returns_index_vec = (returns * weights).sum(axis=1)
    # marketcap
    assert marketcap.shape == binary_marketcap.shape
    assert marketcap.index == binary_marketcap.index
    assert marketcap.index.freq == binary_marketcap.index.freq
    mca_index_vec = (marketcap * binary_marketcap).sum(axis=1)
    # tradingvolume
    assert tradingvolume.shape == binary_marketcap.shape
    assert tradingvolume.index == binary_marketcap.index
    assert tradingvolume.index.freq == binary_marketcap.index.freq
    vol_index_vec = (tradingvolume * binary_marketcap).sum(axis=1)

    # combine returnsurn, tradingvolume, market cap
    df_index = pd.concat([returns_index_vec,
                            mca_index_vec,
                            vol_index_vec
                            ], axis=1)
    df_index.columns = ['return', 'marketcap', 'volume']

    return df_index

# ----------------------------------------------------------------------------

def ggindex(marketcap_matrix, returns_matrix, tradingvolume_matrix,
           start, end,
           name, top,
           rebalance_freq='M', random_rebalance=False,
           weight_max=1, weight_min=0,
           blacklist='', forcelist='',
           weighting_equal=False, smoothing=False,
           export_binarymatrix=False
           ):
  """
  ggindex() stands for generate general index.

  Input:
      marketcap_matrix and returns_matrix and tradingvolume_matrix, are pandas
      dataframes.indexed with datedate.
        todo add option to include price matrix or return matrix. instead.
      Start date and  End date, easy.
      rebalnce frequency, choose any of these http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
      Name of index
      top, the nr of constituents
      Weighting equal or market cap. default to marketcap.
      Blacklist, coins that are forbidden
      Forcelist, coins that must be included (even if they do not fulfil criteria of being in the top). including it can make nr of selected coins to be > `top`.
      Smoothing yes no
      Random rebalance yes no
      weight_max: what the maximum allowed weight is. default 1.
      weight_min: what the minimimum allowed weight is. default 0.


  Output:
      a pandas series.
      on that series we will do sharpe, inforatio, sortino ratio.

  TODO:
      todo add option to include a subclass of forbidden coins, e.g. all stablecoins, all coins tracking other assets, etc.
      write code for random rebalancing.
      write code for smoothing.
      write code for complicated inclusion criteria: only include a coin if it is in top 10 for 2 months in a row.
  """

  ## rename objects
  mcap = marketcap_matrix
  ret = returns_matrix
  volume = tradingvolume_matrix
  del marketcap_matrix
  del returns_matrix

  ## start dates, end dates

  # mcap and ret is daily freq
  mcap = mcap.loc[start:end]
  ret = ret.loc[start:end]
  volume = volume.loc[start:end]

  ## check input is valid

  # df has a freq
  # todo

  # df nr cols > 1 otherweise we cannot make an index
  assert len(df.columns) > 1

  # top is >0 and integer
  assert top > 0
  isinstance(top, int)

  # name is a string
  isinstance(name, basestring)

  # todo more checks? see the import-check.py and trasnform-check


  ## remove blacklist coins

  mcap.drop(blacklist, axis=1, inplace=True)

  ## resample to the rebalancing freq (will be converted back later)

  mcap_mthly = mcap.resample(rebalance_freq, convention='start').asfreq()
  ret_mthly = ret.resample(rebalance_freq, convention='start').asfreq()

  ## create binary market cap matrix

  # ranked market cap. larget market cap gets 1, second largest 2, etc.
  ranked_mcap_mthly = mcap_mthly.rank(axis=1, method='first', ascending=False)
  # binary market cap. 1 for included, 0 for excluded.
  bmc_mat = ranked_mcap_mthly < 1 + nrcoins

  ## force include coins in forcelist

  # method A:
  # on those dates where coins in includelist is not top n
  # coins that are forced include will put away the smallest coins
  # method B:
  # if a coin in the forcelist is not included, then
  # include it and increase the nr of coins

  # do method B.
  # set to 1 if the coins in forcelist is zero somehwere
  bmc_mat[forcelist].replace(0, 1, inplace=True)

  ## go from market cap to weights

  # apply function
  wmc_mat_mthly = create_weights(bmc_mat_mthly, mca_vcc_mat_mthly,
                                 weighting_equal)
  # resample back: convert freq to daily
  wmc_mat = wmc_mat_mthly.reindex(pri_vcc_mat.index, method='ffill')
  # see if any day has >n coins (due to forcelist)
  nr_included = (wmc_mat_mthly > 0).sum()
  (nr_included > nrcoins).any()

  ## create ticker lists

  # coins that has been a member of the index at some date
  tkr_been_in_index = bmc_mat.columns[bmc_mat.sum() > 0]
  # if you return and save bmc mat this can easily be done yourself

  ## calc and create index return, marketcap, volume captured.

  df_index = matrices2index(returns=ret, tradingvolume=volume, mcap=mcap,
                            weights=wmc_mat, binary_mcap=bmc_mat)

  ## export oject

  if export_binarymatrix:
      return df_index, bmc_mat
  return df_index




## use ggindex function to create index object

# ret not yet created. import.py exports: pri, vol, mca
ret_vcc_mat = price2return(pri_vcc_mat)
# apply ggindex with simplified BLX params.
blx_mat = ggindex(marketcap_matrix=mca_vcc_mat,
                returns_matrix=ret_vcc_mat,
                tradingvolume_matrix=vol_vcc_mat,
                start=mca_vcc_mat.index[365], end=mca_vcc_mat.index[-1],
                name='BLX', top=10,
                rebalance_freq='M', random_rebalance=False,
                blacklist='', forcelist='',
                weighting_equal=False, smoothing=False)
# see ggindex
blx_mat.head()
blx_mat.tail()










# ----------------------------------------------------------------------------
# combine xyz_vcc_mat and xyz_fin_mat with df_blx to become xyz_mat for xyz = [ret, mca, pri, mcafr, volfr]
# code below is copied from `4_transform.py`

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
mca_vcc_mat['BLX'] = blc_mat['marketcap']

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


ret_mat = pd.concat([ret_vcc_mat, ret_fin_mat, blx_mat['return']], axis=1)
# todo do same for vol_mat and mca_mat
