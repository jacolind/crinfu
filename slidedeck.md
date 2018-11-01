---
Title: Slide deck
Author: Vinter Capital
terminal path: PS1='\u:\W\$ '
pandoc: pandoc -t beamer slidedeck.md -V theme:Dresden -o slidedeck.pdf
---


## note  to the reader

this is a super early draft of the structure, content and design of the slidedeck.

the slidedeck is a subset of the whitepaper.

as of 20180908:

> Part III is done. Everything else is not done.
>
> Part III is written not in a minimalist style (so that I maximze the amount of attention the listener has to the presenter). Instead, I have included an amount of text that makes it possible for the listener to revisit the slides and comprehend what was said. Also, with the current content I feel comfortable sitting down and pitching without too much training yet feel like I will be able to say everything that should be said. When I have trained more, and the content is in my brain, I will be able to reduce the amount of content - if that is what we want - and still feel comfortable. Let's discuss over the phone what choices to make regarding how much content to write.

## todo

graph of passive should be done by ous. take the data from the plot.  just a few lines of python.

make net-flows-1.png on your own in python to make it look good.

select of make table for historical returns.

todo setup contact@vinter.capital

add details to roadmap

add product details. me / sid / hakan.

redraw corr plot with BlockchainX not Fund as the name.

---

ha en competitor slide med bitwise, xbt, oss. man kan ju förklara oss som fusionen mellan bitwise och xbt.

team slide kanske ska ligga i slutet. när man pratar om competion vs us och vår roadmap.
typ 1) competition och vrf vår produkt är bättre 2) road map dvs hur vi ska göra 3) vi som ska utföra roadmap ,dvs vi kan göra det.

jag tror man ska ha en juridisk slide som övertygare path from today to listed at nasdaq.
varför kommer just vi kunna llista? för att xbt gjort grundjobbet.

---

obesvarade / oklara punkter enligt AL:
- Hur ni tjänar pengar
- Hur listas ni?
- Varför skulle ni listas?
- Även om ni listas, hur får vi noobs som köper på coinbase nu att köpa vårt cert?


## First slide

\maketitle

---

\includegraphics{figures/vinterCapitalLogo.jpg}

# Introduction

## Team

todo copy from web

\begin{columns}[onlytextwidth]

  \begin{column}{.5\textwidth}
  1, name 1, text 1.

  3, name 3, text 3.
  \end{column}

  \begin{column}{.5\textwidth}
  2, name 2, text 2.

  4, name 4, text 4.
  \end{column}

\end{columns}

## Outline

\tableofcontents

<!--
mabe adjust depth?
-->


# Part I: Why indexing

## Money flow

![Net flow from active to passive.](figures/net-flows-1.png)

## Passive beats active

Trying to beat the market is an unprofitable strategy, as shown by academia. 

<!-- kanske ha citat från jensen eller fama. eller har ref till många artiklar. -->

<!-- 1 is logic and math. 2 is empirics, and is intuitive.  3 is empirics, see transition matrix and morningstar plot. -->

## Markovitz

![Diversification stems from correlation and it increases the risk adjusted returns.](figures/Efficient-Portfolio-Frontier.png)

## No indexing in cryptocurrencies

Most cryptocurrency owners only have 1-3 different coins.

[comment]: # "include the fomo comment When did you buy Ethereum"


# Part II: Why cryptocurrency

##  The internet of money

Bitcoin is fast, cheap, global payment.

Cryptocurrencies will do to value what the internet did to information.

Email was the first real use case of the internet.

Payment is the first real world use case of cryptocurrencies.

<!-- give more Similarities betwen email, internet and bitcoin.
* Bitcoin is fast cheap global mobile payment.
* Email was the first real application of the internet. Payments is the first real application of cryptocurrencies and blockchain technology.
* Another similarity between bitcoin and email is that if you know someones email or bitcoin adress then you can send them information or value instantly across the globe, but it can only be sent if your password or private key.
-->

Different cryptocurrencies have different use cases, and multiple winners will emerge - but which ones?

##  History of money

