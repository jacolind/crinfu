'''
this script tests and illustrates the function rescale_w()
'''



## illustrate how the function works

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
arow.fillna(0) # fattar ej vrf fillna doe snot affect anything

# apply f on a matrix
arow
arow.sort_values()
wei2 = wei1.iloc[1200:1300, :]
wei2adj = wei2.apply(rescale_w, axis=1,
                     weight_min=0.05, weight_max=.50)

# see a certain date
wei2.loc['2017-01-01'].nlargest(10)
wei2adj.loc['2017-01-01'].nlargest(10)

# see before vs after
pd.concat([wei2adj.iloc[0, :].nlargest(10),
           wei2.iloc[0, :].nlargest(10)],
          axis=1)

# area plot, before vs after
show_plot_before_vs_after = True
if show_plot_before_vs_after:
  wei2adj.plot.area(legend=False)
  wei2.plot.area(legend=False)

# study differences cap vs no cap, by asset.
weidiff = wei2adj - wei2
weidiff_bycoin = weidiff.mean(axis=0)
weidiff_bycoin[weidiff_bycoin!=0]..nlargest(20)
abs(weidiff).mean(axis=0).sort_values(ascending=False)

