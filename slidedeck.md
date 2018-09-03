---
Title: Slide deck
Author: Vinter Capital
---

## note  to the reader

this is a super early draft of the structure, content and design of the slidedeck.

the slidedeck is a subset of the whitepaper.

## todo

pröva --- i "added benefits".

## First slide

logo

slogan

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

theoreical:

- active cannot collectivley beat the market

empirical:

- sub-groups do not beat their sub-index
- winners do not stay winners. see transition matrix and morningstar plot.

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

## story

very compelling story

## facts

numbers on usage, market cap and returns.

## communities

every virtual currency is like its own community

## the case for crypto in an inst portf

5% allocation, tolerannce 3-7%, increase sharpe ratio from this to that.

# Part III: Our product

## Difficult to buy

so hard

many exchanges

much sweat

## Difficult to store

so complex

theft

## Passive investing requires activity

all that rebalancing

## Solution: A certificate

(i) Simple

(ii) Secure

(iii) Diverse

## Added benefits

1. Lower taxes
2. Capitalizing on chain events
3. Increased invested capital
4. Increased trading volume

## 1: Lower taxes

Tax on every crypto trade

vs

Tax on 1.5% of AUM

## 2: Capitalizing on chain events


| Chain event |  Stock event |
| ------------| ---------------------|
| Air-drops |  Dividends             |
| Staking   |  Stock lending    |
| Hard fork |  De-merger             |

Economies of scale

## 3: Increased invested capital

Many investors who cannot buy today for legal or technical reasons will be able to buy the BlockchainX certificate.

## 4: Increased trading volume

- Capture more volume
- New investors
- Old investors

## another method

above I tried to fix an "issue" that the whitepaper has a section depth which is deeper than what is allowed for slides. structure is important and should be kept. but how do you keep the structure yet make it visually appealing? the above solution was one way to do it. below is another way of doing it.


## Added benefits

(1) Lower taxes

(2) Capitalizing on chain events

(3) Increased invested capital

(4) Increased trading volume


## Added benefits

(1) Lower taxes

Tax on every crypto trade

vs

Tax on 1.5% of AUM

## Added benefits


(2) Capitalizing on chain events


| Chain event |  Stock event |
| ------------| ---------------------|
| Air-drops |  Dividends             |
| Staking   |  Stock lending    |
| Hard fork |  De-merger             |

Economies of scale


## Added benefits


(3) Increased invested capital

Many investors who cannot buy today for legal or technical reasons will be able to buy the BlockchainX certificate.


## Added benefits


(4) Increased trading volume

- Capture more volume
- New investors
- Old investors


## now back to the content again

## Product details

* Index
  * Top 10
  * Market capializaiton weighted
    * the weight of each currency is $w_i = m_i / m$ where $m_i$ is the market capitalization of currency $i$ and $m$ is the total market cap for the 10 selected coins i.e. $m = \sum_{i=1}^10 m_i$
  * Rebalanced monthly
  * Daily frequency
* Hedging
* Storage solution
* stuff from hakan and simons texts.

For details, read our Whitepaper.

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

```
hakan@vinter.capital
jacob@vinter.capital
leopold@vinter.capital
marco@vinter.capital
simon@vinter.capital
tim@vinter.capital
name-of-cto@vinter.capital
```

## Whitepaper

For more in-depth content read our whitepaper
`www.vintercapital.com/whitepaper`

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
