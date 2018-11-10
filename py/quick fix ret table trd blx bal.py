#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:55:53 2018

@author: he2
"""

tkr_sel_2
tkr_sel_3

ret = ret_mat
ret['TRD'] = ret['Stocks']*0.60 + ret['Bonds']*0.40

ret.BLX

ret['BAL'] = ret.BLX*0.05 + ret.TRD*0.95

tkr_sel_4 = ['TRD', 'BLX', 'BAL']


def returns_vol_tbl(df, assets, start, end='2018-04', T=12):
    """start with rr since it contains fund and coins returns.
    T=12 for monthly data and T=365 for daily data.
    output returnstable for a certain period.
    """
    # calc mean and vol
    ret = df.loc[start:end, assets].mean() * T
    vol = df.loc[start:end, assets].std() * np.sqrt(T)
    # put into tbl 
    tbl = pd.concat([ret, vol], axis=1)
    # rename
    tbl.columns = ['Return', 'Volatility']
    tbl['Return / Vol'] = tbl['Return'] / tbl['Volatility']
    return tbl.round(2).T
    
returns_vol_tbl(ret, tkr_sel_4, '2015-04', '2018-04', 
                252).to_csv('output/retvoltbl_simplified.txt')


returns_vol_tbl(ret, tkr_sel_4, '2015-04', '2018-04', 
                252)