1. It had to be invented for trade.
2. Commodity money: seashells, knifes, cows, alcohol, and coins of gold or silver.
3. Representative money: paper in china.
4. Gold standard: paper backed by gold.
5. Fiat money: paper without intrinsic value.

Throughout history we have used many forms of money.

##  Properties of money

Definition of money:

> Money is any item (or verifiable record) that is generally accepted as payment for goods and services and repayment of debts.

Functions of money:

- Means of exchange.
- Store of value.
- Unit of account.

<!-- beh ej defn dessa iom storyn tidigare med pianisten -->

<!-- jag säger typ: money can be defn in terms of its funciton. anything that satifies these properties can be thought of as money. it follow, then, that some things are more money than others. -->

##  Properties of money

Properties money should have:

- Durable: can withstand repeated use.
- Divisible: can be divided to make smaller payments.
- Portbale: can be carried by one person and tranfered to others.
- Fungible: each unit is interchangeable.
- Uniform: each unit have the same value.
- Scarce: limited supply so its value does not fall.

Some things are more money than others.

<!--
texten ovan är från http://money.visualcapitalist.com/infographic-the-properties-of-money/ skriv om eller korta ner elle rbåda.
easy to verify. hard to fake.

-->

<!-- accepted är väl mer en konsekvens än en property? om ngt är accepted så är det per defn money. och saker är ju mer money om det är mer accepted. men det känns logiskt tveksamt att inkludera accepted, för det är ett  cirkulärt argument. därtill är det dåligt för vårt crypto case. -->



##  History of bitcoin

waitinfor sid

2009

2010

2011

##  Properties of bitcoin

<!-- se properties of money och highlihta där bitcoin excels. -->

Properties money should have that bitcon does have:

* Durable: It can be used an infinite amount of times.
* Divisible: each bitcoin can be divided into 100 million parts. <!-- If 1 BTC costs $99,000 then $0.00099 is the lowest value that can be sent.-->
* Portable: bitcoin is borderless.
* Fungible: all units are interchangeable.
* Uniform: all units have the same value.
* Scarce: Supply is capped at 21 million

<!-- source on fee https://bitinfocharts.com/comparison/bitcoin-transactionfees.html -->

##  Properties of bitcoin

Bonus properties of bitcoin:

* Low fee: costs $0.60 to move millions of dollars.
* Decentralized: No single point of failure.
* Secure: Everybody can see the code, and the bitcoin has never been hacked.
* Censorship resistant: Anyone can send and recieve value.
* Open source: Actively developed with new features.
* Programmable: New solutions such as micropayments, video streaming by the second and other future innovations.

<!-- these points connects to each other.
securty & open source.
programmable & open source.
-->


<!-- the supply of bitcoins will reach 21 million. Today there are ca 16 million and the supply grows by ca 4%.

divisble to 100 million pieces. 1 satoshi.

decentralized: no single point of failure.
censor: impossible to not allow someone to transact
open source : is actively developed and can be audited
 -->

##  Note to self

nu har jag nog etablerat att bitcoin kan funka som pengar. nästa steg blir att säga att det finns andra use cases oxå.

##  Different blockchains

Different use cases and communities.

- Bitcoin: Digital gold and peer-to-peer digital cash.
- Ethereum: A world computer with smart contracts.
- Ripple: Global remittances, fast and cheap.
- Augur: Decentralized prediction market.
- Storj: Rent your hard drive.

Which of these will dominate?

<!-- table above illistrate different use cases, they try to solve different provlems.

then I argue that even though two cryptocurrencies try to solve the very same problem (e.g. Bitcoin vs Litecoin or Ethereum vs EOS) there is an equillibrium in which they can co-exists since they differ in their parameters.

then i just make a point about communities. btc convervative, ehtereum developers, xrp bank friendly.

lastly i make a point that we do not know who will win
-->





<!--
##  Market in numbers

- Total market capitalization of all cryptocurrencies: qq as of yyyy-mm-dd
- Nr of users
- Nr of coins
- Trading volume for qq largest exchanges during Oct 2018 was USD qq million.

