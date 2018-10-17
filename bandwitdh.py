# bandwidth rebalanced portfolio of two assets (e.g. 5% +- 2% BLX allocation).
###############################################################################

## define invest and rebalance functions 

def invest(df, i, amount, p):
    """
    Invest amount dollars between P% BLX and 1-P% TRD,
    starting at ordinal index i.
    This modifies df, by creating new cols: shares & value & ratio.
    """
    c = dict([(col, j) for j, col in enumerate(df.columns)])
    
    # prices are from the market, but the nr of shares to own we cancontrol
    
    # 1) reset nr shares of shares you own 
    # shares = value / share price. 
    # we allow for fractions of shares. 
    value_blx = amount * p
    value_trd = amount * (1-p)
    df.iloc[i:, c['BLX_shares']] = value_blx / df.iloc[i, c['BLX']]
    df.iloc[i:, c['TRD_shares']] = value_trd / df.iloc[i, c['TRD']]
    
    # 2) based on shares owned being reset, calc what value those are by
    # value = share price * shares 
    df.iloc[i:, c['BLX_value']] = (df.iloc[i:, c['BLX']] * 
                                   df.iloc[i:, c['BLX_shares']])
    df.iloc[i:, c['TRD_value']] = (df.iloc[i:, c['TRD']] * 
                                   df.iloc[i:, c['TRD_shares']])
    
    # 3) set ratio of how much value we have in each asset 
    df.iloc[i:, c['ratio']] = (df.iloc[i:, c['BLX_value']] / 
                               df.iloc[i:, c['TRD_value']]+df.iloc[i:, c['BLX_value']])

# todo: could make the function more general by accepting input
# A='BLX' B='TRD'. then we could reuse the invest() to create a 60/40 portoflio 
# based on only two column namely prices of stocks and bonds. 

def rebalance(df, tol, p, i=0):
    """
    Rebalance df whenever the ratio falls outside the tolerance range.
    This modifies df, by adjusting the cols shares & value, based on ratio.
    """
    c = dict([(col, j) for j, col in enumerate(df.columns)])
    while True:
        # 1) create a mask 
        
        # return true whenever ratio is outside of range 
        mask = (df['ratio'] >= w_target + w_band) | 
               (df['ratio'] <= w_target - w_band)
        # overwrite with false for prior locations (i.e. prior days)
        mask[:i] = False
        
        # 2) find the location i where mask is true.
        try:
            # Move i one index past the first index where mask is True
            # Note that this means the ratio at i will remain outside tol range
            i = np.where(mask)[0][0] + 1
        except IndexError:
            break
        
        # 3) at that location, re-invest (i.e. rebalance)
        
        # amount we have in our porftolio now 
        amount = (df.iloc[i, c['BLX_value']] + df.iloc[i, c['TRD_value']])
        # invest that amount (this begins investing process again e.g. rebalnce)
        invest(df, i, amount, p)
    return df

## create our bandwidth rebalanced portfolio 

# set ideal weight for BLX 
w_target = 0.05

# set how many percentage points BLX is allowed to be outside ideal weight
w_band = 0.02

# assuming df contains two cols df contain two cols: TRD and BLX with prices.
# below till return df with new columns. 
invest(df, i=0, amount=100, p=w_target) # create cols  
rebalance(df, tol=w_band, p=w_target) # change value of cols 

# based on new column, create portfolio value 
df['PORTF_value'] = df['BLX_value'] + df['TRD_value']
df['BLX_weight'] = df['BLX_value'] / df['PORTF_value']
df['TRD_weight'] = df['TRD_value'] / df['PORTF_value']

# show the rows which trigger rebalancing
mask = (df['ratio'] >= w_target+w_band) | (df['ratio'] <= w_target-w_band)
print(df.loc[mask])

# see what the max and min weights are 
# they can be outside the range, but only for one time period. 
# if results are not satisfactory we must increase the rebalancing frequency or 
# decrease the tolerance band. 
print(df['BLX_weight'].min())
print(df['BLX_weight'].max())
print(df['TRD_weight'].min())
print(df['TRD_weight'].max())

# see all weights 
print(df['BLX_weight'])

# see how often a sell is required 
print(df['ratio'] >= 1+w_band)
# see how often a buy is required 
print(df['ratio'] =< 1-w_band)
