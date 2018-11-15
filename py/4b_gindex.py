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

def gindex(marketcap_matrix, return_matrix, start, end, name, top, 
           rebalance_freq='M', random_rebalance=False,
           blacklist='', forcelist='',
           weighting='marketcap', smoothing=False):
  """
  input:
    df_mca, a market cap matrix. indexed with datedate.
    df_ret, a return matrix. indexed with datedate. todo add option to include price matrix instead. 
    Start date
    End date
    rebalnce frequency, choose any of these http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
    Name of index
    top, the nr of constituents
    Weighting equal or market cap
    Blacklist, coins that are forbidden 
    Forcelist, coins that must be included (even if they do not fulfil criteria of being in the top)
    Smoothing yes no
    Random rebalance yes no

  
  Output:
    a pandas series. 
    on that series we will do sharpe, inforatio, sortino ratio.
    
  todo:
  add option to include a subclass of forbidden coins, e.g. all stablecoins, all coins tracking other assets, etc. 
  """
  ## rename 
  mcap = marketcap_matrix
  return = return_matrix
           
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
  
  # todo more checks? 

  
  ## remove blacklisted coins  

  ## filter by date 
  
  ## resample to correct freq 

  mcap_mthly = mcap.resample(rebalance_freq, convention='start').asfreq()

 
  ## create binary market cap matrix
           
  ranked_mcap_mat_mthly = mcap_mthly.rank(axis=1, method='first', 
                                               ascending=False)
  # binary market cap. 1 for included, 0 for excluded. 
  binary_mcap_mthly = ranked_mcap_mat_mthly < 1 + nrcoins
  
  # on those dates where coins in includelist is not top n,
  # coins that are forced include will put away the smallest coins 
  # todo add this functionality later 
  
  ## go from market cap to weights 
  # steal code from 3 functions and 4 transform 
  
  ## calc return, from weights and return matrix 
  
  ## calc volume captured by index 
  
  ## calc market cap captured by index
  
  ## combine return, volume, market cap 
  
  ## export oject 
  
  
