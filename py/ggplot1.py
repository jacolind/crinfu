"""
this script demonstrates ggplot in python.

todo run script at clinux.
todo see if data must be long for ggplot. 
"""

from ggplot import *

## graphs from website
# -----------------------------------------------------------------------------

## fun

ggplot(diamonds, aes(x='carat', y='price', color='cut')) +\
    geom_point() +\
    scale_color_brewer(type='diverging', palette=4) +\
    xlab("Carats") + ylab("Price") + ggtitle("Diamonds")

## powerful

ggplot(diamonds, aes(x='price', fill='cut')) +\
    geom_density(alpha=0.25) +\
    facet_wrap("clarity")


## qplot

qplot(x=df.time, y=df.lifeexp, color=df.region, fill=df.gdp,
      xlab="Year", ylab="Life expectancy",
      main="Health improves across the world")
# can add xlim=(0, 100) ylim=(-1, 200) log="y"

## themes

# http://ggplot.yhathq.com/docs/theme_seaborn.html
ggplot(aes('carat', 'price'), data=diamonds) +\
 geom_point() + theme_seaborn(context='poster')
# black white
ggplot(aes('carat', 'price'), data=diamonds) + geom_point() + theme_bw()



## graphs with my own data
# -----------------------------------------------------------------------------

# todo go to plot.py and do them with ggplot syntax

# how does it work when one variable is in the index?
# should i do .reset_index() so that i can access date variable?
# i must change from wide to long format to use ggplot? i mean, what is y?
dfl_vcc = pd.read_csv(filepath1long, parse_dates=True)
ggplot(ret2aum(dfl_vcc.loc[dfl_vcc.symbol.isin(['BTC', 'ETH'])]),
       aes('date', 'return')) + geom_point()
