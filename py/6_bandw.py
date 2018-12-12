"""
badnwidth portfolio

similar to bandw-2-stackoverfl-almostoriginal.py
"""

## define functions

def setup_df(df, A, B):
    """
    asset A and B are strings.
    """
    df = df[[A, B]]
    df = df.fillna(method='ffill') # maybe remove

    A_shares = A + '_shares'
    B_shares = B + '_shares'
    A_value = A +'_value'
    B_value = B +'_value'

    df[A_shares] = 0
    df[B_shares] = 0
    df[A_value] = 0
    df[B_value] = 0
    df['wA'] = 0

    return df

def invest(df, i, amount, perc, A, B):
    """
    Invest amount dollars evenly between Stocks and Gold
    starting at ordinal index i.
    This modifies df.
    """

    A_shares = A + '_shares'
    B_shares = B + '_shares'
    A_value = A +'_value'
    B_value = B +'_value'

    c = dict([(col, j) for j, col in enumerate(df.columns)])

    df.iloc[i:, c[A_shares]] = amount * perc / df.iloc[i, c[A]]
    df.iloc[i:, c[B_shares]] = amount * (1-perc) / df.iloc[i, c[B]]

    df.iloc[i:, c[A_value]] = (
        df.iloc[i:, c[A]] * df.iloc[i:, c[A_shares]])
    df.iloc[i:, c[B_value]] = (
        df.iloc[i:, c[B]] * df.iloc[i:, c[B_shares]])
    df.iloc[i:, c['wA']] = (
        df.iloc[i:, c[A_value]] / (df.iloc[i:, c[B_value]]+df.iloc[i:, c[A_value]])    )

def rebalance(df, tol, perc, A,B, i=0):
    """
    Rebalance df whenever the ratio falls outside the tolerance range.
    This modifies df.
    """

    c = dict([(col, j) for j, col in enumerate(df.columns)])
    A_value = A +'_value'
    B_value = B +'_value'


    while True:
        mask = (df['wA'] >= perc+tol) | (df['wA'] <= perc-tol)
        # ignore prior locations where the ratio falls outside tol range
        mask[:i] = False
        try:
            # Move i one index past the first index where mask is True
            # Note that this means the ratio at i will remain outside tol range
            i = np.where(mask)[0][0] + 1
        except IndexError:
            break
        # recalc the amount we own today.
        amount = (df.iloc[i, c[A_value]] + df.iloc[i, c[B_value]])
        # invest that amount
        invest(df, i, amount, perc, A,B)

    return df

def create_pf(df, A, B, pf):
    """
    input: A, B, pf are strings. pf is portfolio name.
    assumes df have cols from functions above (invest and rebalance)
    """
    df[pf] = df[A + '_value'] + df[B + '_value']
    df[pf] = price2aum(df[pf])
    return df

def rm_cols(df, A, B):
    A_shares = A + '_shares'
    B_shares = B + '_shares'
    A_value = A +'_value'
    B_value = B +'_value'
    cols_to_drop = [A_shares, B_shares, A_value, B_value]
    df = df.drop(cols_to_drop, axis=1)
    return df



## create legacy portfolio 60/40 stocks bonds.

# choose assets
A1 = 'Stocks'
B1 = 'Bonds'

# read and setup
pri_fin_mat_2 = pd.read_csv(file_pri_fin, index_col = 'Date', parse_dates=True)
pri_fin_mat_2 = re_index_date(pri_fin_mat_2)
df_trd = setup_df(pri_fin_mat_2, A=A1, B=B1)
del pri_fin_mat_2

# rebalance
perc1 = 0.60
tol1 = 0.05
invest(df_trd, i=0, amount=100, perc=perc1, A=A1, B=B1)
rebalance(df_trd, tol=tol1, perc=perc1, A=A1, B=B1)

# remove and create cols
pf1 = 'TRD'
df_trd = create_pf(df_trd, A1, B1, pf1)
# remove cols shares and value
df_trd = rm_cols(df_trd, A1, B1)


