'''
this scriaapt aims to replace 4b-1_ggindex.py
and once it has, 4b-2 will be modified so that is uses ggbasket not ggindex

# todo what to borrow from ggindex.py :

## assert input is valid, it is easier now with smaller f()

```
## check input is valid

# df has a freq
# todo

# df nr cols > 1 otherweise we cannot make an index
assert len(mcap.columns) > 1

# nrtop is >0 and integer
assert nrtop > 0
assert isinstance(nrtop, int)

# name is a string
assert isinstance(name, basestring)
```

'''


## start end date

def date_slicer(df, start='', end='', startafter=365):
  # default: start 1y after df first day. end on last day.
  # override this default using params start and end.
  if start=='':
      start = df.index[startafter]
  if end=='':
      end = df.index[-1]
  # slice by dates
  return df.loc[start:end]

## mcap2binary

def mcap2binary(marketcap_matrix,
                # below is all the "rules" of the basket
                nrtop, rebalance_freq,
                blacklist='', forcelist=''):
  '''
  input marketcap matrix and basket rules, output binary matrix.

  input data
    :param marketcap_matrix:
  input params that decides the basket rules:
    :param nrtop:
    :param rebalance_freq:
    :param blacklist:
    :param forcelist:
  :return: a binary matrix with same frequency as the input

  this function is used before creating weights.
  this function does not care about smoothing and max min weights, that is handled later.
  '''

  # rebalance frequency
  mcap_mthly = marketcap_matrix.resample(rebalance_freq, convention='start').asfreq()
  # provar ny metod nu 12 dec
  mcap_mthly = marketcap_matrix.resample(rebalance_freq).first()

  # object has name _mthly for simplicity, as it is the default value.

  # ranked market cap. larget market cap gets 1, second largest 2, etc.
  ranked_mcap_mthly = mcap_mthly.rank(axis=1, method='first', ascending=False)

  # binary market cap. 1 for included, 0 for excluded.
  binary_mthly = ranked_mcap_mthly < (1 + nrtop)

  # blacklist and forcelist:
  # binary matrix zero <=> asset is always excluded
  # binary matrix one <=> asset is always included
  binary_mthly = blacklist_binary(binary_mthly, blacklist)
  binary_mthly = forcelist_binary(binary_mthly, forcelist, nrtop)

  # return binary matrix with same freq as the input
  return binary_mthly.reindex(marketcap_matrix.index, method='ffill')

## help functions for mcap2binary()

def blacklist_binary(binary_mthly, blacklist):
  '''
  the assets in forcelist get a zero in the binary matrix.
  input their tickers in the form of a py list.
  other choices available are: 'stablecoins'.
  '''
  # binary matrix zero <=> asset is always excluded
  if blacklist != '':
    binary_mthly.loc[:, blacklist] = 0
  if blacklist == 'stablecoins':
    stablecoins = ['USDT', 'MKR', 'BTS']
    binary_mthly.loc[:, stablecoins] = 0
  '''
  todo add functionality to say ["stablecoins", "LTC"]as input. 
  todo not prio: add optionality to force something after a certain date only.
  '''



  return binary_mthly

def forcelist_binary(binary_mthly, forcelist, nrtop):
  '''
  the assets in the forcelist get a one in the binary matrix.


  method A:
  on those dates where coins in includelist is not top n
  coins that are forced include will put away the smallest coins

  method B:
  if a coin in the forcelist is not included, then
  include it and increase the nr of coins

  do method B.
  '''

  # binary matrix one <=> asset is always included
  if forcelist != '':
    # modify df
    binary_mthly.loc[:, forcelist] = 1

    # there is one issue with the method above, namely the last row.
    # if last row had zero before, make it so again:
    last_row_sum = binary_mthly.iloc[-1, :].sum()
    if last_row_sum == 0:
      binary_mthly.iloc[-1, :] = 0

    # see if any day has >n coins (due to forcelist)
    nr_included = (binary_mthly > 0).sum()
    more_contituents = (nr_included > nrtop)
    if more_contituents:
        print("Due to Forcelist, the number of coins is sometimes more than",
              nrtop)

  return binary_mthly

## binary2weight

