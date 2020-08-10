# This program uses Monte Carlo simulations to predict the firm's future gross profit
# Requirements are the expected value and expected COGS (Cost of goods sold)

# Monte Carlo simulations: enable observation of different possible realisations of a future event
# We use past data to create a simulation, a new set of fictional but sensible data

# Current Revenues = Last Year Revenues * (1+ y-o-y growth rate)
# The y-o-y growth rate is the unknown, we run 1000 simulations of growth rate, and create an idea of
# maximum, minimum and average growth rates

# Revenues - COGS = Gross Profit

import numpy as np
import matplotlib.pyplot as plt

# Revenue
rev_m = 170

# Revenue standard deviation
rev_stdev = 20
iterations = 1000

# Use the numpy random normal distribution generator to produce simulations of future revenues
rev = np.random.normal(rev_m, rev_stdev, iterations)
print(rev)

plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()

# COGS amount approximately 60% of a company's revenue on average
# And a standard deviation value of 10%
# The negative sign represents money being spent
COGS = - (rev * np.random.normal(0.6, 0.1))
plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()

print(COGS.mean())

# The deviation of COGS will be around 10% of its mean
print(COGS.std())

Gross_Profit = rev + COGS
print(Gross_Profit)

plt.figure(figsize=(15, 6))
plt.plot(Gross_Profit)
plt.show()

print(max(Gross_Profit))

print(min(Gross_Profit))

print(Gross_Profit.mean())

print(Gross_Profit.std())

# Use a histogram to plot the distribution of the output
plt.figure(figsize=(10, 6))
plt.hist(Gross_Profit, bins=20)
plt.show()
