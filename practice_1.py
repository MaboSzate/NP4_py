import numpy as np
import seaborn as sns


def uncorr_returns(r_exp, vols, numOfPath):
    n = len(r_exp)
    r_exp = np.array(r_exp)
    vols = np.array(vols)
    alfa = r_exp - vols * vols / 2
    returns = np.random.normal(alfa, vols, [numOfPath, n])
    return returns


def test_uncorr_reutrns():
    rs = [0.1, 0.05]
    vol = [0.2, 0.01]
    print(uncorr_returns(rs, vol, 10))
#test_uncorr_reutrns()


def corr_std_norm(corrMat, numOfPath):
    a_corr = np.array(corrMat)
    numOfAssets = a_corr.shape[0]
    a_l = np.linalg.cholesky(a_corr)
    a_uncorr = np.random.normal(size=(numOfPath, numOfAssets))
    z = (np.matmul(a_l, a_l.transpose()))

    pass


def test_corr_std_norm():
    corr_mat = [[1.0, -.8], [-.8, 1.0]]
    print(corr_std_norm(corr_mat, 1000))

test_corr_std_norm()
