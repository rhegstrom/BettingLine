# -*- coding: utf-8 -*-
"""
attached is a file of the first 8 weeks of the NFL season.  

Columns are week, visit team, home team, the line 

(first entry is DAL at TB the betting line is -7.5, that means bookmakers expect if a large number of games were played between DAL and TB, at TB, the average difference 
 in scores would be Tampa Bay to win by 7.5.  The last column is the actual difference; in this case TB actually won by 2.   

Line 12  CLE at KC- the betting line is -8.  That means that the bookmakers expect, on average, KC would win by 8   The average difference in score CLE - KC would be 8.  
So the betting line is KC-8.  And it turned out that KC LOST the game by 4.
Using the data in the .csv file, construct a linear model:  actual score = b0 + b1* line

If the bookmakers were perfect, b0 would be 0 and b1 would be 1.

Interpret the results.  Is b0 significantly different from 0?    Is b1 significantly different from 1?

What does this mean about betting line in the NFL?
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ds = pd.read_csv('lineVSactual.csv')

BL = ds['line']     # Line rows
BA = ds['actual']   # Actual rows
errors = BA - BL

meanError = np.mean(errors)
stdError = np.std(errors)

normalApprox = np.random.normal(meanError, stdError, 1000)

plt.hist(ds['line'], alpha=0.5, density=True, label='line')
plt.hist(ds['actual'], alpha=0.5, density=True, label='actual')
plt.hist(normalApprox, alpha=0.4, density=True, label='error diff')
plt.legend()
plt.grid()
plt.show()


print(f"The mean of the line is  : {np.mean(BL):.2f}")
print(f"The mean of the actual is: {np.mean(BA):.2f}")
print(f"The mean of the error is : {meanError:.2f}")
print(f"The standard deviation is: {stdError:.2f}")

# if line + actual is negative you lose if betting home
#if line + actual is > 0  you win if betting home

lost = 0
win = 0

bank = 0

for i in range(len(BL)):
    n = BL[i] + BA[i]
    if n < 0:
        lost += 1
        bank -= 11
#        print('You lost')
    if n > 0: 
        win += 1
        bank += 10
#        print('You won..')
        
print(f'[betting on home] wins = {win}, lost = {lost}, bank = {bank}')



