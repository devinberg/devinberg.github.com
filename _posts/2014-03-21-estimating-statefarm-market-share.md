---
title: Estimating State Farm Market Share
tags: random
category: miscellaneous
permalink: 2014/03/estimating-statefarm-market-share
layout: post
comments: true
---

# Back of the envelope calculations sometimes work out
While driving home the other day I heard a commercial for State Farm insurance (SF) on the radio. They stated in the commercial that they processed 35,000 claims per day. This sounded like a lot so I started to wonder what this meant in terms of how many customers they had. Below is a brief summary of my though process during the rest of the drive as I attempted to work this out in my head.

I started with the number of claims that SF processes a day compared to the US population which I estimated at 350 million (Note: it's actually closer to 318 million [1]). Therefore, I get
\begin{equation}
  \frac{35000}{350000000} = 0.01 \frac{\% of population}{day}
\end{equation}
as an estimation of the percentage of US population making claims per day. Of course this doesn't make sense because it is under the assumption that State Farm has 100% market share. Definitely not the case. So what would could be used to arrive at a semi-realistic estimation? This required some guessing. I estimated now that each person makes 1 claim every 5 years on average. This is probably high but at the time seemed reasonable for a rough estimation. Therefore this would mean that 20% of the population makes a claim every year. Which then means that ~ 0.055% of the population makes a claim per day ($20\frac{\% of population}{year}$ / $365 \frac{days}{year}$).

Now taking our original claims per day number and relating it to the total number of claims per day from my ``1 claim per 5 years" estimate and I get
\begin{equation}
  \frac{0.01 \frac{\% of population}{day}}{0.055 \frac{\% of population}{day}} = 18.18\% \text{market share.}
\end{equation}
Compare this with the actual data [2, 3] where it is reported that State Farm's market share is 18.37% and we see that it is pretty close. Surprisingly close actually but probably more of a coincidence since it all hinged on my guess that on averate each person makes an auto insurance claim once in 5 years. Lucky guess I suppose.



# References
1. [U.S. and World Population Clock](http://www.census.gov/popclock/).
2. [Findthebest.com](http://car-insurance.findthebest.com/q/25/3238/How-big-is-State-Farm-auto-insurance).
3. [Precision Auto Body](http://pabbodyshop.com/2013/04/big-auto-insurers-see-decline-in-market-share/).
