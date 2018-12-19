# 20181128 no more long format 

here is what i previously put into the todo.md 

    ## `dfl_indexes` and `dfl_ vcc` concated
    
    Insert column on which coins are included in the certain date, and their weight (can be a dict inside the column with symbol w dictionary). And save as long format after the ggindex is done. 
    
    Add column asset type Index (to contrast it with vcc or fin). Maybe concat to dfl vcc and rename to dfl. Then concat fin and call it asset type traditional.
    
    
    ## long format 
    
    i cannot make ggindex() work on long form data because pandas is inferior to dplyr when it comes to this. however, i can convert to wide, apply ggindex() to create objects, and then convert to long format for storage. 
     
    pro with long format is that i will not have to create many objects and keep track of them with naming, since everything is stored in a large `dfl` object that can be accessed by .query 
    
    or apply ggindex on wide and then save to long after. 

but this is not my plan anymore. as i wrote in dflong.py

> aborted this idea 20181128 1524. i prefer wide. we can wait with fancy shiny apps. long format is needed for fancy shiny with ggindex, but for simple apps wide format is fine. it is also easier to reason analyticallya bout. i will do wide format in python with naming

# portfolio turnover notes 

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

# 