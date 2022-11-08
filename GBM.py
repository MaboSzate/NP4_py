from GBM_class import GBPath
import matplotlib.pyplot as plt
import numpy as np
from opciok_class import Option
import pandas as pd

gb = GBPath()

sigma=0.35
N=250
K=1000
spots = gb.generate(sigma,0,K,N,1)
times = np.arange(0,1,1/N)
#plt.plot(times,spots)
# plt.show()

opt = Option("C", 1, K, None)

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

df = pd.DataFrame({"time": times, "spot": spots})


def calc_price(row):
    opt = Option("C", 1, K, None)
    vola = 0.3
    return opt.calc_price(row.spot, 1-row.time, vola)


df["price"] = df.apply(calc_price, axis=1)
df.price.plot()
#plt.show()