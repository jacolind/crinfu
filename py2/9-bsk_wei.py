'''
this script analyze weight differences with different index constructions.
results are saved to /output/ and /output/vip/
'''




## effect of caps and floors

# plot 1
r8.name, r1.name
wd = w8m.subtract(w1m, axis=0)
#with plt.style.context(('seaborn-pastel')):
wd[wd>0].loc['2017':, tkr_t10now].plot.area(stacked=True, alpha=0.5)
title1 = 'Effect of caps and floors: \n Floor 2% cap 50% vs regular top 10 basket'
ytext1 = 'Weight difference: \n floored & capped minus regular'
plt.title(title1)
plt.ylabel(ytext1)
plt.savefig('output/bsk/wei/capsfloors_effect_1_alts.png')

# plot 2
wd.loc['2017':, 'BTC'].plot(color='orange')
plt.title(title1)
plt.ylabel('Weight difference for BTC')
plt.savefig('output/bsk/wei/capsfloors_effect_1_BTC.png')

# mean
wd_mean = wd.mean(axis=0).round(3)
wd_mean['BTC']
wd_mean[wd_mean!=0].sort_values()
wd_mean.nlargest(10).to_csv('output/bsk/wei/wd_mean.txt')

## effect of smoothing

# time series plot
r1.name, r2.name
w2m = w3.resample('MS').first()
w_diff = w1m - w2m
w_diff = w_diff.resample('MS').first()
w_diff_m = w_diff.mean()
w_diff_m[w_diff_m > 0.02]
w_diff_m[w_diff_m < -0.02]
w_diff_m[w_diff_m < -0.02].to_csv('output/bsk/wei/smoothing_1.csv')

# aggregated plot
# recall when interpeting this plot, that BTC w is 50%
# so it should be largest, since we measre absolute value of % diff
# we could normalize by each asset's (average) weight in the basket, to see which coins are "relatively" most effected
w_diff_1 = w_diff.abs().mean()
w_diff_1 = w_diff_1.nlargest(20)
w_diff_1.plot.barh()
plt.title('Effect of smoothing')
plt.ylabel('Ticker')
plt.xlabel('Mean of abs(Smoothed weight minus raw weight)')
plt.savefig('output/bsk/wei/smoothing_w1.png')
w_diff_1.to_csv('output/bsk/wei/w smooth minus w raw, abs(mean()).csv')

## nrtop = 5 vs 10

# weights in fifth vs tenth asset. it has implication on turnover.
r1.name, r4.name

def find_nth(row, n):
  # remove zero and na
  row = row.fillna(0)
  row_pos = row[row != 0]
  row_nth = row.nlargest(n).nsmallest(1)
  # return value, not index
  return row_nth.values[0]

find_nth(w4.iloc[300,:], n=5)

w4_fifth = w4.apply(find_nth, n=5)
w1_tenth = w1.apply(find_nth, n=10)
# todo this saves the index and i do not want that

## turnover

# see turnover depending on portf.
w1.shape

## trading volume nr 5 vs 10

# Kolla nr 5 vs nr 10 I volym i usd, jfr dom.
# to see if it is easier to trade

#
r1.name

# create
w1rank = w1.fillna(0).rank(axis=1, method='max', ascending=False)
rank5 = (w1rank == 5)
rank10 = (w1rank == 10)
assert (rank5.sum(axis=1) == 1).all()
vol5 = (vol_vcc_mat * rank5).sum(axis=1)
vol10 = (vol_vcc_mat * rank10).sum(axis=1)
vol_5vs10_mat = pd.concat([vol5, vol10, vol10-vol5], axis=1)
vol_5vs10_mat.columns = ['Fifth', 'Tenth', 'Diff']
# mean
vol_5vs10_mat.mean(axis=0)
# plot 1
vol_5vs10_mat.drop('Diff',axis=1).rolling(30).mean().plot()
plt.ylabel('Trading volume in USD \n Rolling 30 days mean')
plt.title('Trading volume per asset')
plt.savefig('output/bsk/wei/volume_5vs10_1.png')

## back of the envelope re 10 vs 5 trading volume

# aum estimate from other firms
fund_aum = 200e6

# assume
w_10th = 0.015
w_5th = 0.030
# estimates taken from the lates weights
w1.iloc[-1].sort_values(ascending=False)[5-1]
w1.iloc[-1].sort_values(ascending=False)[10-1]

# take these nr from the graph
vol_5th = 4e8
vol_10th = 1e8

# if an asset exits. what is the effect on us moving the price?
print("fund aum times weight in asset, divided by market trading volume:")
print(fund_aum*w_5th / vol_5th)
print(fund_aum*w_10th / vol_10th)

# now the question is how much volume is needed to affect the price? probably not when it is only 1%

