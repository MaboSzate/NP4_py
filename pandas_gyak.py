import pandas as pd

df_tlt = pd.read_csv('TLT.csv')
df_voo = pd.read_csv('VOO.csv')
df_test = pd.read_excel('test.xlsx', sheet_name='Munka1')

# print(df_tlt, df_voo, df_test)

# df_test.to_csv('df_test_output.csv')

df = pd.DataFrame(data={'A': ['F', 4, 'S'],
                        'B': [2, 3, 5]})

# print(df)
#
# print(df_voo.head(3))
# print(df_voo.tail(3))
# print(df_voo.columns)
# print(df_voo.index)
# print(df_voo.dtypes)

# print(df['A'])
# df['C'] = ''
# print(df)
# del df['C']
# print(df)

# df_voo_copy = df_voo.copy()
# df_voo_copy.index = df_voo_copy['Date']
# del df_voo_copy['Date']

df_voo['Volume in 1000s'] = df_voo['Volume'] / 1000
df_voo['Open Close Diff'] = df_voo['Open'] - df_voo['Close']
#print(df_voo)

df_merged = df_voo.merge(df_tlt, how='inner', on='Date', suffixes=('_voo', '_tlt'))
print(df_merged)

df_merged_filtered = df_merged[['Date', 'Adj Close_voo', 'Adj Close_tlt']]
