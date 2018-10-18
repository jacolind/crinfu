df = pri_fin_mat[['Stocks', 'Bonds']]
df['sh Stocks'] = 0
df['sh Bonds'] = 0
df['Stocks value'] = 0
df['Bonds value'] = 0
df['ratio'] = 0

def invest(df, p, i=0, amount=100):
    """
    Invest amount dollars evenly between Stocks and Bonds
    starting at ordinal index i.
    This modifies df.
    """
    c = dict([(col, j) for j, col in enumerate(df.columns)])
    halfvalue = amount/2
    df.iloc[i:, c['sh Stocks']] = amount*p / df.iloc[i, c['Stocks']]
    df.iloc[i:, c['sh Bonds']] = amount*(1-p) / df.iloc[i, c['Bonds']]

    df.iloc[i:, c['Stocks value']] = (
        df.iloc[i:, c['Stocks']] * df.iloc[i:, c['sh Stocks']])
    df.iloc[i:, c['Bonds value']] = (
        df.iloc[i:, c['Bonds']] * df.iloc[i:, c['sh Bonds']])
    df.iloc[i:, c['ratio']] = (
        df.iloc[i:, c['Stocks value']] / df.iloc[i:, c['Bonds value']])
    ideal_ratio = p / (1-p)
    df.iloc[i:, c['ratio']] = df.iloc[i:, c['ratio']] / ideal_ratio
    return df

def rebalance(df, tol, p, i=0):
    """
    Rebalance df whenever the ratio falls outside the tolerance range.
    This modifies df.
    """
    c = dict([(col, j) for j, col in enumerate(df.columns)])
    while True:
        mask = (df['ratio'] >= 1+tol) | (df['ratio'] <= 1-tol)
        # ignore prior locations where the ratio falls outside tol range
        mask[:i] = False
        try:
            # Move i one index past the first index where mask is True
            # Note that this means the ratio at i will remain outside tol range
            i = np.where(mask)[0][0] + 1
        except IndexError:
            break
        amount = (df.iloc[i, c['Stocks value']] + df.iloc[i, c['Bonds value']])
        invest(df, i, amount, p)
    return df

tol = 0.05
p_ = 0.60
dfi = invest(df, i=0, amount=100, p=p_)
dfr = rebalance(dfi, tol, p=p_)
dfi.head()
dfr.head()
dfi.tail()
dfr.tail()

df['portfolio value'] = df['Stocks value'] + df['Bonds value']
df['Stocks weight'] = df['Stocks value'] / df['portfolio value']
df['Bonds weight'] = df['Bonds value'] / df['portfolio value']

print(df['Stocks weight'].min())
df['Stocks weight'].max()
df['Bonds weight'].min()
df['Bonds weight'].max()

# This shows the rows which trigger rebalancing
mask = (df['ratio'] >= 1+tol) | (df['ratio'] <= 1-tol)
print(df.loc[mask])