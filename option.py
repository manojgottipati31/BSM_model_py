from scipy.stats import norm
from math import log, sqrt, exp

class Option:
    def __init__(self, S, K, r, T, sigma, option_type):
        self.S = S
        self.K = K
        self.r = r
        self.T = T
        self.sigma = sigma
        self.option_type = option_type
        self.price = self.calculate_price()
        self.delta = self.calculate_delta()
        self.gamma = self.calculate_gamma()
        self.vega = self.calculate_vega()
        self.theta = self.calculate_theta()
        self.rho = self.calculate_rho()

    def calculate_price(self):
        d1 = (log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T))
        d2 = d1 - self.sigma * sqrt(self.T)
        if self.option_type == "call":
            price = self.S * norm.cdf(d1) - self.K * exp(-self.r * self.T) * norm.cdf(d2)
        else:
            price = self.K * exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)
        return price

    def calculate_delta(self):
        d1 = (log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T))
        if self.option_type == "call":
            delta = norm.cdf(d1)
        else:
            delta = norm.cdf(d1) - 1
        return delta

    def calculate_gamma(self):
        d1 = (log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T))
        gamma = norm.pdf(d1) / (self.S * self.sigma * sqrt(self.T))
        return gamma

    def calculate_vega(self):
        d1 = (log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T))
        vega = self.S * norm.pdf(d1) * sqrt(self.T)
        return vega

    def calculate_theta(self):
        d1 = (log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T))
        d2 = d1 - self.sigma * sqrt(self.T)
        if self.option_type == "call":
            theta = - (self.S * norm.pdf(d1) * self.sigma) / (2 * sqrt(self.T)) - self.r * self.K * exp(-self.r * self.T) * norm.cdf(d2) + self.r * self.S * norm.cdf(d1)
        else:
            theta = - (self.S * norm.pdf(d1) * self.sigma) / (2 * sqrt(self.T)) + self.r * self.K * exp(-self.r * self.T) * norm.cdf(-d2) - self.r * self.S * norm.cdf(-d1)
        return theta

    def calculate_rho(self):
        d1 = (log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T))
        d2 = d1 - self.sigma * sqrt(self.T)
        if self.option_type == "call":
            rho = self.K * self.T * exp(-self.r * self.T) * norm.cdf(d2)
        else:
            rho = -self.K * self.T * exp(-self.r * self.T) * norm.cdf(-d2)
        return rho

