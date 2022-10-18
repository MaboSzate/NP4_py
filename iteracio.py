import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class VelSzamok:

    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
        self.value = np.random.random([dim1, dim2])

    def atlag(self):
        atlagok = np.mean(self.value, axis=0)
        plt.scatter([range(self.dim2)], atlagok)
        plt.show()


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

matrix = VelSzamok(2, 3)
print(matrix.value)
matrix.atlag()