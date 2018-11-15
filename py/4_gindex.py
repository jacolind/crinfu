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

def gindex(df_mca, df_ret, start, end, name, top, 
           blacklist='', forcelist='',
           weighting='marketcap', smoothing=False, random_rebalance=False):
  """
  input:
    df_mca, a market cap matrix. indexed with datedate.
    df_ret, a return matrix. indexed with datedate. todo add option to include price matrix instead. 
    Start date
    End date
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
  
  ## force includelist coins 
  
  ## filter by date 
  
  ## select top n 
  
  ## go from market cap to weights 
  # steal code from 3 functions and 4 transform 
  
  ## calc return, from weights and return matrix 
  
  ## calc volume captured by index 
  
  ## calc market cap captured by index
  
  ## combine return, volume, market cap 
  
  ## export oject 
  
  
