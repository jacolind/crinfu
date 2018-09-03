"""
output: summarystats, both in the form of tables and sentences using print().
saved in /output/ and /output/vip/ as text files.

https://donatstudios.com/CsvToMarkdownTable

http://mpastell.com/pweave/index.html
"""

# coins that has been in fund
with open("output/tkr_beeninblx.txt", "w") as text_file:
    text_file.write("Coins that once has been in top 10 \n \n" +
                    str(tkr_beeninblx))

# returnstable for selected, blx, fin
tbl_ret_1 = returns_vol_tbl(df=ret_mat, start='2017', assets=tkr_sel_blx_fin)
tbl_ret_1.to_csv('output/tbl_ret_1.csv')
