## test out the samller f() on real data
bin1 = mcap2binary(marketcap_matrix=mca_vcc_mat,
                  nrtop=10, rebalance_freq='M')
wei1 = binary2weight(bin1, mca_vcc_mat,
                      rebalance_freq='M',
                      weighting='marketcap')
wei1.sum(axis=1)
wei1cf1 = wei1.loc['2018':].apply(rescale_w, axis=1,
                     weight_min=0.02, weight_max=0.30)
wei1.loc['2018-02-01'].sort_values(ascending=False)[0:11]
wei1cf1.loc['2018-02-01'].sort_values(ascending=False)[0:11]
# this should be equivalent to the above. take much more time with minmax weights.
wei2 = binary2weight(bin1.iloc[300:400, :],
                     mca_vcc_mat.iloc[300:400, :],
                     rebalance_freq='M',
                     weighting='marketcap',
                     weight_min=0.02, weight_max=0.30)

#
rescale_w(wei1.loc['2016-10-01',:],
           weight_min=0.02, weight_max=0.30).sort_values()
wei1.loc['2016-01-01']
wei1cf = binary2weight(bin1, mca_vcc_mat.loc['2016':],
                      rebalance_freq='M',
                      weighting='marketcap',
                       weight_min=0.02, weight_max=0.30)
