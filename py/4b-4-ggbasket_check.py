## wei sum to 1

assert (w1.sum(1) < 1 + 0.001).any()
assert (w1.sum(1) > 1 - 0.001).any()

## nr of constituents is 10

b1 = w1>0
assert (b1.sum(1) == 10).all()

##

