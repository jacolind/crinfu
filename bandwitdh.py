# bandwidth rebalanced portfolio of two assets (e.g. 5% +- 2% BLX allocation).
###############################################################################

## define invest and rebalance functions 

def invest(df, i, amount, p, A, B, rm_shares=False):
    """
    Invest a USD amount in p% of asset A and 1-p% in asset B,
    starting at ordinal index i,
    where A and B are the names of the assets and these cols contain prices!
    This modifies df, by creating new cols: shares & value & ratio.
    col with shares can be removed. 
    """
    c = dict([(col, j) for j, col in enumerate(df.columns)])
    
    # prices are from the market, but the nr of shares to own we cancontrol
    
    # 1) reset nr shares of shares you own 
    # shares bought = amount invested / share price. 
    # we allow for fractions of shares. 
    amount_A = amount * p
    amount_B = amount * (1-p)
    A_shares = A + '_shares'
    B_shares = B + '_shares'
    df.iloc[i:, c[A_shares]] = amount_A / df.iloc[i, c[A]]
    df.iloc[i:, c[B_shares]] = amount_B / df.iloc[i, c[B]]
    
    # 2) based on shares owned being reset, calc what value those are by
    # value = share price * shares bought 
    A_value = A + '_value'
    B_value = B + '_value'
    df.iloc[i:, c[A_value]] = (df.iloc[i:, c[A]] * df.iloc[i:, c[A_shares]])
    df.iloc[i:, c[B_value]] = (df.iloc[i:, c[B]] * df.iloc[i:, c[B_shares]])
    
    # 3) set ratio of how much value we have in each asset 
    df.iloc[i:, c['ratio']] = (df.iloc[i:, c[A_value]] / 
                               df.iloc[i:, c[A_value]]+df.iloc[i:, c[B_value]])
                               
    # remove cols 
    if rm_shares:
        del df[A_shares]
        del df[B_shares]

def rebalance(df, tol, p, i=0, rm_shares=False, rm_cols=False):
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
        amount = (df.iloc[i, c[A_value]] + df.iloc[i, c[B_value]])
        # invest that amount (this begins investing process again e.g. rebalnce)
        invest(df, i, amount, p, rm_shares)
    # remove cols 
    if rm_cols:
      # recall A shares is taken care of otherwise 
      cols_created = ['ratio', A_value, B_value]
      df.drop(cols_created, inplace=True)
    return df

## create our bandwidth rebalanced portfolio 

# firstly, create TRD: a 60%/40% stocks/bonds portfolio. tolereance band 5%. 
invest(df, i=0, amount=100, p=0.60, A='Stocks', B='Bonds', rm_shares=True)
rebalance(df, tol=0.05, p=0.60, A='Stocks', B='Bonds', rm_shares=True)
# invest() create cols and rebalance() change their values by rebalancing.
# based on new columns that wes create, create portfolio value 
df['TRD'] = df['Stocks_value'] + df['Bonds_value']
# delete or rename ratio since it will be used later
del df['ratio'] 

# seconldy, create a 5%/95% portfolio of BLX/TRD 
invest(df, i=0, amount=100, p=w_target, A='BLX', B='TRD')
w_target = 0.05 
w_band = 0.02
rebalance(df, tol=w_band, p=w_target, A='BLX', B='TRD') 
# create portfolio value for portoflio A 'PFA': 5%/95%
df['PFA'] = df['BLX_value'] + df['TRD_value'] # must add _value
df['BLX_weight'] = df['BLX_value'] / df['PFA']
df['TRD_weight'] = df['TRD_value'] / df['PFA']
# delete cols we do not need 
df.drop(['BLX_shares', 'TRD_shares', 
         'BLX_value', 'TRD_value'], inplace=True)

## see the portfolio 

# plot investent over time 
df[['PFA', 'BLX', 'TRD']].plot()

# compare return 
price2return(df[['PFA', 'BLX', 'TRD']])

# see all weights over time 
print(df['BLX_weight'])

# see how often a sell is required 
print(df['ratio'] >= 1+w_band)
# see how often a buy is required 
print(df['ratio'] =< 1-w_band)

# show the rows which trigger rebalancing
mask_1 = (df['ratio'] >= w_target+w_band) | (df['ratio'] <= w_target-w_band)
print(df.loc[mask_1])

# see what the max and min weights are 
# they can be outside the range, but only for one time period. 
# if results are not satisfactory we must increase the rebalancing frequency or 
# decrease the tolerance band. 
print(df['BLX_weight'].min())
print(df['BLX_weight'].max())
print(df['TRD_weight'].min())
print(df['TRD_weight'].max())
