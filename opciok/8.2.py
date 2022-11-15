import numpy as np
import pandas as pd
from opciok_class import Option
import matplotlib.pyplot as plt

df = pd.read_csv("KO.csv")


# Lejáratig lévő idő oszlop

df["date"]=pd.to_datetime(df["date"])
df["expiry"]=pd.to_datetime(df["expiry"])
df["daysToExp"] = (df.expiry - df.date).dt.days
df = df.set_index("date")

# Forward price vs time plot (kvázi spot price)

#df.groupby(df.index).forward_price.median().plot()  # megegyező indexűek fognak egy csoportot alkotni
# plt.show()


def calcVolaMid(row):
    opt = Option(row.cp_flag, 1, row.strike, row.expiry)
    if row.forward_price * row.daysToExp * row.mid > 0:
        return opt.calcVola(row.forward_price, row.daysToExp/365, row.mid)
    else:
        return None


df0 = df[df.index < "2018-03-01"]

df0.loc[:, "impliedVolaMid"] = df0.apply(calcVolaMid, axis=1)

print(df0)

# Egy tetszőleges opció kiválasztása

dates = df0.index.unique()
df_ = df0[df0.index == dates[23]]
df_ = df0[df0.daysToExp == 102]
date = df_.index[0]
df_ = df_[df_.last_date == date]
df_.groupby(df_.strike).impliedVolaMid.median().plot()
plt.show()
