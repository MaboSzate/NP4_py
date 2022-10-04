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
# print(df_voo)

df_merged = df_voo.merge(df_tlt, how='inner', on='Date', suffixes=('_voo', '_tlt'))
print(df_merged)

df_merged_filtered = df_merged[['Date', 'Adj Close_voo', 'Adj Close_tlt']]

df_prop = pd.read_csv('property data.csv')
df_prop_berkeley = df_prop.loc[df_prop['ST_NAME'] == 'BERKELEY']
msk = df_prop['ST_NAME'].isin(['BERKELEY', 'LEXINGTON'])
df_prop_berlex = df_prop.loc[msk,]
print(msk)

msk2 = df_prop['ST_NUM'] < 200
df_prop_smallNum = df_prop.loc[msk2]
msk3 = (df_prop['ST_NUM'] < 200) & (df_prop['ST_NAME'] == 'LEXINGTON')
df_prop_smallNumLex = df_prop.loc[msk3]

mskNAN = df_prop['ST_NUM'].notnull()
df_prop["PID"] = df_prop["PID"].fillna(float('nan'))

df_prop = df_prop.loc[mskNAN]
# print(df_prop)

df_prop_copy = df_prop.copy()
for col in df_prop_copy.columns:
    df_prop_copy[col] = df_prop_copy[col].fillna("NEM JÓ")

# print(df_prop_copy)

df_prop_copy2 = df_prop.copy()
df_prop_copy2 = df_prop_copy2.fillna("FOS")

# print(df_prop_copy2)

df_voo['r_eff'] = df_voo['Adj Close'] / df_voo['Adj Close'].shift(1) - 1
print(df_voo[['Adj Close', 'r_eff']])

import numpy as np

df_voo['log_return'] = np.log(df_voo['Adj Close'] / df_voo['Adj Close'].shift(1))
df_voo['cum_log_return'] = df_voo['log_return'].cumsum()
print(df_voo)

