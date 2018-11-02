# next


## index and cols

see the printout of `tranform-check`. it is not very rigourous, some matrices have more cols/rows than others.
this is due to importing. it can be fixed. i am not sure now how much all results are affected.

## portfolio turnover

it is not calculated correctly now. review the logic. it should be lower.

also, the code now use a simplified index logic. in reality, if coin nr 11 goes into top 10 then we do not include it immediately - we wait (a) for the coin to marketcap = 2x the others, or (b) for the coin to be top 10 two months in a row. i would chose b because it is more logical.

## reduce cols?

it might also be worthwile to let `ret_mat` only contain `tkr_beeninblx` (the tickers that have been in the blx certificate) since it reduces the nr of cols from 1500+ to ca 50. it improves the speed an memory.

that is dony by creating mca matrix, then binary matrix, then creating list of tickers that has been in the fund, then `ret_mat = ret_mat[tkr_beeninblx]`.

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


## aum start at 100

ev do a quickfix by prepending a row of 100 for all assets.

## sifr

https://www.sifrdata.com/category/market-data/ ha med dessa grejer

## choose colors, and plot themes.

### plot style

testa att ha kvar matplotlib men ändra till

    plt.style.use('seaborn-notebook')
    #styles: ggplot , seaborn-notebook or -talk or -poster

try seaborn?

try this:

    corr_mat = # some code
    sns.clustermap(corr_mat)


## dead coins

out of those ca 50 coins that has been top10, what is their status now? how many are dead? (first, define dead then count the nr of dead.)

## rollcorr

more thought can be put in here, and do fun stat stuff.


## B daily

`B_daily = B_monthly.resample('M', method='ffill')` and then use daily data for the fund!
now i have monthly data for the fund. what if we still use monthly re-weights but keep the data in daily format? then B matrix would have to be replicated 30 times for each row. it is more normal to work with dialy data and by doing so we can see how plots change.
detta bör göras så att fundret by defn är månatlig. i binarizer kan man välja resample freq. fundera bara igenom vilken ordning det blir dvs det du gjorde i excelfilen med sumproduct, vilken vikt blir var?
^^ är detta done?


## coin switches

Visualisera nr of coin switches bättre. Både inom fonden och runtikring top 10 Kommentaren är it's difficult to do this yourself so we provide a service. Det som är runtikring top 10 triggar ett trade event för fonden, eftersom förra 10an är såld helt och flrrau11an köps helt. Kolla då hur mkt vikt 10e platsen har vid varje månad (och gör en describe på den för att se median och kvartiler) för ju större vikt 10an hade desto mer ska säljas av, dvs fonden ändras mkt.








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
