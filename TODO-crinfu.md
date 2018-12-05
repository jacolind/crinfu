# goal driven data anlaysis "hypotes driven"  

decide what anlaysis to do so i do not get stuck in a explorative loop

# next: before irl meeting

## change ggindex() 

either change the f() or use a for loop after it to put stuff info objexts i can use, such as `ret_bsk_mat` and `vol_bsk_mat` to follow naming conventions. 

how to change the f()

### method A 

    w1 = g_basket_weight_mat(mca_vcc_mat, params-describing-index...)
    w2 = g_basket_weight_mat(mca_vcc_mat, params-describing-index...)
    r1, v1 = g_basket_returns(w1, ret_vcc, vol_vcc)
    r2, v2 = g_basket_returns(w2, ret_vcc, vol_vcc)
    ret_bsk_mat = pd.concat([r1, r2], axis=1)
    vol_bsk_mat = pd.concat([v1, v2], axis=1)

### method B 
do like you do now, but let ggindex export the weight matrix if you want, not binary matrix. 
then use some smart pd.concat maybe:

    basket1 = ggindex(mca, vol, ret, params-...)
    basket2 = ggindex(mca, vol, ret, params-...)
    basket3 = and so on 
    baskets = [basket1, basket2, basket3]
    ret_bsk_mat = [b['return'] for b in baskets]
    vol_bsk_mat = [b['volume'] for b in baskets]
    mca_bsk_mat = [b['mcap'] for b in baskets]


## compare indexes 

after fixing ggindex() plot different indexes against each other 

## dead coins

out of those ca 50 coins that has been top10, what is their status now? how many are dead? (first, define dead then count the nr of dead.)

## rollcorr

more thought can be put in here, and do fun stat stuff.

    # plot rolling mean with vol bands. good for mcap or rollcorr plot.
    m = roll.agg(['mean', 'std'])
    ax = m['mean'].plot()
    ax.fill_between(m.index, m['mean'] - m['std'], m['mean'] + m['std'],
                    alpha=.25)
    plt.tight_layout()
    plt.ylabel("Close ($)")
    sns.despine()



## read hodlbot articles 

read hodlbot data analysis and see what should be included for us. 

## download financial data on sp500  clinux 

see file stocks.py

want marketcap on this as well. 


## calc portfolio turnover

it is not calculated correctly now. review the logic. it should be lower.

the correct logic should be like this 

    # w day 1 grows to day 2 with return between day 1 and 2
    # compare w day 2 vs what weights is suggested by market cap
    # the diff needs to be bought 
    # for small supply changes, small trades must be made. 
    # for coinswitches, large trades must be made. 


if asseet z goes from 11 to 10, then weight in z goes from 0% to, say, 2%. assume previous nr 10 asset k had weight of 1%. then we sell 1% of k and buy 2% of z. what is the portfolio turnover?  

> Portfolio turnover is calculated by taking either the total amount of new securities purchased or the amount of securities sold (whichever is less) over a particular period, divided by the total net asset value (NAV) of the fund. The measurement is usually reported for a 12-month time period.
> ...
> If a portfolio begins one year at $10,000 and ends the year at $12,000, add the two together and divide by two to get $11,000. Next, assume the amount of purchases totaled $1,000 and the amount sold was $500. Finally, divide the smaller amount -- buys or sales -- by the average amount of the portfolio. For this example, the smaller amount is the sales. Therefore, divide the $500 sales amount by $11,000 to get the portfolio turnover. In this case, the portfolio turnover is 4.54%.
> / investopedia  

 
     # update weights with return since we have gotten somethign for holding it
     w = w * return
     # calc what you bought and sold 
     bought_sum = sum those with larger w in day 2 than day 1
     sold_sum = sum those with smaller w in day 2 than day 1 
     # defn of turnover 
     turnover = min(bought_sum, sold_sum)
     # https://www.sapling.com/5885771/calculate-portfolio-turnover 
      

also, the code now use a simplified index logic. in reality, if coin nr 11 goes into top 10 then we do not include it immediately - we wait (a) for the coin to marketcap = 2x the others, or (b) for the coin to be top 10 two months in a row. i would chose b because it is more logical.

## coin switches

Visualisera nr of coin switches bättre. Både inom fonden och runtikring top 10 Kommentaren är it's difficult to do this yourself so we provide a service. Det som är runtikring top 10 triggar ett trade event för fonden, eftersom förra 10an är såld helt och flrrau11an köps helt. Kolla då hur mkt vikt 10e platsen har vid varje månad (och gör en describe på den för att se median och kvartiler) för ju större vikt 10an hade desto mer ska säljas av, dvs fonden ändras mkt.


## rolling corr(entiremarket, top200, top10, top5, top1)

Defn variabeln market som är sum of all coins mcap. Gör rolling Corr på dem och BLX och Bitcoin för att se vilket som fångar hela marinaden bäst och hur bra dom fångar. 

# afer irl meeting 

## plot krashes 

a famous youtube video "it went all to x, and then it krashed."
slice out those timeperiods, and make a figure with many plots in it. 


## marketcap na. how to handle? 

marketcap has na. how should we handle it?

i think na.approx() is best.  

when using .reindex do not fill with zero but with na.approx so that we do not see zero return on days when price is NA. 


## output key objects to csv

the objects found in `naming-convention-objects.md` can be exported to csv.

then i can import to R use ggplot instead of `...plot.py` and use shiny to vizualize general index constuction.

one problem: have to research how to make a nice corr plot which is now done with seaborn.

## colors

use these colors:

URL:
http://colorbrewer2.org/?type=diverging&scheme=Spectral&n=5

JavaScript:
['#d7191c','#fdae61','#ffffbf','#abdda4','#2b83ba']
[red, orange, beige, green, blue]
[last_resort, btc, stocks / bonds / xrp / others, eth, blx]


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
