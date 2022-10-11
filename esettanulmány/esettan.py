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



# splitCount = 0
# splitStockName = []
# for i in range(len(prices)):
#     if prices['close'][i] != pricesAdj['close'][i]:
#         splitCount += 1
#         splitStockName.append(prices['symbol'])
#
#
# print(splitCount, splitStockName)
