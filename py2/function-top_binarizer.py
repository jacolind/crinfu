# -*- coding: utf-8 -*-
"""
function top_binarizer() was previously used to create the binary matrix `bmc_mat`.

top_binarizer() can be built upon to make a more realistic binary matrix.
because currently it is based on rank of market cap.
in reality, however, it is more complex.
for example, nr 11 will have to beat nr 10 for three consecutive months in order to be a constituent.
"""

def top_binarizer(row, p):
    """
    Return 1 if a coin's mcap is within top p
    return 0 otherwise
    """
    # convert to pandas series. maybe not needed but safer
    row = pd.Series(row)
    # sort row
    row_sorted = row.sort_values(ascending=False)
    # find threshold value (e.g 11th value)
    threshold = row_sorted[p]
    # give a zero if a coin's mcap is less than threshold:
    binary = (row.values > threshold).astype('int')
    return binary

#threshold = row_sorted[p]
#binary = (row.values > threshold).astype('int')
