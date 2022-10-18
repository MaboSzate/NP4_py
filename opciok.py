import numpy as np
from scipy.stats import norm

class Option:
    def __init__(self, right: str, pos: int, strike: float, expiry: str):
        self.right = right  # call/put
        self.pos = pos  # long/short db
        self.strike = strike  # lehivasi arf.
        self.expiry = expiry  # lejarat
        self.vola = np.nan

    def initVola(self):
        self.vola = 0.2

    def calc_price(self, S: float, time_to_exp: float, vola: float, rate=0):
        if not np.isnan(vola):
            IV = vola
        else:
            IV = self.vola if not np.isnan(self.vola) else self.initVola
        if np.isnan(IV):
            print("Vola is not set!")
            return np.nan
        t = time_to_exp
        if t > 0:
            d1 = (np.log(S / self.strike) + (rate + IV ** 2 / 2) * t) / (IV * np.sqrt(t))
            d2 = d1 - IV * np.sqrt(t)
            if self.right == 'C':
                return (S * norm.cdf(d1) - norm.cdf(d2) * self.strike * np.exp(-rate * t)) * self.pos
            else:
                return (norm.cdf(-d2) * self.strike * np.exp(-rate * t) - S * norm.cdf(-d1)) * self.pos
        elif t == 0:
            return self.payoff(S)
        else:
            print("expired!")
            return np.nan

    def payoff(self, spot: float):
        if self.right == 'C':
            return max(spot - self.strike, 0) * self.pos
        elif self.right == 'P':
            return max(self.strike - spot, 0) * self.pos
        else:
            print("Teso call vagy put?")
            return None
