# Markowitz proved the existence of an efficient set of portfolios that provide a higher
# rate of return for the same or even lower risk.
# These portfolios are called the Efficient Frontier.

# He analysed ways to understand how different securities in a portfolio interact with one-another.

# Covariance - measure of the relationship of 2 securities.
# The combination of securities with little correlation allows investors to optimise their return
# without assuming additional risk.

# A positive correlation value means the securities will likely change in the same direction.

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Global variables
trading_days_in_a_year = 250

# Assets composed of Goldman Sachs and the S&P 500
assets = ['GS', '^GSPC']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(
        a, data_source='yahoo', start='2010-1-1')['Adj Close']

print(pf_data.tail())

# Normalise the data to 100
(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))
# plt.show()

log_returns = np.log(pf_data / pf_data.shift(1))

# Average returns
log_returns.mean() * trading_days_in_a_year

# Covariance
log_returns.cov() * trading_days_in_a_year

# Correlation
# Correlation = 0.762081, this is bigger than 0.3, meaning the returns are well-correlated
log_returns.corr()
print(log_returns.corr())

# Number of assets
num_assets = len(assets)

# Generate 2 random weights
arr = np.random.random(2)
print(arr)

# Generate 2 random weights with the sum equaling 1
weights = np.random.random(num_assets)
weights /= np.sum(weights)
print(weights)
print(weights[0] + weights[1])

# Expected portfolio return
expected_portfolio_return = np.sum(
    weights * log_returns.mean()) * trading_days_in_a_year
print('expected_portfolio_return: ' + str(expected_portfolio_return))

# Expected portfolio variance
expected_portfolio_variance = np.dot(weights.T, np.dot(
    log_returns.cov() * trading_days_in_a_year, weights))
print('expected_portfolio_variance: ' + str(expected_portfolio_variance))

# Expected portfolio volatility, the formula for standard deviation
expected_portfolio_volatility = np.sqrt(
    np.dot(weights.T, np.dot(log_returns.cov() * trading_days_in_a_year, weights)))
print('expected_portfolio_volatility: ' + str(expected_portfolio_volatility))

# The simulation will generate 1000 different combinations of weight values of the assets, and select the most efficient
pfolio_returns = []
pfolio_volatilities = []

for x in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(
        np.sum(weights * log_returns.mean()) * trading_days_in_a_year)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(
        log_returns.cov() * trading_days_in_a_year, weights))))

print('pfolio_returns:\n' + str(pfolio_returns))
print('pfolio_volatilities:\n' + str(pfolio_volatilities))

# Modify the lists into numpy arrays for further usability when plotting the Efficient Frontier
pfolio_returns = []
pfolio_volatilities = []

for x in range(1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(
        np.sum(weights * log_returns.mean()) * trading_days_in_a_year)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(
        log_returns.cov() * trading_days_in_a_year, weights))))

pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

print('pfolio_returns:\n' + str(pfolio_returns))
print('pfolio_volatilities:\n' + str(pfolio_volatilities))

portfolios = pd.DataFrame(
    {'Return': pfolio_returns, 'Volatility': pfolio_volatilities})
print(portfolios.head())
print(portfolios.tail())

portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6))
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.show()
