import pandas as pd

prices = pd.read_csv('prices.csv')
pricesAdj = pd.read_csv('prices-split-adjusted.csv')
securities = pd.read_csv('securities.csv')


def process_prices(df):
    df['date'] = df['date'].apply(lambda x: x[:10])
    df_filtered = df[['date', 'symbol', 'close']]
    df_pivot = pd.pivot_table(df_filtered, index=['date'], columns=['symbol'], values=['close'])

    print(df_pivot)

process_prices(prices)

# splitCount = 0
# splitStockName = []
# for i in range(len(prices)):
#     if prices['close'][i] != pricesAdj['close'][i]:
#         splitCount += 1
#         splitStockName.append(prices['symbol'])
#
#
# print(splitCount, splitStockName)
