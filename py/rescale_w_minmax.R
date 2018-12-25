# save these for fun
# these are not the true scaling functions.

w_truncate < - function(weight_original, minimum=0.01, maximum=0.30)
{
stopifnot(sum(weight_original) == 1)
w1 < - if_else(weight_original > maximum,
             maximum,
             weight_original)
w2 < - if_else(w1 < minimum,
             minimum,
             w1)
return (w2)
}
wexample < - c(0.6, 0.9, 20.5, 50, 28) / 100
w_truncate(wexample)
w_truncate(wexample) * c(1, 1, 0, 0, 0)

w_rescale_minmax < - function(weight_original, minimum=0.01, maximum=0.30)
{
# input: weights, summing to 1.
# output: weights with max 30% and min 1%.
# how it is done:
# distribute leftover percentages to the ones who were not changed
# (do it according to previous weight)

# truncate original weights
w_truncated < - w_truncate(weight_original, minimum, maximum)

# calc what weights are leftovers from truncating.
leftover < - 1 - sum(w_truncated)
unchanged < - as.integer(weight_original == w_truncated)
tot_mcap_unchanged < - sum(w_truncated * unchanged)

# if changed from the truncation,
# take that (so it becomes 30% or 1%)
# if unchanged then distribute leftover in accordance with original market cap
w_final < - if_else(unchanged == 1,
                  w_truncated + leftover * weight_original / tot_mcap_unchanged,
                  w_truncated)
stopifnot(1 == sum(w_final))
return (w_final)

}