# plot weight
df_trd.wA.plot()
plt.ylabel('Weight in ' + A1)
plt.axhline(y=perc1 + tol1, color='black', linestyle='--')
plt.axhline(y=perc1 - tol1, color='black', linestyle='--')

# see max min  w
df_trd.wA.min(), df_trd.wA.max()

# plot performance
price2aum(df_trd[[A1, B1, pf1]]).plot()

# see
df_trd.head()

## create bandw portfolio 95/5 with LEG/BLX. name it BAL for balanced.

# choose assets
A2 = 'BLX'
B2 = 'TRD' # a 60/40 stocks/bonds

# read and setup
df_bal = pd.concat([df_trd['TRD'], pri_mat['BLX']], axis=1, join='inner')
df_bal = df_bal.reindex()
assert (df_bal.index == pri_mat.index).all()
df_bal = setup_df(df_bal, A2, B2)

# rebalance
perc2 = 0.05
tol2 = 0.02
invest(df_bal, i=0, amount=100, perc=perc2, A=A2, B=B2)
rebalance(df_bal, tol=tol2, perc=perc2, A=A2, B=B2)

# remove and create cols
#pf2 ='5/95 BLX/TRD'
pf2 = 'BAL'
df_bal = create_pf(df=df_bal, A=A2, B=B2, pf=pf2)
df_bal.head()

# remove cols shares and value
df_bal = rm_cols(df_bal, A=A2, B=B2)

# plot weight
df_bal.wA.plot()
ylabel2 = 'Weight in ' + A2 + '\n is ' + str(perc2) + ' +- ' + str(tol2)
plt.ylabel(ylabel2)
plt.axhline(y=perc2 + tol2, color='black', linestyle='--')
plt.axhline(y=perc2 - tol2, color='black', linestyle='--')
title2 = 'Bandwidth rebalanced portfolio \n with 5% BLX and 95% TRD'
plt.title(title2)
plt.savefig('output/df_bal.wA.png')

# plot performance
#price2aum(df_bal[[A2, B2, pf2]]).plot(logy=True)
price2aum(df_bal[[B2, pf2]]).plot()
title3 = 'TRD vs BAL: \n Traditional 60%/40% stocks/bonds portfolio (TRD) \n vs 5%/95% BLX/TRD bandwidth rebalanced (BAL)'
plt.title(title3)
plt.savefig('output/df_bal-aum.png')

## plot 1% and 5% allocation to blx.

## plot area weights  stocks/bonds/blx in the BALanced portf

# not same index => must join
df_bal.shape != df_trd.shape 
# concat, inner join 
df_bal_w = pd.concat([df_trd.wA, df_bal.wA], axis=1, join='inner')
df_bal_w.columns = ['w_stocks_in_trd', 'w_blx_in_bal']
assert (df_bal_w.w_blx_in_bal == df_bal.wA).all()
# weight on stock in balanced pf = weights in TRD * (1 - blx weight)
df_bal_w['w_stocks_in_bal'] = df_bal_w['w_stocks_in_trd'] * (1 - df_bal_w.w_blx_in_bal)
# weight in bond is the rest
df_bal_w['w_bonds_in_bal'] = 1 - df_bal_w.w_blx_in_bal - df_bal_w['w_stocks_in_bal']
df_bal_w.columns = ['removecol', 'BLX', 'Stocks', 'Bonds'] # tror det är ordningen
df_bal_w.drop('removecol', axis=1, inplace=True)
# plot
df_bal_w.plot.area(color=['#483d8b', '#ee82ee', '#a020f0'], alpha=0.8)
title4 = 'BAL portfolio: \n 5% to BLX and 95% to 60/40 stocks/bonds'
title5 = 'BAL portfolio: 5% in BLX and 95% in TRD'
plt.title(title5)
plt.ylabel('Allocation in BAL portfolio')
plt.legend(loc=(1.04,0))
plt.savefig('output/df_bal_w.png')

"""
todo maybe call it TRD for traditional not LEG for legacy. then we can say traditional 60/40
todo fix index as datetime! either via new = df.resample('T', how='mean') or via re_index_date
"""
