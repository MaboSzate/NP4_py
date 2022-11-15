import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Függvény a kock. mentes kamatláb előhívására


def getDailyRiskFreeRate():
    df = pd.read_csv("DTB3.csv")
    df.index = pd.to_datetime(df["DATE"])
    df = df[["DTB3"]]
    df.columns = ["riskFreeDaily"]
    msk = df["riskFreeDaily"] != "."  # adathiba kiszedése
    df = df[msk]
    df = df.astype(float)
    df = df / 252
    return df


dfRiskFree = getDailyRiskFreeRate()
df = pd.read_csv("BRK-B.csv")
df.index = pd.to_datetime(df["Date"])

# Kettő df joinolása

dfJoin = df.join(dfRiskFree)


# Log return, excess return:
dfJoin["LogReturn"] = np.log(dfJoin["Adj Close"] / dfJoin["Adj Close"].shift(1))
dfJoin["ExcessReturn"] = dfJoin["LogReturn"] - dfJoin["riskFreeDaily"]

# Rolling Volatily különböző ablakokra:

volWindowsInYear = [0.25, 1, 3, 10]
daysInYear = 252
colsVol = []

for year in volWindowsInYear:
    col = "RollingVolatility_" + str(year) + "y"
    colsVol.append(col)
    dfJoin[col]= np.sqrt(daysInYear) * dfJoin['LogReturn'].rolling(int(year * daysInYear)).std()

plt.show()
# Rolling Average különböző ablakokra

colsAvg = []
for year in volWindowsInYear:
    col = "RollingAvg_" + str(year) + "y"
    colsAvg.append(col)
    dfJoin[col]= daysInYear * dfJoin['LogReturn'].rolling(int(year * daysInYear)).mean()






dfJoin[["LogReturn", "RollingVolatility_1y", "RollingAvg_1y"]].plot()
plt.show()