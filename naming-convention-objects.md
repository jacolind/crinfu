---
title: naming conventions
description: how to name objects in coins3.py
date: 2018-07-26
---

# Three parts

a name consist of three parts:

1. type of data in in the cells (e.g. prices)
2. what columns they contain (e.g. virtual currencies)
3. what form the object is (e.g. matrix)

each part is separated with an underscore.

the names are abbreviated to three letters.

examples:

* `pri_vcc_mat` is a price matrix for virtual cryptocurrencies
* `mca_blx_vec` is a vector of market cap for our ETN.
* `ret_fin_mat` is a returns matrix for traditional financial assets.
* `ret_vccfin_mat` is a returns matrix for virtual currencies and traditional financial assets.

## details on part 1

part 1 has an exception. if the letter `fr` is applied it is a fraction, so that `volfr` is the fraction of volume. in order to create such an object we need to have a column called 'Total' what we can use as a divisor.

## examples of part 2

here is a list of all the the items we use now.
1. ret, pri, vol, mca. stands for: return, price, trading volume, market cap. also, fr is a possible suffix.
2. vcc, fin, blx. stands for: virtual currency, traditional financial asset, our certficiate BLX.
3. mat, vec. stands for matrix, vector.


## details on part 2

part 2 is not necessary. this is needed in the importing step to keep track of the content. however, the goal is to end up with only one price matrix containing all assets, and this matrix does not have any part 2 as it is not necessary. (an option would be to use `_all_` but we chose to leave it blank to signal to the reader this is the "clean" object)

# frequency

all time series objects, such as a returns matrix or price vector, have daily frequency if nothing is stated. if a frequency is not daily, the correct frequency should be appended to the name e.g. `_monthly` or `_quarterly`.

# column 'Others'

Lastly, we have a column called 'Others'.
- `Total` is the sum of all 1500+ coins.
- `Selected` is almost alway BTC and ETH. It is the same for evey comparison, but can be chosen in the beginning of the script.
- `Others` is simply Total minus Selected.

It is very useful, for example when plotting how much of the total market cap BLX is capturing -- in this graph we compare BLX to BTC, ETH and Others as it makes the plot easier to see. Below is an example.

```
## area plot of how much market cap BLX captures
# select what areas to plot
tickers_1 = ['BTC' + 'ETH' + 'Others']
colors_1 = ['Orange', 'Green', 'Grey']
vol_mat[tickers_1].plot.area(color=colors_1)
# select which lines to plot
vol_mat['BLX'].plot(lty=2, color='Blue')
plt.title('BLX captures more volume')
plt.show()

## line plot how much market cap BLX captures
tickers_2 = tickers_1 + ['BLX']
colors_2 = colors_1 + ['Blue']
vol_cs-e_mat[tickers_2].plot(color=colors_2)
plt.show()
```

# When does these conventions apply?

most objects follow the rules but some do not.

some temporary objects or objects used very little does not follow this standard, such as
* `nrcoins` the variable that holds the nr of coins in our index
* `startdate`, `startdate2`, etc..
* `tickers_top10, tickers_member, tickers_selected` everyone is a list of ticker names
* etc...
