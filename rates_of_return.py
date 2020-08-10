import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Global variables
trading_days_in_a_year = 250

PG = wb.DataReader('GS', data_source='yahoo', start='1995-1-1')
print(PG.head)
print(PG.tail)

# Formula for Simple Rate of Return:
# (P1 - P0) / P0 = P1/P0 - 1

# Create a new column in PG for the simple rate of return
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])

# Plot the simple return value
# The plot shows a high loss of close to 20% in a day in 2008/9
PG['simple_return'].plot(figsize=(8, 5))
plt.show()

# Average daily return
avg_returns_d = PG['simple_return'].mean()
print(avg_returns_d)

# Average annual return
avg_returns_a = PG['simple_return'].mean() * trading_days_in_a_year
print(avg_returns_a)

print(str(round(avg_returns_a, 5) * 100) + ' %')
