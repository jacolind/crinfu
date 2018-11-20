"""
create a bunch of different indexes using ggindex() and compare their properties.
"""

## create index from ggindex

# see default values
?ggindex()
# defaults are
# top 10
# monthly rebelance
# startdate = 1y after marketcap matrix first date.

top10_monthly = ggindex(mca_vcc_mat, ret_vcc_mat, vol_vcc_mat)

top5_monthly = ggindex(mca_vcc_mat, ret_vcc_mat, vol_vcc_mat,
                            nrtop=5)

top5_equal_monthly = ggindex(mca_vcc_mat, ret_vcc_mat, vol_vcc_mat,
                             nrtop=5,
                             weighting_equal=True)

top5_equal_weekly = ggindex(mca_vcc_mat, ret_vcc_mat, vol_vcc_mat,
                            nrtop=5,
                            rebalance_freq='W',
                            weighting_equal=True)

# todo i have an error with rebalancing.
(top5_equal_weekly.returns == top5_equal_monthly.returns).all()

# returns diff
top5_equal_monthly.returns.mean()
top10_monthly.returns.mean()

# corr
pd.concat([top5_equal_monthly.returns,
           top10_monthly.returns,
           top5_equal_weekly.returns
           ],
           axis=1).corr()
