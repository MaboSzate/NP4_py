import numpy as np


class GBPath:
    def __init__(self):
        pass

    def generate(self,sigma,mu,S0,N,T):
        # dS = mu*S*dt + sigma*S*dWt
        # S(t+dt) = S(t)*exp((mu-sigma^2/2)*dt + sigma*sqrt(dt)
        dt = T/N
        X = np.exp((mu-sigma**2/2)*dt) + sigma * np.random.normal(0, np.sqrt(dt), N)
        return S0*np.cumprod(X)
