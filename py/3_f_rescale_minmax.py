'''
this script defines one function, and illustrates how it is used
'''

## define function

def rescale_w_minmax(row_input, weight_min, weight_max):
  '''
  will run marketcap_matrix.apply(thisfunction, 0.01, 0.30)

  :param row_input: a row from a pandas df
  :param weight_min: a number
  :param weight_max: a number
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
  (except those whose weight == max_weight)
  '''

  # rename
  w1 = row_input

  # step 1:  make sure upper threshold is satisfied
  while max(w1) > weight_max:
    # clip at 30%
    w2 = w1.clip(upper=weight_max)
    # calc leftovers from this upper clip
    leftover_upper = 1 - w2.sum()
    # three non-overlapping sets
    w2_touched = w2[w2 == weight_max]
    w2_unt = w2[(weight_max > w2) & (w2 > 0)]
    w2_zero = w2[w2 == 0]
    # add leftovers to the untouched, in accordance with weight
    w2_unt_added = w2_unt + leftover_upper * w2_unt / w2_unt.sum()
    #
    w2_unt_added
    w2_touched
    w2_zero
    # check indexes are intact
    s1 = set(w2_touched.index)
    s2 = set(w2_unt_added.index)
    s3 = set(w2_zero.index)
    sets = s1.union(s2).union(s3)
    assert set(w1.index) == sets
    # add it all back
    w3 = pd.concat([w2_touched, w2_unt_added, w2_zero], axis=0)
    # same index for output and input
    w3 = w3.reindex(w1.index)
    # sum to 1
    assert abs(w3.sum() - 1) < 0.001
    # rename w3 to w1 so that it works in a while loop
    w1 = w3
  # pd.concat([row_input, w1], axis=1) # see input vs output

  # step 2: make sure lower threshold is satisfied
  if min(w1[w1>0]) < weight_min:
    # (w1[w1>0].clip(lower=0.02) != w1[w1>0]).any() # equivalnet but harder to understand
    # four parts
    w1_upper = w1[w1 == weight_max]
    w1_zero = w1[w1 == 0]
    w1_below_lth = w1[(w1>0) & (w1<weight_min)] # "lth" is lower threshold
    w1_above_lth = w1[(w1>weight_min) & (w1<weight_max)]
    # assert all ara distinct
    len_four = len(w1_upper) + len(w1_zero) + len(w1_below_lth) + len(w1_above_lth)
    assert(len_four == len(w1))
    # todo add more fancy with asserting set of index is the empty set, and union of the four's sets is == set of index before it was divided to four parts
    # change those >0 but below weight_min to == weight_min
    w1_below_lth_mod = w1_below_lth.clip(lower=weight_min)
    # remove leftovers on those with weight between 2% and 30%
    leftover_lower = w1_below_lth_mod.sum() -  w1_below_lth.sum()
    w1_above_lth_mod = w1_above_lth - leftover_lower * w1_above_lth  / w1_above_lth.sum()
    # add i all back
    w4 = pd.concat([w1_upper, w1_zero, # these two were not changed
                    w1_below_lth_mod,
                    w1_above_lth_mod],
                   axis=0)
    # same index for output and input
    w4 = w4.reindex(w1.index)
    pd.concat([row_input, w1, w1], axis=1)
    # sum to 1
    assert abs(w5.sum() - 1) < 0.001
    # rename to w1 so that the function() works in its enterity
    w1 = w4
  # pd.concat([row_input, w1], axis=1) # see input vs output

  # return both upper and lower clip
  return(w1.round(6))  # todo decide rounding factor later


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
  wex_rescaled = wex.apply(rescale_w_minmax, axis=1,
                     weight_min=0.02, weight_max=0.30)

  # compare before vs after
  see_row = 10
  comparison = pd.concat([wex.iloc[see_row, :],
             wex_rescaled.iloc[see_row, :].round(2)],
            axis=1)
  print(comparison)