## pf turnover

see_example = False
if see_example:
  # resample to month start
  # todo diff between .firt() and .freq() ?
  w1_mthly = w1.resample('MS').first()
  pri_vcc_mat_mthly = pri_vcc_mat.resample('MS').first()
  ret_vcc_mat_mthly = pri_vcc_mat_mthly.div(pri_vcc_mat_mthly.shift(1))-1
  (w1_mthly.index == ret_vcc_mat_mthly.index).all()
  # the "correct" weights are these
  w1_mthly
  # a (too) simplistic way to calc the trade needed between rebelance date is +after-before
  w1_totrade_simple = w1_mthly - w1_mthly.shift(-1)
  w1_totrade_simple[tkr_t10now].tail().round(2)
  # it is overly simplistic because we have gotten a return during the month! the simplicity will lead to an overstatement of the rebalancing needed. in reality we do not need to trade this much.
  # weights before rebalncing is the weights in jan grown with a return
  # that return is the price move jan to feb <=> ret in feb
  w1_grown = w1_mthly.shift(1) * (1+ret_vcc_mat_mthly)
  w1_before_rebalance = w1_grown.div(w1_grown.sum(axis=1), axis=0)
  # the "correct" weights minus weights before rebalancing, is what must be traded
  w1_totrade_at_rebalance = w1_mthly - w1_before_rebalance
  w1_totrade_at_rebalance[tkr_t10now].tail().round(2)
  w1_mthly.loc['2018-01':, tkr_t10now]
  ret_vcc_mat_mthly.loc['2018-01':, tkr_t10now]

def rebalance_trade(wei_mat,
                 rebalance_freq='MS',
                 price_matrix=pri_vcc_mat):
  '''
  input dialy weights matrix. output monthly matrix of weights  to trade at rebelance date.
  :param wei_mat: daily
  :param price_matrix: daily
  :return:  monthly freq
  '''
  # rename
  w = wei_mat
  p = price_matrix
  # resample to month start
  # todo diff between .firt() and .freq() ?
  w_mthly = w.resample(rebalance_freq).first()
  p_mthly = price_matrix.resample(rebalance_freq).first()
  ret_mthly = p_mthly.div(p_mthly.shift(1)) - 1
  #(w_mthly.index == ret_mthly.index).all()
  # the "correct" weights are these
  w_mthly
  # weights before rebalncing is the weights in jan grown with a return
  # that return is the price move jan to feb <=> ret in feb
  w_grown= w_mthly.shift(1) * (1 + ret_mthly)
  # normalize
  w_before_rebalance = w_grown.div(w_grown.sum(axis=1), axis=0)
  # the correct weights minus weights before rebalancing, is what must be traded
  w_totrade_at_rebalance = w_mthly - w_before_rebalance
  return w_totrade_at_rebalance


def turnover(wei_trade_mat, what='min'):
  '''
  input matrix of weights to be traded, see rebalance_trade(). 
  output a pd series of the portfolio turnover.
  :param wei_mat:
  :param ret_mat: returns matrix. assumed freq is daily
  :param what: to be preciese, turnover is defined as the minumum of min(pos, neg) but its numercailly almost the same as 'pos' and pos has a much easier explanation.
  :return:
  '''
  wei_trade_mat = wei_trade_mat.fillna(0)
  sum_positive = wei_trade_mat[wei_trade_mat>0].sum(axis=1)
  sum_negative = -wei_trade_mat[wei_trade_mat<0].sum(axis=1)
  turnover = pd.concat([sum_positive, sum_negative], axis=1)
  turnover.columns = ['pos', 'neg']
  turnover['min'] = turnover.min(axis=1)
  return(turnover[what])

# see turnover for a basket
wt1m = rebalance_trade(w1m)
wt1m.loc['2018':, tkr_t10now].round(2)
turno1 = turnover(wt1m)
turno1.mean()
turno1.name = r1.name

# plot 1
turno1.plot(style='.')
plt.title('Turnover ' + r1.name)
ylabel1 = 'Turnover: trading needed to rebalance'
plt.ylabel(ylabel1)
plt.savefig('output/bsk/wei/turnover_1.png')

# plot 2
turno4 = turnover(rebalance_trade(w4))
turno4.name = r4.name
turno1vs4 = turno1 - turno4
r1.name, r4.name
turno1vs4.name = 't10 minus t5'
turno1vs4.plot(style='o')#, color='blue')
plt.legend(loc='upper left')
plt.title('Turnover comparison')
plt.ylabel(ylabel1)
plt.axhline(y=turno1vs4.mean(), color='grey', alpha=0.5)
plt.savefig('output/bsk/wei/turnover_2.png')

## coin switsches