def binary2weight(binary_matrix, marketcap_matrix,
                  # now list all rules
                  rebalance_freq,
                  weighting=['marketcap', 'equal', 'custom'],
                  smooth=False,
                  custom_assets = [], custom_weights=[],
                  weight_max=1, weight_min=0):
  """
  input two df: marketcap and binary matrices. often daily freq.
  output one df: weight matrix.

  the function  does not care about nrtop or blacklist or forcelist,
  that info is contained in binary matrix.
  """
  ## calc weights based on parameter `weighting`. three cases can occur.
  if weighting == 'marketcap':
    if smooth:
      # todo read more on smoothing optoins for my understanding. and maybe let user decide more?
      marketcap_matrix = marketcap_matrix.ewm(span=30).mean()
    # convert freq. for example daily to monthly
    b_mthly = binary_matrix.resample(rebalance_freq,
                                     convention='start').asfreq()
    b_mthly = binary_matrix.resample(rebalance_freq).first()
    m_mthly = marketcap_matrix.resample(rebalance_freq,
                                        convention='start').asfreq()
    m_mthly = marketcap_matrix.resample(rebalance_freq).first()
    # W matrix is normalized B * M
    b_times_m_mthly = b_mthly * m_mthly
    # normalize so weight sum to 1
    w_mat_mthly = b_times_m_mthly.div(b_times_m_mthly.sum(axis=1), axis=0)
    # resample back to same freq as the input mcap matrix
    weights_matrix = w_mat_mthly.reindex(marketcap_matrix.index,
                                         method='ffill')
  if weighting == 'equal':
    weights_matrix = binary_matrix.div(binary_matrix.sum(axis=1), axis=0)
  if weighting == 'custom':
    # todo this part of function not written yet.
    assert sum(custom_weights) == 100
    assert len(custom_assets) > 0
    '''
    if custom_assets is a list of symbols, interpret it as == forcelist
    if custom_assets is an integer (e.g. 5) interpret it as top 5, and then we interpret custom_weights as this: second position is 30 => second largest asset has 30% weight.
    '''
    # weighting='custom', custom_assets=['BTC','XRP','LTC'], custom_weight=[50,30,20]
    if isinstance(custom_assets[0], str):
      # kan man gora saa med isinstans str? tog forst len > 0 men det aar inte korrekt tror jag.
      # all assets not in custom_assets have zero weight.
      # all assets in custom_assets have weight on each date set to custom_weights
      weights_matrix = binary_matrix # to get correct dim and index
      weights_matrix = 0  #
      weights_matrix.loc[:, custom_assets] = custom_weights/100 # funkar denna broadcast?
    if isinstance(custom_assets, int):
      assert len(custom_weights < 11) # only allow up to 10 because i was lazy when coding dictionary
      # use rank to know what asset has a certain position
      ranked_mcap = marketcap_matrix.rank(axis=1, method='first', ascending=False)
      #  map from rankings to weight
      # kan bli issue med att dict har siffror?
      dict_rank2weight = {1: custom_weights[0],
                          2: custom_weights[1],
                          3: custom_weights[2],
                          4: custom_weights[3],
                          5: custom_weights[4],
                          6: custom_weights[5],
                          7: custom_weights[6],
                          8: custom_weights[7],
                          9: custom_weights[8],
                          10: custom_weights[9]
                          }
      weights_matrix = ranked_mcap.replace(dict_rank2weight)

  ## rescale weights if min or max is imposed.
  minmax_weights_imposed = (weight_max < 1) | (weight_min > 0)
  if minmax_weights_imposed:
    weights_matrix = weights_matrix.apply(rescale_w, axis=1,
                                          weight_min=weight_min,
                                          weight_max=weight_max)

  return weights_matrix


# there must be at least one notnull value

#price2return(pri_vcc_mat) * wei1
#vol_vcc_mat * bin1

## generate general basket: ggbasket

def ggbasket(name,
             # 2binary() params
                nrtop, rebalance_freq,
                blacklist='', forcelist='',
             # 2weight() params
               weighting=['marketcap', 'equal', 'custom'],
               smooth=False,
               custom_assets=[], custom_weights=[],
               weight_max=1, weight_min=0,
             # date slicing
             start='', end='', startafter=365,
             # historical data
             marketcap_matrix = mca_vcc_mat,
             returns_matrix = price2return(pri_vcc_mat),
            volume_matrix = vol_vcc_mat):
  # input data
  # input rules
  # output weights and
  # todo write func descr

  ## clean input

  returns_matrix = returns_matrix.fillna(0)
  # todo: later, fill with na approx for volume or mcap. for now do ffill
  marketcap_matrix = marketcap_matrix.fillna(method='ffill')
  volume_matrix = volume_matrix.fillna(method='ffill')

  ## create binary matrix

  b = mcap2binary(marketcap_matrix=marketcap_matrix,
                  nrtop=nrtop, rebalance_freq=rebalance_freq,
                  blacklist=blacklist, forcelist=forcelist
                  )

  ## create weight matrix

  w = binary2weight(binary_matrix=b, marketcap_matrix=marketcap_matrix,
                    rebalance_freq=rebalance_freq,
                    weighting=weighting, smooth=smooth,
                    custom_assets=custom_assets,
                    custom_weights=custom_weights,
                    weight_max=weight_max, weight_min=weight_min
                    )



  ## create vectors and matrices

  # todo kolla att detta blir korrekt . aar ej saaker paa att det aar just haar jag ska ha dom.

  # returns_basket_vector
  rbv = returns_matrix * w.shift(1).fillna(0)
  rbv = rbv.sum(axis=1)
  # marketcap_basket_vector
  mbv = marketcap_matrix * b.shift(1).fillna(0)
  mbv = mbv.sum(axis=1)
  # volume_basket_vector
  vbv = volume_matrix * b.shift(1).fillna(0)
  vbv = vbv.sum(axis=1)

  # slice out dates
  rbv = date_slicer(rbv, start=start, end=end, startafter=startafter)
  mbv = date_slicer(mbv, start=start, end=end, startafter=startafter)
  vbv = date_slicer(vbv, start=start, end=end, startafter=startafter)
  w = date_slicer(w, start=start, end=end, startafter=startafter)

  # rename
  rbv.name = name
  mbv.name = name
  vbv.name = name
  w.name = name

  return w, rbv, mbv, vbv
