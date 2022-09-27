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
    a_corr = np.dot(a_uncorr, a_l.transpose())
    return a_corr


def test_corr_std_norm():
    corr_mat = [[1.0, -.8], [-.8, 1.0]]
    a_corr = corr_std_norm(corr_mat, 1000)
    print(np.corrcoef(a_corr.transpose()))
test_corr_std_norm()

def corr_norm(corrMat, alfa, sigma, numOfPath):
    a_corr = np.array(corrMat)
    numOfAssets = a_corr.shape[0]
    a_l = np.linalg.cholesky(a_corr)
    a_uncorr = np.random.normal(size=(numOfPath, numOfAssets))
    a_corr = np.dot(a_uncorr, a_l.transpose())
    a_res = a_corr * np.array(sigma) + np.array(alfa)
    return a_res

def test_corr_norm():
    corr_mat = [[1.0, -.8], [-.8, 1.0]]
    alfa = [0.08, .0495]
    sigma = [0.2, 0.1]
    a_res = corr_norm(corr_mat, alfa, sigma, 10000)
    print(np.mean(a_res, axis=0))
    print(np.std(a_res, axis=0))

test_corr_norm()


