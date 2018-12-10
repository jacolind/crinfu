'''
this script defines two functions, and illustrates how it is used
'''

## define function


def rescale_w(row_input, weight_min, weight_max):
  '''
  :param row_input: a row from a pandas df
  :param weight_min: the floor. type float.
  :param weight_max: the cap. type float.
  :return: a pandas row where weights are adjusted to specify min max.

  step 1:
  while any asset has weight above weight_max,
  set that asset's weight to == weight_max
  and distribute the leftovers to all other assets (whose weight are >0)
  in accordance with their weight.

  step 2:
  if there is a positive weight below min_weight,
  force it to == min_weight
  by stealing from every other asset
  (except those whose weight == max_weight).

  note that the function produce strange output with few assets.
  for example with 3 assets and max 30% the sum is 0.90
  and if A=50% B=20% and one other asset is 1% then
  these are not practical problems as we will analyze on data with many assets.
  '''

  # rename
  w1 = row_input

  # na
  # script returned many errors regarding na
  # so i a fillna(0) here.
  # if that will be the final solution, some cleaning up can be done
  # eg remove _null objects and remove some assertions.
  w1 = w1.fillna(0)

  # proof that index is already sorted.
  assert (w1.sort_index().index == w1.index).all()
  assert (w1.sort_index().values == w1.values).all()

  # remove zeroes to get a faster script
  w1nz = w1[w1 > 0]
  w1z = w1[w1 == 0]
  assert len(w1) == len(w1nz) + len(w1z)
  assert set(w1nz.index).intersection(set(w1z.index)) == set()

  # input must sum to 1 or zero
  sum_w_zero = w1.sum() == 0
  sum_w_one = abs(w1nz.sum()-1) < 0.001
  assert (sum_w_zero | sum_w_one)

  # only execute  if there is at least one notnull value
  # below will work with nz
  if len(w1nz) > 0:

    # step 1:  make sure upper threshold is satisfied
    while max(w1nz) > weight_max:
      # clip at 30%
      w2 = w1nz.clip(upper=weight_max)
      # calc leftovers from this upper clip
      leftover_upper = 1 - w2.sum()
      # add leftovers to the untouched, in accordance with weight
      w2_touched = w2[w2 == weight_max]
      w2_unt = w2[(weight_max > w2) & (w2 > 0)]
      w2_unt_added = w2_unt + leftover_upper * w2_unt / w2_unt.sum()
      # concat all back
      w3 = pd.concat([w2_touched, w2_unt_added], axis=0)
      # same index for output and input
      #w3 = w3.reindex(w1nz.index) # todo prövar nu att ta bort .reindex överallt. ser om pd löser det själv automatiskt
      # rename w3 so that it works in a while loop
      w1nz = w3
    usestep2 = True
    if usestep2:
      # step 2: make sure lower threshold is satisfied
      if min(w1nz) < weight_min:
        # three parts: lower, middle, upper.
        # those in "lower" will recieve from those in "middle"
        upper = w1nz[w1nz >= weight_max]
        middle = w1nz[(w1nz > weight_min) & (w1nz < weight_max)]
        lower = w1nz[w1nz <= weight_min]
        # assert len
        assert (len(upper) + len(middle) + len(lower) == len(w1nz))
        # change lower to == weight_min
        lower_modified = lower.clip(lower=weight_min)
        # the weights given to "lower" is stolen from "middle"
        stolen_weigths = lower_modified.sum() - lower.sum()
        middle_modified = middle - stolen_weigths * middle / middle.sum()
        # concat
        w4 = pd.concat([lower_modified,
                        middle_modified,
                        upper], axis=0)
        # rename
        w1nz = w4

  # lastly, concat adjusted nonzero with zero.
  w1adj = pd.concat([w1nz, w1z], axis=0)
  assert abs(w1adj.sum() - 1 < 0.001)
  # sort index to get same column arrangements as input row.
  w1adj = w1adj.sort_index()
  assert (w1adj.index == w1.index).all()

  return (w1adj)


# todo decide rounding factor later.
# i used w1.round(6) but it returned an error called
# AttributeError: ("'float' object has no attribute 'rint'", u'occurred at index 2013-04-28 00:00:00')



## illustrate how the function works

illustrate_function = False
if illustrate_function:
  # read an example df
  wex = pd.read_excel('w_example_1.xlsx', index_col='date')
  wex.drop('random', axis=1, inplace=True)
  wex = wex / 100
  sum_one = (1 == wex.sum(axis=1))
  assert sum_one.all()

  # apply function
  wex_rescaled = wex.apply(rescale_w, axis=1,
                           weight_min=0.05, weight_max=0.30)

  # compare before vs after
  see_row = 10
  comparison = pd.concat([wex.iloc[see_row, :],
                          wex_rescaled.iloc[see_row, :].round(2)],
                         axis=1)
  print(comparison)


## test on real data.

# wei1
# is crated in another script. 4b-1-ggbasket.py

test_on_real_data = False
if test_on_real_data:


  # see how input looks
  arow = wei1.iloc[300, :]
  brow = wei1.iloc[600, :]
  pd.concat([arow, brow], axis=0).index
  arowf = arow.fillna(0)
  arowf[arowf==0]
  arowf[arowf>0]
  len(arowf[arowf==0])+len(arowf[arowf>0])

  # use f on one row
  arow.sort_values()
  ut = rescale_w(arow, weight_min=0.01, weight_max=0.50)
  ut_sorted = ut.sort_values(ascending=False)
  ut_sorted
  len(ut)
  len(arow)
  sum(ut.isnull())
  sum(arow.isnull())
  arow.fillna(0) # fattar ej vrf fillna inte påverkar någoting!

  # apply f on a matrix
  arow
  arow.sort_values()
  wei2 = wei1.iloc[1200:1300, :]
  wei2adj = wei2.apply(rescale_w, axis=1,
                       weight_min=0.05, weight_max=.50)

  # see a certain date
  wei2.loc['2017-01-01'].sort_values(ascending=False)[0:10]
  wei2adj.loc['2017-01-01'].sort_values(ascending=False)[0:10]

  # see before vs after
  pd.concat([wei2adj.iloc[0, :].sort_values(ascending=False)[0:10],
             wei2.iloc[0, :].sort_values(ascending=False)[0:10]],
            axis=1)

  # area plot, before vs after
  show_plot_before_vs_after = True
  if show_plot_before_vs_after:
    wei2adj.plot.area(legend=False)
    wei2.plot.area(legend=False)

  # study differences cap vs no cap, by asset.
  weidiff = wei2adj - wei2
  weidiff_bycoin = weidiff.mean(axis=0)
  weidiff_bycoin[weidiff_bycoin!=0].sort_values()[0:20]
  abs(weidiff).mean(axis=0).sort_values(ascending=False)

