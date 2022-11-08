from GBM_class import GBPath
import matplotlib.pyplot as plt
import numpy as np
from opciok_class import Option

gb = GBPath()

sigma=0.35
N=250
S0=1000
spots = gb.generate(sigma,0,S0,N,1)
times = np.arange(0,1,1/N)
#plt.plot(times,spots)
# plt.show()

opt = Option("C", 1, S0, None)

vola = 0.3
prices = []
deltas = []
for (t,S) in zip(times, spots):
    price = opt.calc_price(S,1-t,vola)
    delta = opt.calcDelta(S,1-t,vola)
    prices.append(price)
    deltas.append(delta)

plt.plot(times, np.array(prices))
plt.show()