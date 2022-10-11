import pandas as pd


prices = pd.read_csv('prices.csv')
pricesAdj = pd.read_csv('prices-split-adjusted.csv')
securities = pd.read_csv('securities.csv')


def process_prices(df):
    df['date'] = df['date'].apply(lambda x: x[:10])
    df_filtered = df[['date', 'symbol', 'close']]
    df_pivot = pd.pivot_table(df_filtered, index=['date'], columns=['symbol'], values=['close'])
    df_pivot.columns = df_pivot.columns.droplevel()
    return df_pivot


prices_processed = process_prices(prices)
pricesAdj_processed = process_prices(pricesAdj)

def add_effective_return(df):
    df_out = pd.DataFrame()
    for col in df.columns:
        df_out[col + '_eff'] = df[col] / df[col].shift(1) - 1
    return df_out


prices_processed_with_returns = add_effective_return(prices_processed)
pricesAdj_processed_with_returns = add_effective_return(pricesAdj_processed)

merged = prices_processed_with_returns.merge(pricesAdj_processed_with_returns, on='date',
                                             suffixes=('_normal', '_adjusted'))

symbols = prices_processed.columns
splits = []

for symbol in symbols:
    df_symbol = merged[[symbol + "_eff_normal", symbol + "_eff_adjusted"]]
    diff_array = df_symbol[symbol + "_eff_normal"] - df_symbol[symbol + "_eff_adjusted"] > 0.001
    if len(df_symbol.loc[diff_array]) > 0:
        splits.append(symbol)

print(splits, len(splits))

import numpy as np


def add_log_return(df):
    df_out = pd.DataFrame()
    for col in df.columns:
        df_out[col] = np.log(df[col] / df[col].shift(1))
    return df_out


priceAdj_log = add_log_return(pricesAdj_processed)
return_dict = {}
for col in priceAdj_log.columns:
    col_notnull = priceAdj_log.loc[priceAdj_log[col].notnull(), col]
    yearly_return = 255 * col_notnull.mean()
    return_dict[col] = yearly_return

securities['yearly_return'] = securities['Ticker symbol'].map(return_dict)

sector_avg_returns = securities.groupby('GICS Sector').mean(numeric_only=True)
print(sector_avg_returns)

filtered = priceAdj_log[['A']]
filtered['cumsum'] = filtered.cumsum()
print(filtered)

import matplotlib.pyplot as plt

filtered['cumsum'].plot()
plt.show()

