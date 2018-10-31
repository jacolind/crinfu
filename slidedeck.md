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

## First slide

logo

slogan.

> Don't bet - invest.

# Introduction

## Team

\begin{columns}[onlytextwidth]

  \begin{column}{.5\textwidth}
  image 1, name 1, text 1.

  image 3, name 3, text 3.
  \end{column}

  \begin{column}{.5\textwidth}
  image 2, name 2, text 2.

  image 4, name 4, text 4.
  \end{column}

\end{columns}

## Outline

\tableofcontents

<!--
mabe adjust depth?
-->


# Part I: Why indexing

## Money flow

From active funds to passive funds.

![Net flow into index funds](figures/net-flows-1.png)

## Passive beats active

Trying to beat the market is an unprofitable strategy.

1. active cannot collectivley beat the market
2. sub-groups do not beat their sub-index.
3. winners do not stay winners. see transition matrix and morningstar plot.

## Markovitz


\begin{columns}[onlytextwidth]

  \begin{column}{.5\textwidth}

  Diversification explained.

  \end{column}

  \begin{column}{.5\textwidth}

  \includegraphics{figures/Efficient-Portfolio-Frontier.png}

  \end{column}

\end{columns}

## Indexing in crypto

Most crypto owners only have 1-3 different virtual currencies.

[comment]: # "include the fomo comment When did you buy Ethereum"


# Part II: Why crypto

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

##  Properties of money

Definition of money:

> Money is any item (or verifiable record) that is generally accepted as payment for goods and services and repayment of debts.
> detta är min omskrivning av wikis.

Functions of money:

- Means of exchange.
- Store of value.
- Unit of account.

<!-- beh ej defn dessa iom storyn tidigare med pianisten -->

<!-- jag säger typ: money can be defn in terms of its funciton. anything that satifies these properties can be thought of as money. it follow, then, that some things are more money than others. -->

##  Properties of money

Some things are more money than others.

Properties money should have:

* Scarce: The supply of money in circulation ensures values remain relatively constant.
* Divisible: Can be divided into smaller units of value.
* Fungible: One unit is viewed as interchangeable with another.
* Portable: Individuals can carry money with them and transfer it to others.
* Durable: An item must be able to withstand being used repeatedly.
* ((Accepted: Everyone must be able to use the money for transactions.))
* Uniform: All versions of the same denomination must have the same purchasing power.

<!-- accepted är väl mer en konsekvens än en property? om ngt är accepted så är det per defn money. och saker är ju mer money om det är mer accepted. men det känns logiskt tveksamt att inkludera accepted, för det är ett  cirkulärt argument. därtill är det dåligt för vårt crypto case. -->

texten ovan är från http://money.visualcapitalist.com/infographic-the-properties-of-money/ skriv om eller korta ner elle rbåda.
easy to verify. hard to fake.


##  History of bitcoin

waitinfor sid

2009

2010

2011

##  Properties of bitcoin

<!-- se properties of money och highlihta där bitcoin excels. -->

Properties money should have that bitcon does have

* Scarce: Supply is capped at 21 million
* Low fee: cost 60 cents to move millions of dollars [^bitinfo-fee]
* Portable: bitcoin is borderless
* Divisible: a bitcoin can be divided into 100 million parts. If 1 BTC costs $99,000 then $0.00099 is the lowest value that can be sent.
* Fungible: Yes
* Durable: Yes
* Uniform: Yes

[^bitinfo-fee]: https://bitinfocharts.com/comparison/bitcoin-transactionfees.html

##  Properties of bitcoin

Bonus properties of bitcoin

* Decentralized: Users and miners are spread across the globe, implying that It cannot be shut down as there is no single point of failure => secure.
* Secure: The blockchain has never been hacked. (Merely exchanges and individual accounts, because storing coins safely is difficult.)
* Censorship resistant: It is impossible to prevent a person from sending value to someone else.
* Open source: Actively developed and constantly improving. This improves security since anyone can inspect the code and improve it (or hack it which has not happened)
* Programmable: New solutions such as micropayments, video streaming by the second or other innovations are possible when money is not static but digital.

<!-- the supply of bitcoins will reach 21 million. Today there are ca 16 million and the supply grows by ca 4%.

divisble to 100 million pieces. 1 satoshi.

decentralized: no single point of failure.
censor: impossible to not allow someone to transact
open source : is actively developed and can be audited
 -->

##  note to self

nu har jag nog etablerat att bitcoin kan funka som pengar. nästa steg blir att säga att det finns andra use cases oxå.

##  Different blockchains

- Bitcoin: Digital gold and peer-to-peer digital cash.
- Ethereum: A world computer with smart contracts.
- XRP: Global remittances, fast and cheap.
- Augur: Decentralized prediction market.
- Storj: Rent your hard drive.

