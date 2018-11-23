# created 20181121
# attempt to do stuff like HH says with keeping the long format 

## lib 

library(dplyr)
library(readr)
library(tidyr)
library(lubridate)

## gather spread analysis 

# question: does spread() produce what I want? 
table <- read_excel("~/pythonR/RStudio/coins/gather-spread-example.xlsx")
table
table %>%
  spread(key=symbol, value=price)
table %>%
  spread(key=symbol, value=price) %>%
  is.na()
rm(table)
# conclusion: yes it works

## read 

# if script is run for first time, or with new data from database, run this
create_files <- FALSE

# if csv files not created then run this 
if (create_files){
  df <- read_csv("~/pythonR/RStudio/coins/data/CryptoData.csv")
  df <- filter(df, ranknow < 201)
  write_csv(df, "data/CryptoData_top200.csv")
}

# read
use_top200 <- TRUE
file <- ifelse(use_top200,
       "data/CryptoData_top200.csv",
       "data/CryptoData.csv")
df <- read_csv(file)

# create n 
n <- unique(df$date)


# selct cols 
df <- df %>%
  mutate(year = year(date), 
         month = month(date)) %>%
  select(date, year, month, 
         symbol, ranknow, 
         close, volume, market) %>%
  rename(price = close, mcap = market)

# see ranknow variable is static. same for all dates. so it is useless.
df %>%
  filter(symbol == "LTC") %>%
  select(ranknow) %>%
  table()
# delect cols 
df <- select(df, -ranknow)

# see dates are sorted from beginning to end, as it should be.
df %>%
  select(date) %>%
  head(3)

# create return 
df <- df %>%
  group_by(symbol) %>%
  mutate(return = log(price) - log(lag(price))) %>%
  ungroup()

# see how groupby works 
df %>%
  group_by(year, month) 

# create rank 
df <- df %>%
  group_by(date) %>%
  mutate(rank = min_rank(desc(mcap))) %>%
  ungroup()

# create list of coins in top 10 
tkr_been_in_top10 <- df %>%
  filter(rank < 11) %>%
  select(symbol) %>%
  unique()
tkr_been_in_top10 <- tkr_been_in_top10$symbol


# see rank distribution for a particular asset
df %>%
  filter(symbol == "XRP") %>%
  select(date, rank) %>%
  table() %>% colMeans() %>% round(2)

# volume and return has na 
df %>%
  is.na() %>%
  colMeans()

# count assets with NA volume 
df %>%
  filter(is.na(volume)) %>%
  select(symbol) %>%
  table()

# todo how to solve na volume? na.approx or ffill? do not know. solve later 
# library(zoo)
# df %>%
#   group_by(symbol, date) %>%
#   mutate(volume2 = na.approx(volume, date)) %>%
#   filter(is.na(volume2))
  

## weight, if rebalanced daily 

df %>%
  group_by(date) %>%
  mutate(included = rank < 11) %>%
  filter(rank < 11) %>%
  mutate(weight = mcap / sum(mcap)) %>%
  ungroup() %>%
  arrange(date) %>%
  filter(year == 2018, month == 4) %>%
  # see three "sections"
  print(n=3*10)

## weight, if rebalanced monthly 

df %>%
  filter(year > 2017) %>% # to see when many coins are in the set
  select(-price, -return) %>%
  mutate(inlcuded = as.integer(rank < 11)) %>%
  filter(day(date) == 1, rank < 11) %>%
  group_by(date) %>%
  mutate(weight = mcap / sum(mcap)) %>%
  ungroup() %>%
  arrange(date, rank) %>%
  print(n=30)


## weight, if min and max weights are 30% and 1%

df %>%
  filter(year > 2017) %>% # to see when many coins are in the set
  select(-price, -return, -volume, -year,-month) %>% # easier viewing 
  mutate(inlcuded = as.integer(rank < 11)) %>%
  filter(day(date) == 1, rank < 11) %>%
  group_by(date) %>%
  mutate(weight = mcap / sum(mcap)) %>%
  mutate(w_minmax = w_rescale_minmax(weight, 0.01, 0.30)) %>%
  ungroup() %>%
  arrange(date, rank) %>%
  print(n=30) %>%
  select(date, symbol, w_minmax)

## weight, if stagnant contituents ("tröghet") is used 

df %>%
  filter(year > 2017) %>% # to see when many coins are in the set
  select(-price, -return, -volume, -mcap) %>%
  filter(day(date) == 1) %>%
  mutate(rank_top10 = as.integer(rank < 11)) %>%
  group_by(symbol) %>%
  mutate(lag(rank_top10)) %>%
  print(n=30)



# included: if rank is> 10 then <10 only include if it stays there for a month
df %>%
  filter(year > 2017) %>%
  group_by(symbol) %>%
  mutate(incl = rank < 8) %>%
  # stagnant inclusion: only if it is included twice map to 1, 
  # and if rank<10 twice map to 0 
  mutate(incl_stagnant = incl + lag(incl) == 2) %>%
  select(-price, -volume, -mcap, -return) %>%
  filter(symbol == "LTC")

## weight, smoothed 

# smoothing procedure: on daily data take marketcap last n=20 days. apply EWMA. go to monthly data. apply standard w = smoothed mcap / tot(smoothed mcap)
# that is one way. not THE way. how do others do it? 
# for now use average not EWMA

# first  weights then smooth them => not sure weights sum to one 
# first smooth mcap then weights => weight sum to one. 

# ewma is dependent on group size
df %>%
  group_by(symbol) %>%
  group_size() %>%
  min()
df %>%
  filter(symbol %in% tkr_been_in_top10) %>%
  group_by(symbol) %>%
  group_size() %>%
  min()

# calc ewma 
df2 <- df %>%
  # filter only top10 so we can use large n in EWMA 
  filter(symbol %in% tkr_been_in_top10) %>%
  # smooth mcap
  group_by(symbol) %>%
  mutate(mcap_smooth = TTR::EMA(mcap, n=60)) %>%
  # weight is fraction of mcap and sum(mcap)
  group_by(date) %>%
  mutate(w        = mcap / sum(mcap),
         w_smooth = mcap_smooth / sum(mcap_smooth)) %>%
  # view 
  ungroup()

# calc diff between smoothign and not smoothing. it does make a diff!
df2 %>%
  group_by(symbol) %>%
  summarise(mean_delta = mean(w / w_smooth - 1, na.rm=TRUE)) %>%
  arrange(mean_delta %>% abs() %>% desc() )

## calc return tables 

df3 <- df %>%
  filter(date > "2015-04-01") %>%
  group_by(date) %>%
  summarise(mcap_all = sum(mcap)/10^9)

ggplot(df3, 
  aes(x=date, y=mcap_all)) + 
  # todo add log = TRUE 
  geom_line() +
  ggtitle("Total market cap") + 
  label(y="Market capitalization in $ billion")

