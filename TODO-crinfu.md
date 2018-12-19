title: todo
description: we do "goal driven" data anlaysis i.e. not just exploring for the fun of it.

# inbox

it would be fun to make a function that analyzes delta weight in two different index constructions at a certain date. see for example comparrisons between befoore/after caps & floors 1% 30%

kanske ska sätta resample till
.resample('BMS').first()
som är första business day of month.

För skojs skull pröva att w bestäms av smoothed trading volume. då får man tims liq index.


kör lite bredare streck i vissa grafer

------------------------------------------------------------------------------


# next: before irl meeting

## få alla plottar att funka. är nog 9 wei 9 ret som är problemet

## fil-struktur

splitta upp 7 plot filen i flera mindre. tex plot corr. och det är snarare EDA än plot ty tabeller tas fram oxå.

då kan jag lättare felsöka vrf det blir konstig output

## printa, färger ok?

## commit and close.


## dead coins

out of those ca 50 coins that has been top10, what is their status now? how many are dead? (first, define dead then count the nr of dead.)


## read hodlbot articles

read hodlbot data analysis and see what should be included for us.


## marketcap na. how to handle?

marketcap has na. how should we handle it?

i think na.approx() is best.  

when using .reindex do not fill with zero but with na.approx so that we do not see zero return on days when price is NA.


## drawdown

drawdown(price_matrix, time=365):

## bokeh manual

läs den och testa runt


## statsmodel manual

läs

## sns manual

läs seaborn manualen


## selection criterias till kod

### tröghet

och sen se hur det blir med tröghet vs ewma

Se crypto market cap Nomics artikeln. Kanske göra ngt av deras.

## wei intra month

the first evey month the weights are re-set.
if btc has w 50% on day 1 and on day 5 its price has increased by 10% and all other assets are standing still, then portf w in btc will be 55%. if we look at data, how does this appear? see the turnover calculations for details. maybe chat with blechley. they say turnover is minescule for some months.  


## printa plots i svartvitt o se hur dom ser ut


## att göra enl slides

ska ha denna bild. så gör en vol ret plot av detta.

    ![Increasing choice can only lead to better outcomes.](markovitz plot both top10vcc and TRD assets)

---

![Digital assets exhibit low correlation with traditional assets.](corr matrix. för såväl _vcc_ som _fin_ plotta 5st till 10st och med/utan indexet.)
10+1+10+1=22 för många cols tror jag
5+1+5+1=12 st cols är max tror jag
kanske kör 5+1+1=6st cols så alla vcc men bara sp500.
ska jag ha sp500 eller bal förresten?


## download financial data on sp500  clinux

see file stocks.py

want marketcap on this as well.


## rollcorr with +- std.

more thought can be put in here, and do fun stat stuff.
there is a sns plot for this premade!

    # plot rolling mean with vol bands. good for mcap or rollcorr plot.
    m = roll.agg(['mean', 'std'])
    ax = m['mean'].plot()
    ax.fill_between(m.index, m['mean'] - m['std'], m['mean'] + m['std'],
                    alpha=.25)
    plt.tight_layout()
    plt.ylabel("Close ($)")
    sns.despine()




## stat analys på indexes

https://kurser.math.su.se/pluginfile.php/20130/mod_folder/content/0/Kandidat/2016/2016_04_report.pdf?forcedownload=1
see plots in that, and measures: nr obcs, nr NA, min mean medin max var vol skew kurt

Alla index, samt "the market" som är sum of the mcap. Dom ska jämföras på ett simpelt sätt.

Ret vol table
Corr matrix
Corr över tid

## stat package

anv ngt stat / trading package för att generera automatiska plots, tex

statsmodels

cufflinks and py-quantmod
source https://quant.stackexchange.com/questions/30834/quantmod-alternative-for-pandas
se
https://github.com/jackluo/py-quantmod
https://github.com/santosjorge/cufflinks
  http://nbviewer.jupyter.org/gist/santosjorge/b278ce0ae2448f47c31d
  http://nbviewer.jupyter.org/gist/santosjorge/aba934a0d20023a136c2


zipline
source https://stackoverflow.com/questions/18275306/does-python-has-a-similar-library-like-quantmod-in-r-that-can-download-financial
dokumenteart bra http://www.zipline.io/index.html




# maybe


## colors

use these colors:

URL:
http://colorbrewer2.org/?type=diverging&scheme=Spectral&n=5

JavaScript:
['#d7191c','#fdae61','#ffffbf','#abdda4','#2b83ba']
[red, orange, beige, green, blue]
[last_resort, btc, stocks / bonds / xrp / others, eth, blx]





-----------------------------------------------------------------------------

# afer irl meeting

## plot krashes