"""
definition: A coin shift has occured in month t+1 if
the set of selected coins for month t is not the same as month t+1.

This is calculated by comparing the B matrix with the lagged B matrix.
The more coinswitches the harder it would be to do it yourself.
Main goal is to see how it impacts our trading.
"""

def coinswitch(weights_mat, rebalance_freq='MS'):
  '''
  input daily weights matrix.
  output monthly vector of the nr of coin switches.
  '''
  # monthly
  weights_mat_mthly = weights_mat.resample(rebalance_freq).first()
  bin_mat_mthly = (weights_mat_mthly> 0)
  # create vector measing nr of in/out events
  b_vs_bshift_mat = (bin_mat_mthly.shift(1) != bin_mat_mthly)
  coinswitch_vec = b_vs_bshift_mat.sum(axis=1)
  # delete first row
  coinswitch_vec = coinswitch_vec[1:]
  # Coin A in and coin B out is 1 switch not 2.
  coinswitch_vec = coinswitch_vec / 2
  # name
  coinswitch_vec.name = 'switches'
  return coinswitch_vec


def plot_coinswitch(coinswitch_vec, rname='', filename=''):
  #coinswitch_vec = coinswitch(weight_matrix, rebalance_freq='MS')
  coinswitch_vec.plot(style='.')
  plt.title('Number of coins entering basket \n' + rname)
  plt.ylabel('Number of coins')
  plt.yticks(np.arange(coinswitch_vec.min().min() - 1,
                       coinswitch_vec.max().max() + 2))
  #plt.ylim([-1, coinswitch_vec.max()+1])
  
  if filename != '':
    plt.savefig('output/bsk/wei/coinswitches' + filename + '.png')

# plot a few baskets coin switches
plot_coinswitch(coinswitch_vec=coinswitch(w1m), rname=r1.name, filename='1')
plot_coinswitch(coinswitch_vec=coinswitch(w4m), rname=r4.name, filename='4')
plot_coinswitch(coinswitch_vec=coinswitch(w8m), rname=r8.name, filename='8')

# nr of coin switches
coinswitch(w1).value_counts(normalize=True).sort_index().round(2)\
  .to_csv('output/bsk/wei/coinswitches_bsk1.txt')

# compare basket's coin switches 
csw_1minus4 = coinswitch(w1) - coinswitch(w4)
csw_1vs4 = pd.concat([coinswitch(w1), coinswitch(w4)], axis=1)
csw_1vs4.columns = [r1.name, r4.name]

# plot
plot_coinswitch(csw_1minus4, rname=r1.name + ' minus ' + r4.name,
                filename='1minus4')

# plot
csw_1minus4.value_counts(normalize=True).sort_index().round(2)\
  .to_csv('output/bsk/wei/coinswitches_bsk1_minus_bsk4.txt')

# plot
csw_1vs4.plot(style=['o', 'x'])
(csw_1minus4 == 0).any()
plt.yticks(np.arange(-1, 4))

## export members and wei for SL

# to compare 5 vs 10 in if cold storage solutions exists for them
# to answer questions re technical issues with assets e.g. wallet changes

def members(wei_mat):
  member = wei_mat.fillna(0).sum() > 0
  member = member[member].index
  return member
members(w1)
mem = w1.fillna(0).sum() > 0

def members2csv(wei_mat, name):
  member = members(wei_mat)
  avgwei_by_member = wei_mat[member].sum().\
    round(4).sort_values(ascending=False)
  #avgwei_by_member = avgwei_by_member[avgwei_by_member>0]
  avgwei_by_member.name = 'sum_weight'
  file = 'output/bsk/wei/' + 'member_sum_wei_' + name + '.txt'
  avgwei_by_member.to_csv(file)

# nr of months
w1.shape[0]/30

# export
members2csv(w1, r1.name)
members2csv(w4, r4.name)

def members2txt(wei_mat, name):
  tkrlist = members(wei_mat)
  tkrlist = str(tkrlist)
  file = 'output/bsk/wei/' + 'member_' + name + '.txt'
  with open(file, "w") as text_file:
    text_file.write(tkrlist)

def export_wei(wei, name):
  w_mthly = wei.resample('MS').first()
  w_mthly = w_mthly.fillna(0).round(3)
  tkr_member = members(w_mthly)
  filename = 'output/bsk/wei/wei_mthly_'  + name + '.csv'
  w_mthly[tkr_member].to_csv(filename)

# export
export_wei(w1m, name=r1.name)
export_wei(w4m, name=r4.name)

## plot members and wei

# weight mat area plot for a few baskets. then put them side byside in latex to compare how much w is held in each.

# choose
tkr_sel_2 = ['BTC', 'ETH', 'XRP']

