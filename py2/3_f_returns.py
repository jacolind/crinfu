"""
define most of the functions:
price 2 return
return 2 aum
corrplot
and others.
"""

## files and folders

def text_export(object, file, description='', folder='output/'):
  filepath = folder + file + '.txt'
  with open(filepath, "w") as text_file:
    text_file.write(description + "\n \n" + str(object))


## modify price and returns  for df

def price2return(prices, fill_na_0=True):
  """
  input prices (vector or matrix).
  output returns.
  """
  # definition of return
  r = prices / prices.shift(1) - 1
  #r = np.log(prices) - np.log(prices.shift(1))
  # first day is NA due to .shift
  if fill_na_0 == True:
    r = r.fillna(0)
  # replace inf with 0 <=> buying after 1 day of existence
  r = r.replace([np.inf, -np.inf], 0)
  return r

def return2aum(returns, startvalue=100):
  """
  input returns (vector or matrix).
  output asset under management, starting at 100.
  """
  # replace info with zero
  r = returns.replace([np.inf, -np.inf], 0)
  # replace na with zero
  r = r.fillna(0)
  # make aum begin at startvalue
  r[0] = 0
  # formula: indexed price serie = exp(cumsum(return_series))
  aum = startvalue * np.exp(r.cumsum())
  if isinstance(aum, pd.DataFrame):
    aum = aum.drop(0, axis=1)
  return aum

def price2aum(prices, fill_na=True, startvalue=100):
  """
  input prices (vector or matrix).
  output asset under management, starting at 100.
  """
  r = price2return(prices, fill_na_0=fill_na)
  #r[0] = 0
  aum = startvalue * np.exp(r.cumsum())
  if isinstance(aum, pd.DataFrame):
    aum = aum.drop(0, axis=1)
  return aum

## risk/return measures

def sharpe(returns_mat, freq='daily', showall=False,
           riskfree=0, decimals=4):
  """
  input returns and T.
  output sharpe ratio.

  freq can be 'monthly' or 'daily'. assume 365 trading days in a year not 252. it can also be a number (see code).

  riskfree rate = 0
  which does not matter since we compare among cryptocurrencies
  and their rf is arguably the same -- although unknown.
  """
  # calc T
  if freq == 'monthly':
    T = 12
  if freq == 'daily':
    T = 365
  if isinstance(freq, int):
    T = freq
  # rf
  if riskfree == 'BTC':
    riskfree = returns_mat['BTC'] # can be generalized to any asset with this: if isinstance(object, str) then riskfree = retmat[object]
  # calc mean vol sharpe
  mean = T*np.mean(returns_mat)
  vol = np.sqrt(T)*np.std(returns_mat)
  shrp = np.round((mean-riskfree)/vol, decimals)
  # output
  output = shrp
  if showall:
    output = pd.concat([mean, vol, shrp], axis=1)
    output.columns = ['Return', 'Volatility', 'Sharpe']
  return output.round(decimals)

# and old function. need not be used.
# def returns_vol_tbl(df, assets, start, end='2018-04', T=365):
#   """start with rr since it contains fund and coins returns.
#   T=12 for monthly data and T=365 for daily data.
#   output returnstable for a certain period.
#   """
#   # calc mean and vol
#   ret = df.loc[start:end, assets].mean() * T
#   vol = df.loc[start:end, assets].std() * np.sqrt(T)
#   # put into tbl
#   tbl = pd.concat([ret, vol], axis=1)
#   # rename
#   tbl.columns = ['Return', 'Volatility']
#   tbl['Return / Vol'] = tbl['Return'] / tbl['Volatility']
#   return tbl.round(2).T

def retvol(retmat):
  ret = retmat.mean() * 365
  vol = retmat.std() * np.sqrt(365)
  df_ret_vol = pd.concat([ret, vol], axis=1)
  df_ret_vol.columns = ['Return', 'Volatility']
  return df_ret_vol


def returns_interval(returns_matrix, assets='', T=365):
  """start with rr since it contains fund and coins returns.
  T=12 for monthly data and T=365 for daily data.
  output returnstable for a certain period.
  """
  # default choice
  if assets=='':
    assets = returns_matrix.columns
  # calc mean and vol
  ret = returns_matrix.mean() * T
  vol = returns_matrix.std() * np.sqrt(T)
  # put into tbl
  tbl = pd.concat([ret - 2*vol,
                   ret,
                   ret + 2*vol],
                  axis=1)
  # rename
  tbl.columns = ['Mean-2*vol', 'Mean', 'Mean+2*vol']
  return tbl.round(4)

def sortino_vec(ret_vec, target=0, T=365):
   '''
   input pandas series and target annual return. output its sortino ratio.
   https://en.wikipedia.org/wiki/Sortino_ratio
   '''

   mean = ret_vec.mean() * T - target
   vol = ret_vec[ret_vec < target].std() * np.sqrt(T)
   sortino_ratio = mean / vol
   return sortino_ratio