a famous youtube video "it went all to x, and then it krashed."
slice out those timeperiods, and make a figure with many plots in it.




## output key objects to csv

the objects found in `naming-convention-objects.md` can be exported to csv.

then i can import to R use ggplot instead of `...plot.py` and use shiny to vizualize general index constuction.

one problem: have to research how to make a nice corr plot which is now done with seaborn.


## shiny apps

### learn shiny

learn by doing, but i must also read about how it works.

read this doc
https://bookdown.org/yihui/rmarkdown/shiny-documents.html

### index competition with ggindex()

use the ggindex function to generate shiny app. plot the aum of usd 100 invesment. show table with return and risk (vol, IR, sharpe, sortino, 95% VaR).

input: date, checkbox with prebuilt indexes (top5 EW/mcap, top10 EW/mcap, btc, and their custom built index). OR generate a few different indexes yourself and then compare them (this is harder for me and harder for the user but is more general so have it as a version 2).


### corr matrix, giph  

input: start date (slider yyyy-mm), length of window (type in nr of months), input selectize type name of tickers.
v1 only tickers. v2 tickers AND name will match.   

output: corr plot.

v3 do a slider so that you can see the colors changing over time.  

### corr over time

input: 2-6 assets

output: rollcorr graph.



## when echange data is present

### hedging with equal weights vs liquidity weighted

if we have order book data we can asses if liquidity weighted would cross the spread more often.

### hedging on 1 vs 3 echanges

see price diff of buying on one exchange vs buying on three. if delta is low then IT barrier.


## index and cols

see the printout of `tranform-check`. it is not very rigourous, some matrices have more cols/rows than others.
this is due to importing. it can be fixed. i am not sure now how much all results are affected.


## web plots

@nxt @waitingfor web guys to say if html worked or not. if it worked, proceed with the idea below.

ide: pick a date, to see
* weights per asset. in a table or horizontal bar graph.
* blx value
* blx annualized return last 6m.
this can be done in shiny actually.

mcap over time, with hover = asset_name

corr matrix, hover visar pair & corr med två digits, samt p värde inom parentes.
gärna samma färg-schema som existerande plots.


## sifr

https://www.sifrdata.com/category/market-data/ ha med dessa grejer

## plot style

testa att ha kvar matplotlib men ändra till

    plt.style.use('seaborn-notebook')
    #styles: ggplot , seaborn-notebook or -talk or -poster

try seaborn?

try this:

    corr_mat = # some code
    sns.clustermap(corr_mat)

try ggplot theme in matplotlib?  


## B daily

`B_daily = B_monthly.resample('M', method='ffill')` and then use daily data for the fund!
now i have monthly data for the fund. what if we still use monthly re-weights but keep the data in daily format? then B matrix would have to be replicated 30 times for each row. it is more normal to work with dialy data and by doing so we can see how plots change.
detta bör göras så att fundret by defn är månatlig. i binarizer kan man välja resample freq. fundera bara igenom vilken ordning det blir dvs det du gjorde i excelfilen med sumproduct, vilken vikt blir var?
^^ är detta done?





--------------------------------------------------------------------------------

# inbox

below are some things i want to do but have not prioritized them into "next"

i filen som håkan ger mig skulle man kunna filtrera bort dom coins som aldrig varit top 50. ty det minskar datan enormt. och variabeln rank finns som är ranking av marketcap.


## notebook -> .py

change from juputer notebook to regular python files. increases performance, sharability (with others + latex).

## network analysis

`20-network-analysis-in-python-part-1`
take course and implement learnings in this project.

## small thing re plots

    # remove dead space in the volumes and mcap plots
    plt.axis('tight')

    # notes
    df[::2, ::4] # every other row, every 4th col


## ACF PACF - stylized facts

AUTOCORR & EDA: titta på vilka sorts grafer du har gjort i thesis. gör dessa för denna data. kolla tex btc och eth först. hur är ACF och PACF? ser vi samma mönster som i finansdata? se snotes "python time-series"

financial data have some properties (google for "stylized facts of asset returns") such as vol clustering, leverage effect, heavy tails, autocorr, etc. do crypto have this as well.

https://tomaugspurger.github.io/modern-7-timeseries

## fin data

https://www.sifrdata.com/cryptocurrency-correlation-matrix/
fin tillgångar:
TNX: The Chicago Board Options Exchange 10-Year T-Note Index is based on the yield-to-maturity of the
most recently auctioned 10-yr T-note.  The index is calculated by multiplying the T-note YTM by a
factor of 10. Ex: YTM 5.75% x 10 = Index Value of 57.50.


## weekly

.resample('W')

a weekly rebalncing. better results?



## coinsbase index fund

Jämför denna fond med coin base.

## volume graphs

Jobba mer med volume.

Kontrollera att volume är korrekt
