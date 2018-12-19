# how pop works
alist = [1, 2, 3]
first = alist.pop(0)
alist
first

m # market cap matrix
rm # ranked market cap matrix

# selection
mca_vcc_mat.iloc[10, :]
mca_vcc_mat.iloc[10, :].index
mca_vcc_mat.iloc[10, :].values

for i in range(m.shape[0]):
  '''
  m is marketcap 
  rm is ranked marketcap 
  '''

  m_row = m.iloc[i, :] # does this have an index and colnames?
  rm_row = m_row.rank() # todo add the specifications
  m_row_prev = m.iloc[i - 1, :]
  # top 8 selected immediately
  b_row = (m_row =< 8)
  # take 2 more. currently ranked 9-12 gets priority if they was incl before.

# en annan approach kan vara att ta "vi tar alltid top 10, men vissa av rank 9:12 hanteras annorlunda".



# pop approaach

rownr = 1000
m_row = mca_vcc_mat.iloc[rownr, :] # example row
m_row_prev = mca_vcc_mat.iloc[rownr-1, :] # example row
m_row.sort_values(ascending=False)[0:8] # top 8
m_row.sort_values(ascending=False)[8:12] # ranked 9-12

