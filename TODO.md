# next

Vid import hide errors

read code and delete a lot. some things shoudl be done using functions but have not due to time constraints.

rename some items they have bad names such as fraq_volu... thiis connects to the above point. and it is easier to do if we have it in .py files not .ipynb

see "todo" inside the ipynb

`B_daily = B_monthly.resample('M', method='ffill')` and then use daily data for the fund!
now i have monthly data for the fund. what if we still use monthly re-weights but keep the data in daily format? then B matrix would have to be replicated 30 times for each row. it is more normal to work with dialy data and by doing so we can see how plots change.



# inbox

below are some things i want to do but have not prioritized them into "next"

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





## sifr

https://www.sifrdata.com/category/market-data/ ha med dessa grejer


## ACF PACF - stylized facts

AUTOCORR & EDA: titta på vilka sorts grafer du har gjort i thesis. gör dessa för denna data. kolla tex btc och eth först. hur är ACF och PACF? ser vi samma mönster som i finansdata? se snotes "python time-series"

financial data have some properties (google for "stylized facts of asset returns") such as vol clustering, leverage effect, heavy tails, autocorr, etc. do crypto have this as well.

## fin data

https://www.sifrdata.com/cryptocurrency-correlation-matrix/
fin tillgångar:
TNX: The Chicago Board Options Exchange 10-Year T-Note Index is based on the yield-to-maturity of the
most recently auctioned 10-yr T-note.  The index is calculated by multiplying the T-note YTM by a
factor of 10. Ex: YTM 5.75% x 10 = Index Value of 57.50.

## plot style

testa att ha kvar matplotlib men ändra till

    plt.style.use('seaborn-notebook')
    #styles: ggplot , seaborn-notebook or -talk or -poster

try seaborn?

try this:

    corr_mat = # some code
    sns.clustermap(corr_mat)

## weekly

.resample('W')

a weekly rebalncing. better results?

## coin switches

Visualisera nr of coin switches bättre. Både inom fonden och runtikring top 10 Kommentaren är it's difficult to do this yourself so we provide a service. Det som är runtikring top 10 triggar ett trade event för fonden, eftersom förra 10an är såld helt och flrrau11an köps helt. Kolla då hur mkt vikt 10e platsen har vid varje månad (och gör en describe på den för att se median och kvartiler) för ju större vikt 10an hade desto mer ska säljas av, dvs fonden ändras mkt.

## coinsbase index fund

Jämför denna fond med coin base.

## volume graphs

Jobba mer med volume.

Kontrollera att volume är korrekt
