'''
this scriåpt aims to replace 4b-1_ggindex.py
and once it has, 4b-2 will be modified so that is uses ggbasket not ggindex

# todo what to borrow from ggindex.py :

## start end date

```
## start dates, end dates

# if start and date are empty use default values
if start=='':
    start=mcap.index[startafter]
if end=='':
    end=mcap.index[-1]
# slice by dates
mcap = mcap.loc[start:end]
ret = ret.loc[start:end]
volume = volume.loc[start:end]
```

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



## mcap2binary

def mcap2binary(marketcap_matrix,
                # below is all the "rules" of the basket
                nrtop, rebalance_freq,
                blacklist='', forcelist=''):
  '''
  input marketcap matrix and basket rules, output binary matrix.

  input data
    :param marketcap_matrix:
  input params regarding the basket rules:
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
  # object has name _mthly for simplicity, as it is the default value.

  # ranked market cap. larget market cap gets 1, second largest 2, etc.
  ranked_mcap_mthly = mcap_mthly.rank(axis=1, method='first', ascending=False)

  # binary market cap. 1 for included, 0 for excluded.
  binary_mthly = ranked_mcap_mthly < 1 + nrtop
  binary_mthly = int(binary_mthly)

  # blacklist and forcelist:
  # binary matrix zero <=> asset is always excluded
  # binary matrix one <=> asset is always included
  binary_mthly = blacklist_binary(mcap_mthly, blacklist)
  binary_mthly = forcelist_binary(mcap_mthly, forcelist)

  # return binary matrix with same freq as the input
  return binary_mthly.reindex(marketcap_matrix.index, method='ffill')


## help functions for mcap2binary()

def blacklist_binary(binary_mthly, blacklist):
  '''
  the assets in forcelist get a zero in the binary matrix.

  todo add functionality to say "stablecoins" as input. it will create a list of all stablecoins.
todo not prio: add optionality to force something after a certain date only.
  '''
  # binary matrix zero <=> asset is always excluded
  if blacklist != '':
    binary_mthly.loc[:, blacklist] = 0
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
                   weighting=['marketcap', 'equal', 'custom'],
                   custom_assets = [], custom_weights=[],
                   weight_max=1, weight_min=0):
  """
  input two df: marketcap and binary matrices.
  output one df: weight matrix.

  the function ignores frequency so it must be solved earlier.
  the function  does not care about nrtop or blacklist or forcelist,
  that info is contained in binary matrix.
  """
  # calc weights based on parameter `weighting`
  if weighting == 'marketcap':
    # monthly W matrix: B * M (element wise mult; "hadamard product")
    if smooth == True:
      # todo write this part
      # http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.ewma
      marketcap_matrix = pd.ewma(marketcap_matrix, min_periods=30)
    b_times_m = binary_matrix * marketcap_matrix
    # normalize so weight sum to 1
    weights_matrix = b_times_m.div(b_times_m.sum(axis=1), axis=0)
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
      # kan man göra så med isinstans str? tog först len > 0 men det är inte korrekt tror jag.
      # all assets not in custom_assets have zero weight.
      # all assets in custom_assets have weight on each date set to custom_weights
      weights_matrix = binary_matrix # to get correct dim and index
      weights_matrix = 0  #
      weights_matrix.loc[:, custom_assets] = custom_weights/100 # funkar denna broadcast?
    if isinstance(custom_assets, int):
      assert len(custom_weights =< 10) # only allow up to 10 because i was lazy when coding dictionary
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

  minmax_weights_imposed = (weight_max < 1) | (weight_min > 0)
  if minmax_weights_imposed:
    weights_matrix = rescale_weights_minmax(weights_matrix,
                                            weight_min, weight_max)

  return weights_matrix

## help functions for binary2weight

# two functions. first one truncates, second one both truncates and distributes.

# todo write these two from R to python

def truncate_weights(weights_matrix, weight_min, weight_max):
  # assert input is valid
  assert weight_min >= 0
  assert weight_max <= 1
  assert weight_max > 0

