# function (r_exp, vols, numOfPath)
# numofpath sor
import numpy as np

rs = np.array([0.1, 0.05])
vol = np.array([0.2, 0.01])


def returns(r_exp, vols, numOfPath):
    n = len(r_exp)
    yields = np.random.normal(r_exp, vols, [numOfPath, n])
    return yields


print(returns(rs, vol, 10))
