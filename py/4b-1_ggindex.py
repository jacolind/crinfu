"""
this file define three functions.
the first two are helper functions for the third.
"""

def create_weights(binary_matrix, marketcap_matrix,
                   weighting_equal=False,
                   weight_max=1, weight_min=0):
  """
  input two df: binary and marketcap.
  output one df: weights.

  by default market cap weighted.

  to get equal weighted, set param to True AND
  (because i was lazy when i wrote the function) simply
  use the same df for both binary and marketcap matrix input.
  """
  # assert input is valid
  assert weight_min >= 0
  assert weight_max <= 1
  assert weight_max > 0
  assert binary_matrix.shape == marketcap_matrix.shape
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
      print("limit impose is to be built")
      # impose weight limits.xlsx
  return weights_matrix


def matrices2index(returns, tradingvolume, marketcap,
                   weights_marketcap, binary_marketcap,
                   assertions=False):
    """
    input pandas dataframes (all are matrices).
    check they are compatible with each other.
    output an index dataframe with three cols: ret vol mcap.
    """

    ## calc basket returns, market cap, trading volume, price

    returns_index_vec = (weights_marketcap * returns).sum(axis=1)
    mcap_index_vec = (binary_marketcap * marketcap).sum(axis=1)
    volume_index_vec = (binary_marketcap * tradingvolume).sum(axis=1)
    aum_index_vec = return2aum(returns_index_vec)

    ## combine all to a df

    df_index = pd.concat([returns_index_vec,
                            mcap_index_vec,
                            volume_index_vec,
                            aum_index_vec
                            ],
                            axis=1)
    df_index.columns = ['returns', 'marketcap', 'volume', 'price']

    if assertions:
        # these are all matrices
        returns.shape
        weights.shape
        tradingvolume.shape
        marketcap.shape
        binary_marketcap.shape
        # with same index
        returns.index
        weights.index
        tradingvolume.index
        marketcap.index
        binary_marketcap.index
        # returns
        assert returns.shape[0] == weights.shape[0]
        assert (returns.index == weights.index).all()
        assert returns.index.freq == weights.index.freq
        returns_index_vec = (returns * weights).sum(axis=1)
        # marketcap
        assert marketcap.shape == binary_marketcap.shape
        assert (marketcap.index == binary_marketcap.index).all()
        assert marketcap.index.freq == binary_marketcap.index.freq
        mca_index_vec = (marketcap * binary_marketcap).sum(axis=1)
        # tradingvolume
        assert tradingvolume.shape == binary_marketcap.shape
        assert (tradingvolume.index == binary_marketcap.index).all()
        assert tradingvolume.index.freq == binary_marketcap.index.freq
        vol_index_vec = (tradingvolume * binary_marketcap).sum(axis=1)

    return df_index


def ggindex(marketcap_matrix,
            returns_matrix,
            tradingvolume_matrix,
            startafter=365,
            start='',
            end='',
            nrtop=10,
            rebalance_freq='M',
            random_rebalance=False,
            blacklist='', forcelist='',
            weighting_equal=False,
            smoothing=False,
            export_binarymatrix=False,
            weight_max=1, weight_min=0
            ):
  """
  ggindex() stands for generate general index.
  Input:
      _matrix: three matrices. must be pandas dataframes.
      we assume freq is daily and dates are evenly spaced.
      marketcap_matrix and returns_matrix and tradingvolume_matrix, are pandas
      dataframes.indexed with datedate.
        todo add option to include price matrix or return matrix. instead.
  Output:
      a pandas df with cols "returns, marketcap, volume, price"
      on that series we will do sharpe, inforatio, sortino ratio.
  Input optional:
      Start date and. input as string e.g. '2018-11-12'.
        defaults to start 1y after first date in mcap matrix and end the last day of that matrix.
      rebalance frequency, choose any of these http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
      nrtop, the nr of constituents. eg 5 or 10 or 20.
      Weighting, equal or market cap. default to marketcap.
      Blacklist, coins that are forbidden
      Forcelist, coins that must be included (even if they do not fulfil criteria of being in the top). including it can make nr of selected coins to be > `top`.
      Smoothing, yes no
      Random rebalance, yes no
      weight_max: what the maximum allowed weight is. default 1. used in create_weights()
      weight_min: what the minimimum allowed weight is. default 0. used in create_weights()
  TODO:
      todo add option to include a subclass of forbidden coins, e.g. all stablecoins, all coins tracking other assets, etc.
      write code for random rebalancing.
      write code for smoothing.
      test if code for blacklist and forcelist works.
      write code for complicated inclusion criteria: only include a coin if it is in top 10 for 2 months in a row.
    """

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

    # todo more checks? see the import-check.py and trasnform-check


    ## rename objects

    mcap = marketcap_matrix
    ret = returns_matrix
    volume = tradingvolume_matrix
    del marketcap_matrix
    del returns_matrix
    del tradingvolume_matrix

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

    ## remove blacklist coins

    if blacklist != '':
      mcap.drop(blacklist, axis=1, inplace=True)

    ## rebalance frequency

    # object has name _mthly for simplicity, as it is the default value.
    mcap_mthly = mcap.resample(rebalance_freq, convention='start').asfreq()

    ## create binary market cap matrix

    # ranked market cap. larget market cap gets 1, second largest 2, etc.
    ranked_mcap_mthly = mcap_mthly.rank(axis=1, method='first', ascending=False)
    # binary market cap. 1 for included, 0 for excluded.
    binary_mthly = ranked_mcap_mthly < 1 + nrtop

    ## force include coins in forcelist

    # method A:
    # on those dates where coins in includelist is not top n
    # coins that are forced include will put away the smallest coins
    # method B:
    # if a coin in the forcelist is not included, then
    # include it and increase the nr of coins

    # do method B.
    # set to 1 if the coins in forcelist is zero somehwere
    last_row_sum = binary_mthly.iloc[-1, :].sum()
    if forcelist != '':
        binary_mthly.loc[:, forcelist] = True
        # above mofidies df.
        # if last row had zero before, make it so again:
        if last_row_sum == 0:
            binary_mthly.iloc[-1, :] = False

    ## go from market cap to weights. then change to daily.

    weights_mthly = create_weights(binary_mthly,
                                   mcap_mthly,
                                   weighting_equal)
    # resample back: convert freq to daily
    # use same index as ret or volume or mcap otherwise lengths will differ
    weights = weights_mthly.reindex(index=mcap.index, method='ffill')
    binary = binary_mthly.reindex(index=mcap.index, method='ffill')
    assert (mcap.index == binary.index).all()

    # see if any day has >n coins (due to forcelist)
    nr_included = (weights_mthly > 0).sum()
    more_contituents = (nr_included > nrtop).
    if more_contituents:
        print("Due to Forcelist, the number of coins is sometimes more than",
              nrtop)

    ## create ticker lists

    # coins that has been a member of the index at some date
    tkr_been_in_index = binary_mthly.columns[binary.sum() > 0]
    # if you return and save bmc mat this can easily be done yourself

    ## calc and create index return, marketcap, volume captured.

    # matrices2index: assert shapes are correct and concat them to one df
    df_index = matrices2index(returns=ret,
                              tradingvolume=volume,
                              marketcap=mcap,
                              weights_marketcap=weights,
                              binary_marketcap=binary)
    # i get first two rows NAA for marketcap and volume
    # but price and returns exists then (because returns have fillna = 0)
    # i am worried this is an error: did i do .shift() properly?
    # we set weights based on marketcap the day before.
    # HH can double check this. todo very important

    ## export oject

    if export_binarymatrix:
      return df_index, binary
    return df_index
