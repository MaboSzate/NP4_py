import pandas as pd

# df_prop = pd.read_csv("property data.csv")
# df_prop['PID'].apply(lambda x: str(x)[:-2])

df = pd.read_excel('stock_test.xlsx')

df_pivot = pd.pivot_table(df, index=['Date'], columns=['Stock'], values=['Price'])
print(df_pivot)

# df.groupby('Stock').mean()

df['Stock Name'] = df['Stock'].apply(lambda x: x[0])

print(df)