'''
make the same analysis as do1long.R byt in pandas.
then try to make ggindex() but in long format.

pandas tools:
* wide to long format (stack) and long to wide (unstack).
  - unstack moves a level of a MultiIndex (innermost by default) up to the columns.
  - stack is the inverse.
* pivot, melt. i think these can be done without groupby (not sure about what the diff is though).
* multiindex.

R and pandas conversion
http://pandas.pydata.org/pandas-docs/stable/comparison_with_r.html

aborted this idea 20181128 1524. i prefer wide. we can wait with fancy shiny apps. long format is needed for fancy shiny with ggindex, but for simple apps wide format is fine. it is also easier to reason analyticallya bout. i will do wide format in python with naming
'''

# see df
dfl_vcc.info()

# create dfl and clean it
cols_1 = ['symbol', 'date', 'close', 'volume', 'market']
dfl = dfl_vcc[cols_1].rename(columns={'close':'price', 'market':'mcap'})
dfl.date = pd.to_datetime(dfl.date)
#dfl = dfl.set_index(['date', 'symbol'])

# exampple of .query in pandas
dfl.query('mcap > 10000')
dfl.query('symbol=="XRP"')

# same query twice
dfl.query('symbol=="XRP" and '
          'date=="2018-04-10"')
dfl.query('symbol=="XRP" and date=="2018-04-10"')

# result1 = df[(df.A < Cmean) & (df.B < Cmean)]
# Cmean = 10.5
# result2 = df.query('A < @Cmean and B < @Cmean')

# create rank
dfl['rank_mcap'] = dfl.groupby('date')['mcap'].rank(ascending=False)

# create included
# version 1: a simple include based on market cap rank
# version 2: add forcelist and blacklist
# version 3: add "trooghet"
nr_top = 10
dfl['included'] = dfl['rank_mcap'] < nr_top + 1

# see which are included on a partuclar date
dfl.query('date == "2013-09-08" & included == True')

# volume and return has na in R but not in pandas
dfl.isnull().mean()

# see rank distribution for a particular asset
dfl.loc[dfl.symbol == 'LTC', 'rank_mcap'].value_counts(normalize=True)


## weight, if rebalanced daily

df %>%
  group_by(date) %>%
  mutate(included = rank < 11) %>%
  filter(rank < 11) %>%
  mutate(weight = mcap / sum(mcap)) %>%
  ungroup() %>%
  arrange(date) %>%
  filter(year == 2018, month == 4) %>%
  # see three "sections"
  print(n=3*10)

dfl.\
    query('included == True & date.dt.day == 1'). \
    groupby('date').\
    assign(w=dfl.mcap / sum(dfl.mcap))

dfl.\
    query('included == True & date.dt.day == 1'). \
    assign(w=dfl.mcap / dfl.groupby('date').mcap.sum())

def frac_of_tot(row, group_cols, frac_col):
    '''
    will be used with apply: df.apply(thisfunction, axis=1)
    input a , groupby cols
    :param row: a df
    :param col:
    :return: row / row.groupby(cols).sum()
    '''
    df_incl =
    # update df
    new_col_name = 'frac+ ' frac_col
    df.loc[df.included == True,
           new_col_name] = \
        df.loc[df.included == True].groupby(group_cols)[frac_col].sum()

def fracoftot(data):
    data_grouped = data.groupby('date', group_keys=False)
    fraction = data_grouped['mcap'] / data_grouped['mcap'].sum()
    return fraction

dfl.loc[dfl.included == True, 'mcap_frac'] = #...

mcaptot = dfl.loc[dfl.included == True].groupby('date')['mcap'].sum()

dfl.loc[dfl.included == True, 'mcap'] / mcaptot


dfl.loc[dfl.included == True] = dfl.query('included == True').\
    assign(weight = lambda x : x.groupby('date',group_keys=False).
           apply(lambda y: y.mcap / y.mcap.sum()))
dfl.query('included == True').\
    assign(weight = fracoftot(dfl))

fracoftot(dfl.loc[dfl.included == True])

## weight, if rebalanced monthly

df %>%
  filter(year > 2017) %>% # to see when many coins are in the set
  select(-price, -return) %>%
  mutate(inlcuded = as.integer(rank < 11)) %>%
  filter(day(date) == 1, rank < 11) %>%
  group_by(date) %>%
  mutate(weight = mcap / sum(mcap)) %>%
  ungroup() %>%
  arrange(date, rank) %>%
  print(n=30)

df %>%
  mutate(inlcuded = as.integer(rank_mcap < 11)) %>%
  filter(day(date) == 1, rank < 11) %>%
  group_by(date) %>%
  mutate(weight = mcap / sum(mcap)) %>%
  ungroup() %>%
  arrange(date, rank) %>%
  print(n=30)


## weight, if min and max weights are 30% and 1%

df %>%
  filter(year > 2017) %>% # to see when many coins are in the set
  select(-price, -return, -volume, -year,-month) %>% # easier viewing
  mutate(inlcuded = as.integer(rank < 11)) %>%
  filter(day(date) == 1, rank < 11) %>%
  group_by(date) %>%
  mutate(weight = mcap / sum(mcap)) %>%
  mutate(w_minmax = w_rescale_minmax(weight, 0.01, 0.30)) %>%
  ungroup() %>%
  arrange(date, rank) %>%
  print(n=30) %>%
  select(date, symbol, w_minmax)

## weight, smoothed



