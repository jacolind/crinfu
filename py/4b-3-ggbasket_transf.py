"""
combine xyz_vcc_mat and xyz_fin_mat with df_blx to become xyz_mat for xyz = [ret, mca, pri, mcafr, volfr]
code below is copied from `4_transform.py`
todo read it and see if it must be modified now that we have ggindex().

these objects will be analyzed in scripts 9-ggbasket-...
"""

## create ret_vcc_mat

ret_vcc_mat = price2return(pri_vcc_mat)

## create indexes

# naming convention: one letter indicating parameter, then a letter/number indicating answer on that parameter. separated by dash.

# top 10, weighted marketcap, rebalanced monthly
w1, r1, m1, v1 = ggbasket(name='t10-wm-rm',
                          nrtop=10,             # t10
                          rebalance_freq='MS',   # -rm
                          weighting='marketcap') # -wm
# top 10, weighted marketcap smoothed, rebalanced monthly
w2, r2, m2, v2 = ggbasket(name='t10-wms-rm',
                          nrtop=10, rebalance_freq='MS',
                          weighting='marketcap',
                          smooth=True)
w3, r3, m3, v3, = ggbasket(name='t5-we-rm',
                           nrtop=5, rebalance_freq='MS',
                           weighting='equal')
w4, r4, m4, v4 = ggbasket(name='t5-wm-rm',
                          nrtop=5, rebalance_freq='MS',
                          weighting='marketcap')
w5, r5, m5, v5 = ggbasket(name='t5-wsm-rm',
                          nrtop=5,
                          rebalance_freq='MS',
                          weighting='marketcap',
                          smooth=True)
# floor to min weight 1%
w6,r6,m6,v6 = ggbasket(name='t5-wm-rm-f1',
                       nrtop=5, rebalance_freq='MS',
                       weighting='marketcap',
                       weight_min=0.01
                       )
# floor 1% cap 30%
w6,r6,m6,v6 = ggbasket(name='t5-wm-rm-f1c30',
                       nrtop=5, rebalance_freq='MS',
                       weighting='marketcap',
                       weight_min=0.01, weight_max=0.30
                       )

w7,r7,m7,v7 = ggbasket(name='t10-wm-rm-f1c30',
                       nrtop=10, rebalance_freq='MS',
                       weighting='marketcap',
                       weight_min=0.01, weight_max=0.30
                       )

w8,r8,m8,v8 = ggbasket(name='t10-wm-rm-f2c50',
                       nrtop=10, rebalance_freq='MS',
                       weighting='marketcap',
                       weight_min=0.02, weight_max=0.50
                       )

w9,r9,m9,v9 = ggbasket(name='t10-wm-rm-f5',
                       nrtop=10, rebalance_freq='MS',
                       weighting='marketcap',
                       weight_min=0.05, weight_max=1
                       )


## matrices of baskets

ret_bsk_mat = pd.concat([r1, r2, r3, r4, r5, r6, r7, r8, r9],
                        axis=1)
# all names
ret_bsk_mat.columns

wei_bsk_mat = pd.concat([w1,w2,w3,w4,w5,w6,w7,w8,w9],
                        axis=1)

# these objects are analyzed in 9-ggbasket-ret.py

## effect of caps and floors

# see 9



