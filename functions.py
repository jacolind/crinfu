"""
define most of the functions.
"""

def top_binarizer(row, p):
    """
    Return 1 if a coin's mcap is within top p
    return 0 otherwise
    """
    # convert to pandas series. maybe not needed but safer
    row = pd.Series(row)
    # sort row
    row_sorted = row.sort_values(ascending=False)
    # find threshold value (e.g 11th value)
    threshold = row_sorted[p]
    # give a zero if a coin's mcap is less than threshold:
    binary = (row.values > threshold).astype('int')
    return binary
# todo later: create a warning if two have identical market cap because nlargest just takes on eof them
#threshold = row_sorted[p]
#binary = (row.values > threshold).astype('int')

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
    return aum

def price2aum(prices, fill_na=True, startvalue=100):
    """
    input prices (vector or matrix).
    output asset under management, starting at 100.
    """
    r = price2return(prices, fill_na_0=fill_na)
    r[0] = 0
    aum = startvalue * np.exp(r.cumsum())
    return aum

def sharpe(returnseries, freq='daily', riskfree=0, decimals=4):
    """
    input returns and T.
    output sharpe ratio.

    freq can be 'monthly' or 'daily'

    riskfree rate = 0
    which does not matter since we compare among cryptocurrencies
    and their rf is arguably the same -- although unknown.
    """
    if freq == 'monthly':
        mean = 12*np.mean(returnseries)
        vol = np.sqrt(12)*np.std(returnseries)
    if freq == 'daily':
        mean = 252*np.mean(returnseries)
        vol = np.sqrt(252)*np.std(returnseries)
    # calc sharpe
    sharpe = np.round((mean-riskfree)/vol, decimals)
    return sharpe

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

    return sns.heatmap(corr, mask=mask, annot=annot, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