##  Historical returns

returns vol table. price graph.

todo select table or graph.

-->




##  Trade and trust

Why are cryptocurrencies useful?

1. Trust is needed for trade.
2. Today we use trusted third parties.
3. A blockchain digitize trust.

<!--
##  Myths and counter arguments

- Volatile
- Bubble
- Illegal activity
- No intrinsic value
- It does not work today
- Bitcoin was hacked
- Miners control bitcoin
- Bitcoin is bad for the environment
- It is a pyramid/ponzi scheme
- Supply of 21 million is not enough
- Governments can shut it down

todo addera mer?

-->

## Cryptocurrencies in a traditional portfolio

<!-- ev. discuss portfolio thinking. -->

<!---
Low correlation between different cryptocurrencies.
Negative correlation between traditional assets and cryptocurrencies.
Thus our certificate can diversify a portfolio.
-->

![Our certificate is a diversifier.](figures/corr-trad_coins_fund-monthly-annotFalse_smallsize.png)

<!-- then: discuss expansion of effieint frontier, or include the plot i asked håkan to make. -->

## Cryptocurrencies in a traditional portfolio

Compare three portfolios:

* BLX: Our BlockchainX certificate, contains the 10 largest cryptocurrencies weighted by market capitalization.
* TRD: A traditional portfolio with of 60% stocks and 40% bonds.
* BAL: A balanced portfolio of 95% TRD and 5% BLX.

<!-- or add the info about rebalancing as a footnote in the retunrs table. -->

## Cryptocurrencies in a traditional portfolio

\begin{table}[retvol-bal]
	\begin{tabular}{|l|l|l|l|}
	\hline
							 & TRD & BLX & BAL \\ \hline
	Return       & 1   & 2   & 3   \\ \hline
	Volatility   & 4   & 5   & 6   \\ \hline
	Return / Vol & 7   & 8   & 9   \\ \hline
	\end{tabular}
\end{table}

Details:

- BLX is rebalanced monthly.
- TRD is rebalanced when weight in stocks is >65% or <55%.
- BAL is rebalanced when weight in BLX  is >7% or <3%.
- Time period is yyyy-mm to yyyy-mm.


## An emerging asset class

Low corrlation with stocks and bonds.

Value is driven by different fundamentals than other asset classes.

How will it behave during a financial crisis?

# Part III: Our product

## Problem: Difficult to buy

Long waiting time.

Hours of KYC and AML.

Register at several exchanges (to reduce dependency and increase liquidity).

Exchanges have different trading rules, fee structures and user interfaces.

<!---
* they would not allow more customer!
-->

## Problem:  Difficult to store

Users (not Euroclear) store their digital assets themselves.

Important: -100% return.

Complicated: USD 670 million lost during 2018 Q1.

<!-- mention mt gox hack BTC 6k. -->

## Problem:  Passive investing requires activity

Assume an investor is both bullish on the crypto market and believe in a passive investment strategy.
What does he have to do?

To set up the portfolio:

* Choose or define an index.
* Buy coins (on several exchanges).
* Move coins to cold storage (in different wallets).

## Problem:  Passive investing requires activity

To invest a portion of the salary every month:

* Repeat the process of buying and moving to cold storage.

To keep his crypto portfolio around 5% of his total portfolio:

* move from cold storage to exchange, sell and move back to cold storage.

## Problem:  Passive investing requires activity

To rebalance once a month:

<!-- (in order to own the current market and not what it was at the purchasing date?) -->

* Move from cold storage to exchange.
* Buy coins that entered the index.
* Sell coins that exited the index.
* Rebalance other coins due to supply changes (e.g. new bitcoins have been created).


To follow the law:

* Log all trades and pay 30% capital gains tax on every trade.


## Problem:  Passive investing requires activity

Doing it yourself is a mess.

## Solution: An exchange traded note


<!--
what i say:

buy it at your broker

do not worry about loss or theft

do not bet on a single project's success, bet on the market.

todo decide if you want to only have the text Simple Secure Diverse.

I like the phrase "do not bet - invest."
-->


