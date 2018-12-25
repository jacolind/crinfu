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

create_from_functions = True
create_by_importing = not create_from_functions

# if create_from_functions:

# "the market". is 10, weighted marketcap, rebalanced monthly
w0, r0, m0, v0 = ggbasket(name='market', # t200-wm-rw
                          nrtop=200,
                          rebalance_freq='W',
                          weighting='marketcap')

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

##

w1.index
r1.index

## create ret bsk and wei bsk

# ret mat is useful because it contains names and returns will be heavily analzyed
ret_bsk_mat = pd.concat([r0, r1, r2, r3, r4, r5, r6, r7, r8, r9],
                        axis=1)

ret_bsk_list = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9]
wei_bsk_list = [w0, w1, w2, w3, w4, w5, w6, w7, w8, w9]

## save weights to disk

# the w matrix can be imported since fram that everything else can be conputed

# save w mat to disk
for k in range(0, len(wei_bsk_list)):
  matrix = wei_bsk_list[k]
  matrix_mthly = matrix.resample('MS').first()
  file = 'object/wei_bsk_mat/' + 'w' + str(k) + '.csv'
  matrix_mthly.to_csv(file)

  # naming
  ret = ret_bsk_list[k]
  name = str(ret.name)
  file2 = 'w' + str(k) + ' is ' + name
  descr = 'name of basket: ' + name + '\n \n'
  text_export(name, file2, description=descr,
              folder='object/wei_bsk_mat/')



#if create_by_importing:
# todo write code that imports from file rather than from script. might save some time but probably not.


## create monthly

w1m = w1.resample('MS').first()
w4m = w4.resample('MS').first()
w8m = w8.resample('MS').first()

## create ticker lists

# tickers that are in top 10 and top 5 now
tkr_t10now = w1.iloc[-1].nlargest(10).index
tkr_t5now = w4.iloc[-1].nlargest(5).index
# tickers that have been in top10 and top5 basket
tkr_t10hasbeen = w1.columns[w1.sum()>0]
tkr_t5hasbeen = w4.columns[w4.sum()>0]
# largest historical weights in the top10 fund
tkr_t5hist = w1.sum().nlargest(5).index
# assert top5 historical is the same for both top10 and top5 baskets
assert (tkr_t5hist == w4.sum().nlargest(5).index).all()

## matrices of baskets


# all names
ret_bsk_mat.columns


# these objects are analyzed in 9-bsk_ret.py

## effect of caps and floors

# see 9