# plot 1
w1m[tkr_sel_2].plot.area(alpha=0.5)
plt.ylabel('Weight')
plt.title('Weight per asset \n basket ' + r1.name)
plt.savefig('output/bsk/wei/w1_area.png')

# plot 4
w4m[tkr_sel_2].plot.area(alpha=0.5)
plt.ylabel('Weight')
plt.title('Weight per asset \n basket ' + r4.name)
plt.savefig('output/bsk/wei/w4_area.png')

# plot 1 vs 4
w4_minusw_1m = w4m - w1m
w4_minusw_1m[tkr_sel_2].plot()
plt.title('Weight in ' + r4.name + ' minus ' + r1.name)
plt.ylabel('Weight difference')
plt.savefig('output/bsk/wei/w4-w1_area.png')

# plot w per asset w/o btc for basket 1 and 4
tkr_t10_top7 = w1m.mean().nlargest(8)
tkr_t5_top7 = w4m.mean().nlargest(8)
# make sure colors are the same in both
tkr_top7_common = pd.concat([tkr_t10_top7, tkr_t5_top7], 1)
tkr_top7_common = tkr_top7_common.sort_values(0, ascending=False)
tkr_top7_common = tkr_top7_common.index

title1 = 'Weight per asset \n'
w1m[tkr_top7_common].drop('BTC', axis=1).plot.area(alpha=0.5)
plt.title(title1 + r1.name)
plt.ylabel('Weight')
plt.savefig('output/bsk/wei/w1_alts.png')

w4m[tkr_top7_common].drop('BTC', axis=1).plot.area(alpha=0.5)
plt.title(title1 + r4.name)
plt.ylabel('Weight')
plt.savefig('output/bsk/wei/w4_alts.png')

w4_minusw_1m[tkr_top7_common].drop('BTC', axis=1).plot(style='.')
plt.savefig('output/bsk/wei/w4-1m_alts.png')
w4_minusw_1m[tkr_top7_common].mean().to_csv('output/bsk/wei/w4_minusw_1m_mean.csv')

## which asset entered and left

# create help objects
b1m = (w1m>0)
bd1 = b1m != b1m.shift(1)
wd1 = w1m - w1m.shift(1)
tkr_gone_in_or_out = bd1.columns[bd1.sum() > 1]
tkr_gone_in_or_out
bd1.sum(1).value_counts().to_csv('output/bsk/wei/nrof_coinsw_w1.csv')
w_times_b = bd1[tkr_gone_in_or_out] * w1m[tkr_gone_in_or_out]

# plot 1
w_times_b.sum(1) # is like turnover
tkr_insouts_mostwei = w_times_b.abs().sum().nlargest(7)
tkr_insouts_mostwei.to_csv('output/bsk/wei/tkr_insouts_mostwei_sum.csv')
wd1[tkr_insouts_mostwei.index].plot(style='.')
plt.ylabel('Trading needed: \n Weight diff current month vs previous')
plt.title('Trading needed per asset \n in assets that most often go in/out of basket')
plt.savefig('output/bsk/wei/wd1_tkr_insouts_mostwei.png')

# create objects of interest
run_txt_files = False # get some error now out of bound. todo fix it, worked before. but the output is already saved so not very important.
if run_txt_files:
  tkr_bin_insouts = []
  tkr_entered = []
  tkr_left = []
  for k in range(0, bd1.shape[0]):
    row = bd1.iloc[k, tkr_gone_in_or_out]
    row = row.fillna(0)
    row_nz = row[row != 0]
    tkr_bin_insouts.append(row[row != 0])

    wrow = wd1.iloc[k, tkr_gone_in_or_out]
    wrow = wrow.fillna(0)
    wrow = wrow * row
    tkr_entered.append(wrow[wrow > 0])
    tkr_left.append(wrow[wrow < 0])
  # see lists
  tkr_bin_insouts
  tkr_entered
  tkr_left

  # export to text files
  text_export(tkr_bin_insouts,
              'coinswitch_w1_which',
              'what assets are involved in the coinswitch')
  text_export(tkr_entered,
              'coinswitch_w1_entered',
              'assets entering the basket and their weight increase')
  text_export(tkr_left,
              'coinswitch_w1_left',
              'assets leaving the basket and their weight decrease')

## coverage

# how much of the total marketcap is covered by top10 and top5?
mca_mat_1 = pd.concat([m0, m1, m4], axis=1)
mca_mat_1.plot()
mca_mat_2 = mca_mat_1.div(mca_mat_1.market, axis=0)
mca_mat_2 = mca_mat_2.drop('market', axis=1)
# plot
mca_mat_2.rolling(20).mean().plot()
plt.title('Fraction of total market capitalization')
plt.ylabel('Basket market cap divided by total market cap')
plt.savefig('output/bsk/wei/mcafr_bsk1bsk4_smooth20.png')

##