def sortino(ret_mat, target=0, T=365):
  # do this f() so the usage is congruent with sharpe()
  return ret_mat.apply(sortino_vec, target=target, T=T)


def information_ratio(returns_mat, benchmark,
                      freq='daily', showall=False,
                      riskfree=0, decimals=4):
  '''
  https://en.wikipedia.org/wiki/Information_ratio

  information ratio is like sharpe ratio but data is not returns but instead returns minus benchmark returns. we use BTC as the default benchmark.

  It is <=> to active return divided by tracking error.
  '''
  returns_bench_vec = returns_mat[benchmark]
  returns_minus_bench = returns_mat.subtract(returns_bench_vec, axis=0)
  out = sharpe(returns_minus_bench,
               freq=freq, showall=showall,
               # must use rf = 0 to get info ratio correct
               riskfree=0,
               decimals=decimals)
  if showall:
    out.columns = ['Return', 'Volatility', 'Info_ratio']
  else:
    out.name = 'Info_ratio'
  # benchmark asset get NaN for info ratio but in fact it is zero
  out = out.fillna(0)
  return out

def tracking_error(returns_mat, benchmark,
                   freq='daily', decimals=4):
  '''
  https://en.wikipedia.org/wiki/Tracking_error
  '''
  if freq == 'daily':
    T=365
  if freq == 'monthly':
    T=12
  active_return = returns_mat.subtract(returns_mat[benchmark], axis=0)
  trackingerror = active_return.std() * np.sqrt(T)
  trackingerror = trackingerror.round(decimals)
  trackingerror.name = 'Tracking_error'
  return trackingerror

def value_at_risk(returns_matrix, alpha=0.95):
  returns_matrix = returns_matrix.fillna(0)
  ret_nonzero = returns_matrix
  #ret_nonzero = returns_matrix[returns_matrix != 0]
  var = ret_nonzero.quantile(1-alpha)
  var.name = 'VaR ' + str(alpha)
  return var

price2return(pri_vcc_mat.iloc[0:900, 0:10]).quantile(0.95)
retex1 = price2return(pri_vcc_mat.iloc[0:900, 0:10])
retex1.quantile(0.05)
value_at_risk(retex1, alpha=0.95)

# beta function taken from
# https://stackoverflow.com/questions/39501277/efficient-python-pandas-stock-beta-calculation-on-many-dataframes
def beta(df):
  # first column is the market
  X = df.values[:, [0]]
  # prepend a column of ones for the intercept
  X = np.concatenate([np.ones_like(X), X], axis=1)
  # matrix algebra
  b = np.linalg.pinv(X.T.dot(X)).dot(X.T).dot(df.values[:, 1:])
  return pd.Series(b[1], df.columns[1:], name='Beta')



# sketch as of now
def drawdown(price_mat, window):
  pri_mat_roll = price_mat.rolling(price_mat)
  pridiff_mat_roll = pri_mat_roll.first() - pri_mat_roll.roll.last()
  return pridiff_mat_roll


## correlation plots

def corrplot(corr, annot=False):
  """
  input: corr matrix.
  output: good looking corr plot.
  usage example: corrplot(df.corr())
  """
  # Generate a mask for the upper triangle
  mask = np.zeros_like(corr, dtype=np.bool)
  mask[np.triu_indices_from(mask)] = True

  # Set up the matplotlib figure
  f, ax = plt.subplots(figsize=(11, 9))

  # Generate a custom diverging colormap
  cmap = sns.diverging_palette(220, 10, as_cmap=True)

  # Draw the heatmap with the mask and correct aspect ratio

  heatmap = sns.heatmap(corr,
                     mask=mask, annot=annot, cmap=cmap,
                     vmax=.3, center=0, square=True,
                     linewidths=.5, cbar_kws={"shrink": .5})
  return heatmap


# define help-function
txt_daterange = START1 + ' to ' + END1
title_corr = 'Correlation matrix - daily data \n from ' + txt_daterange

def show_corr_plot(df,
                   start='', end='',
                   cols='', title=''):
    """
    input a return matrix df (eg monthly or daily returns)
    slice the df by startdate, enddate and columns.
    output a correlation matrix plot.
    """
    # set dates
    if start=='':
      start = df.index[0]
    if end=='':
      end = df.index[-1]
    # default cols
    if cols=='':
      cols = df.columns
    if title=='':
      'Correlation matrix on daily data'
    # plot
    corr_mat = df.loc[start:end, cols].corr()
    corrplot(corr_mat)
    plt.title(title)
    plt.show()

def show_rollcorr_plot(cor_mat, cols, legend=False, title=''):
    cor_mat[cols].plot(legend=legend)
    plt.ylabel('Correlation vs BTC')
    plt.title(title)
    plt.axhline(y=0, color='k', ls='-')
    plt.show()