<!-- table above illistrate different use cases, they try to solve different provlems.

then I argue that even though two cryptocurrencies try to solve the very same problem (e.g. Bitcoin vs Litecoin or Ethereum vs EOS) there is an equillibrium in which they can co-exists since they differ in their parameters.

lastly i just make a point about communities. btc convervative, ehtereum developers, xrp bank friendly.s
-->

##  Market in numbers: users, exchanges, etc.

##  Historical returns

returns vol table. price graph.

##  Trade and trust (den abstrakta grejen).

vet ej om den platsar.

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

addera mer?


## Cryptocurrencies in a traditional portfolio

<!-- ev. discuss portfolio thinking. -->


![Low correlation between different cryptocurrencies.    Negative correlation between traditional assets and cryptocurrencies.   Thus our certificate can diversify a portfolio.](figures/corr-trad_coins_fund-monthly-annotFalse_smallsize.png)

<!-- then: discuss expansion of effieint frontier, or include the plot i asked håkan to make. -->

## Cryptocurrencies in a traditional portfolio

* TRD: A traditional portfolio with 60% weight in stocks and 40% weights in bonds.
* BLX: BlockchainX certificate, contains the ten largest cryptocurrencies weighted by market capitalization.
* BAL: A balanced portfolio of 95% TRD and 5% BLX. Rebalanced whenever weight in BLX go above 7% or below 3%.

## Cryptocurrencies in a traditional portfolio


\begin{columns}[onlytextwidth]

  \begin{column}{.4\textwidth}

    \begin{table}[retvol-bal]
      \begin{tabular}{|l|l|l|l|}
      \hline
                   & TRD & BLX & BAL \\ \hline
      Return       & 1   & 2   & 3   \\ \hline
      Volatility   & 4   & 5   & 6   \\ \hline
      Return / Vol & 7   & 8   & 9   \\ \hline
      \end{tabular}
    \end{table}

  \end{column}

  \begin{column}{.6\textwidth}

    \includegraphics{figures/weight_BAL.jpg}

  \end{column}

\end{columns}


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

\includegraphics{figures/weight_BAL.jpg}


## An emerging asset class



# Part III: Our product

## Problem: Difficult to buy

Long waiting time

Hours of KYC and AML

Register at several exchanges (to reduce dependency and increase liquidity)

Exchanges have different trading rules, fee structures and user interfaces

<!---
* they would not allow more customer!
-->

## Problem:  Difficult to store

Users (not Euroclear) store their digital assets themselves

Important: -100% return

Complicated: USD 670 million lost during 2018 Q1

<!-- mention mt gox hack BTC 6k. -->

## Problem:  Passive investing requires activity

Assume an investor is both bullish on the crypto market and believe in a passive investment strategy.
What does he have to follow this strategy?

Set up the portfolio:

* Choose or define an index
* Buy coins (on several exchanges)
* Move coins to cold storage (in different wallets)

## Problem:  Passive investing requires activity

To invest a portion of the salary every month:

* Repeat the process of buying and moving to cold storage

To keep his crypto portfolio around 5% of his total portfolio:

* move from cold storage to exchange, sell and move back to cold storage

## Problem:  Passive investing requires activity

To rebalance once a month:

<!-- (in order to own the current market and not what it was at the purchasing date?) -->

* Move from cold storage to exchange
* Buy coins that entered the index
* Sell coins that exited the index
* Rebalance other coins due to supply changes (e.g. new bitcoins have been created)


To follow the law:

* Log all trades and pay 30% capital gains tax on every trade


## Problem:  Passive investing requires activity

Doing it yourself is a mess

## Solution: An exchange traded note


<!--
what i say:

buy it at your broker

do not worry about loss or theft

do not bet on a single project's success, bet on the market.

todo decide if you want to only have the text Simple Secure Diverse.

I like the phrase "do not bet - invest."
-->


**Simple**: Buy it at your current broker

**Secure**: No need to worry about loss or theft

**Diverse**: Do not bet on a single project's success - invest in  the market



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
will be able to buy the BlockchainX certificate

## Benefit 4: Increased trading volume

* NASDAQ miss out on the trading volume in coin 3-10
* New investors
* Old investors


## Product details

below is jus tan outline. i will do slides later after talking with hakan and simon.

* Index
  * Top 10
  * Market capializaiton weighted
    * the weight of each currency is $w_i = m_i / m$ where $m_i$ is the market capitalization of currency $i$ and $m$ is the total market cap for the 10 selected coins
  * Rebalanced monthly
  * Publish index value daily frequency

---

* Certificate
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

etc...

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
