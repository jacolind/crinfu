## Loading libraries, functions, data and setwd

library(crypto)
library(Rcpp)
library(tidyr)
library(magrittr)
library(jsonlite)
library(dplyr)
library(lubridate)
library(curl)
library(utils)
library(parallel)
library(stats)
library(doSNOW)

library(Quandl)
library(data.table)
library(devtools)
library(crypto)
library(quantmod)

## get coins

cryptoData <- getCoins()
write.csv(cryptoData, "data-crypto/CryptoData.csv")

cryptoDataWide <- reshape(cryptoData, idvar = "date", timevar="name", direction = "wide")
cryptoDataWide <- as.data.table(cryptoDataWide)
write.csv(cryptoDataWide, "data-crypto/CryptoDataWide.csv")

unique(cryptoData$date) # 1807 days from 2018-04-11 to 2013-04-28
unique(cryptoData$symbol) #1527 coins

metaCryptoDataWide <- CC(cryptoDataWide)
fwrite(metaCryptoDataWide, "data-crypto/metaCryptoDataWide.csv")

## jessevent

install_github("jessevent/crypto")
#<- ave(data$value, data$id, FUN=function(x) c(0, diff(x)))

## quantmod

getSymbols('F')
saveSymbols('F', file.path = "data-crypto/CryptoFund")
testload <- load("data-crypto/F.RData")

## quandl

Quandl.api_key("it is a secret")

# example
head(Quandl("OPEC/ORB"))

# save omxs30
OMXS30NI <- Quandl("NASDAQOMX/OMXS30NI")
write.csv(OMXS30NI, "OMXS30NI.csv")
