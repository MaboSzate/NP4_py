from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

from opciok import Option

# put-call paritás
K = 360
expiry = "20221215"
C = Option("C", 1, K, expiry)
P = Option("P", -1, K, expiry)

S = 124.35
t = 0.23
vola = 0.3

print(C.calc_price(S, t, vola) + P.calc_price(S, t, vola) - S + K)

spots = range(250, 500, 5)
prices = [C.calc_price(s, 1, vola) for s in spots]
pays = [C.payoff(s) for s in spots]

plt.plot(spots, pays, spots, prices)
plt.show()

