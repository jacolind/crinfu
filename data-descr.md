**/data-coins**
50 coins from coinometrics
website where I downloaded "all.zip"
but xrp have empty values for some reason
they included noncrypo returns, which are shown in

**/data-financial**
conatin four csv files comes from coinometrics
(gold, liborusd, sp500, dxy).
it also contains the excel file `price_tradfinance.xlsx` which was extracted using b.

**/data-xbt**
is data on the xbt certificates. I have not used it.

**/data-manual**
is from a manual job usign coinmarketcap.com

**/crypto_data**
is from timescale.com medium post
maybe not useful

**/data-allcoins**
1531 items. is downloaded using the R package, see fie `coin_scrape.R`

# todo

double check "data-allcoins" the total is 24 MB and the file itself is larger, can that be true?

remove libs I dont use.

put libs under one folder "data" and have subfolders, looks cleaner.
