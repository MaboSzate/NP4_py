import pandas as pd
import numpy as np

df = pd.DataFrame(range(1, 21), columns=['n'])
df = df.set_index('n')
df['fib'] = np.nan
# df.loc[df.index == 1, 'fib'] = 1
# df.loc[df.index == 2, 'fib'] = 1

for idx, row in df.iterrows():
    if idx in [1, 2]:
        df.loc[idx, 'fib'] = 1  # elso ket sort 1-re állítjuk
    else:
        df.loc[idx, 'fib'] = df.loc[idx-1, 'fib'] + df.loc[idx-2, 'fib']

print(df)