"""
check that import.py was done correctly.
"""

# same shape and index in market cap and price matrix
assert mca_vcc_mat.shape == pri_vcc_mat.shape
assert (mca_vcc_mat.index == pri_vcc_mat.index).all()

# daily frequency
mca_vcc_mat.index.freq
pri_vcc_mat.index.freq

# and so on... todo e2: more cheks haed and tail to inspect. etc.
# can look into the ipynb and see what checks are reasonable to include.

# check fin
pri_fin_mat.tail()
pri_fin_mat.plot()

"""
note to self: check the following
  - correct freq
  - sum NA
  - boxplots on prices or returns
  - more...

for inspiration on checks to do, see these Ins within coins2_20180415_1017.html
48, 46, 53 check_calc
77, check_calc
86-95, read and clean fin data
and possibly more. search for all assert statements for example. or "check".
"""