def rescale_weights_minmax(weights_matrix, weight_min, weight_max):
  # todo take code from R
  # functions_1.R



  w_truncate < - function(weight_original, minimum=0.01, maximum=0.30)
  {
    stopifnot(sum(weight_original) == 1)
  w1 < - if_else(weight_original > maximum,
                 maximum,
                 weight_original)
  w2 < - if_else(w1 < minimum,
                 minimum,
                 w1)
  return (w2)
  }
  wexample < - c(0.6, 0.9, 20.5, 50, 28) / 100
  w_truncate(wexample)
  w_truncate(wexample) * c(1, 1, 0, 0, 0)

  w_rescale_minmax < - function(weight_original, minimum=0.01, maximum=0.30)
  {
  # input: weights, summing to 1.
  # output: weights with max 30% and min 1%.
  # how it is done:
  # distribute leftover percentages to the ones who were not changed
  # (do it according to previous weight)

  # truncate original weights
  w_truncated < - w_truncate(weight_original, minimum, maximum)

  # calc what weights are leftovers from truncating.
  leftover < - 1 - sum(w_truncated)
  unchanged < - as.integer(weight_original == w_truncated)
  tot_mcap_unchanged < - sum(w_truncated * unchanged)

  # if changed from the truncation,
  # take that (so it becomes 30% or 1%)
  # if unchanged then distribute leftover in accordance with original market cap
  w_final < - if_else(unchanged == 1,
                      w_truncated + leftover * weight_original / tot_mcap_unchanged,
                      w_truncated)
  stopifnot(1 == sum(w_final))
  return (w_final)

}


## generate general basket: ggbasket

def ggbasket(name,
             marketcap_matrix,
             returns_matrix, volume_matrix,
             # 2binary() params
                nrtop, rebalance_freq,
                blacklist='', forcelist='',
             # 2weight() params
               weighting=['marketcap', 'equal', 'custom'],
               custom_assets=[], custom_weights=[],
               weight_max=1, weight_min=0
             ):
  # input data
  # input rules
  # output weights and
  # todo write func descr

  # create binary matrix
  b = mcap2binary(marketcap_matrix,
                  nrtop, rebalance_freq,
                  blacklist, forcelist
                  )

  # create weight matrix
  w = binary2weight(b,
                    weighting,
                    custom_assets, custom_weights,
                    weight_max, weight_min
                    )

  # create vectors and matrices

  # returns_basket_vector
  rbv = returns_matrix * w.shift(1).fillna(0) # todo kolla att detta blir korrekt . är ej säker på att det är just här jag ska ha dom. 
  # marketcap_basket_vector
  mbv = marketcap_matrix * b.shift(1).fillna(0)
  # volume_basket_vector
  vbv = volume_matrix * b.shift(1).fillna(0)

  # rename
  rbv.name = name
  mbv.name = name
  vbv.name = name

  return w, rbv, mbv, vbv


# code below will go into 4b-2_transform.py
# ---------------------------------------------------------------------------------

# naming convention: one letter indicating parameter, then a letter/number indicating answer on that parameter
# top 10, weighted marketcap, rebalanced monthly
w1, r1, m1, v1 = ggbasket(name='t10-wm-rm',
                          marketcap_matrix=mca_vcc_mat,
                          returns_matrix=ret_vcc_mat,
                          volume_matrix=vol_vcc_mat,
                          nrtop=10,
                          rebalance_freq='M',
                          weighting='marketcap'
                          )
# top 10, weighted marketcap smoothed, rebalanced monthly
w1, r2, m2, v2 = ggbasket(name='t10-wms-rm', )
# as above but no stablecoins
ggbasket(name='t10-wms-rm-nostable', )
# top 10, weighted marketcap smoothed, rebalanced monthly, limits lower 1% upper 30%
ggbasket(name='t10-wms-rm-l1u30', )
# top5, weighted equal, rebelanced monthly,
ggbasket(name='t5-wm-rm', )

# returns matrix of baskets
ret_bsk_mat = pd.concat([r1, r2, r3],
                        axis=0)

# corr
ret_bsk_mat.cor()
