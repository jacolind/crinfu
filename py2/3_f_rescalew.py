'''
this script defines a function, and illustrates how it is used
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
      #w3 = w3.reindex(w1nz.index) # todo provar nu att ta bort .reindex overallt. ser om pd loser det sjaalv automatiskt
      # rename w3 so that it works in a while loop
      w1nz = w3
    usestep2 = True # set to false is useful for debugging
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