**Simple**: Buy it through your existing broker.

**Secure**: We secure the assets, no need to worry about loss or theft.

**Diverse**: Do not bet on a single asset - invest in the market.



<!--
## Solution: An exchange traded note

page x : Add where an investor can buy the certificate and how easy it will be etc. Really walk trough the investor experience and compare allocated time, fee's and skill needed between the products in a last slide. Like 3 min to setup and start to trade BLX and X months to do the other. Do the comparison like this :


      BLX	 CRYPTO EXCHANGES
Time
Fee's
Skill
etc.
-->


## Added benefits

1. Lower taxes
2. Capitalizing on blockchain events
3. Increased invested capital
4. Increased trading volume

## Benefit 1: Lower taxes

**Cryptocurrencies**: Investor is taxed 30% on capital gains tax for every single crypto trade (!) both crypto-to-fiat and crypto-to-crypto.

**Certificate**: Investor is taxed less than 0.5% of asset under management in an ISK.

## Benefit 2: Capitalizing on blockchain events

Economies of scale

| Blockchain event |  Stock event |
| ------------| ---------------------|
| Air-drops |  Dividends             |
| Staking   |  Stock lending    |
| Hard fork |  De-merger             |


## Benefit 3: Increased invested capital

Many investors who cannot buy today \newline
(for legal or technical reasons) \newline
will be able to buy the BlockchainX certificate.

## Benefit 4: Increased trading volume

Our certificate attracts both new and old investors.

NASDAQ miss out on the trading volume in coin 3-10 so they have an incentive to list our product.

## Product details

below is jus tan outline. i will do slides later after talking with hakan and simon.

* Index
  * Rebalanced monthly.
  * Publish index value daily frequency.
  * Market capializaiton weighted, i.e. the weight of each asset is equal to its market capitalization divided by the total market cap for the 10 selected assets.

---

* Certificate
  * Fee 2.5% on asset under management
  * Traded throughout the day
  * Delivered T+2
  * ETN is a promise
  * Hedged immediately

---

* Storage solution
  * Buy on exchange,
  * send to cold storage.
* more stuff from hakan and simons texts.

---

For details, read our [Whitepaper][url-whitepaper]

[url-whitepaper]: https://vinter.capital/whitepaper

# Epilogue

## Road map

1. Investment
2. Finansinspektionen
3. NASDAQ

todo add here!

## Ask

## Questions & Answers

<!-- Empty slide -->

# Appendix

## Contact

[contact@vinter.capital](mailto:contact@vinter.capital)

## Whitepaper

For more in-depth content read

[www.vinter.capital/whitepaper][url-whitepaper]

## technical stuff

graphs, etc

## common question 1

data to back up our answer to common question

## common question 2

graph to back up our answer to common question



## pandoc

run the code below to get all pdf's. make sure last row has no `;`

```
pandoc -t beamer slidedeck.md -V theme:Madrid -o slidedeck_Madrid.pdf;
pandoc -t beamer slidedeck.md -V theme:Berkeley -o slidedeck_Berkeley.pdf;
pandoc -t beamer slidedeck.md -V theme:Dresden -o slidedeck_Dresden.pdf;
pandoc -t beamer slidedeck.md -V theme:Ilmenau -o slidedeck_Ilmenau.pdf;
pandoc -t beamer slidedeck.md -o slidedeck_default.pdf
```

Dislike and tested:
Montepiller

My favorites right now are  Berkeley, Dresden.
Ilmenau is similar to dresden but with more color on the boxes.
But I want to include slide numbers as well.

```
pandoc -t beamer slidedeck.md -V theme:Dresden -o slidedeck_Dresden.pdf

pandoc -t beamer slidedeck.md -V theme:Berkeley -o slidedeck_Berkeley.pdf
```

## pandoc 2

adding numbers. did not work for me

```
\addtobeamertemplate{navigation symbols}{}{%
    \usebeamerfont{footline}%
    \usebeamercolor[fg]{footline}%
    \hspace{1em}%
    \insertframenumber/\inserttotalframenumber
}
```
