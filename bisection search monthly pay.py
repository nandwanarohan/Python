# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:11:29 2018

@author: HP PC
"""

balance = 47999
annualintrate = 0.18
lower = balance / 12
upper = balance * ((1 + annualintrate / 12.0) ** 12) / 12.0
mid = (lower + upper)/ 2.0
def EndBalance(monthlypay):
    myBal = balance
    for months in range(1, 13):
        interest = (myBal - monthlypay) * annualintrate / 12.0
        myBal = myBal + interest - monthlypay
    return myBal

while abs(EndBalance(mid)) >= 0.01:
    print('Lower:' +str(lower) + 'Upper: ' + str(upper)  + 'Mid: ' + str(mid))
    if EndBalance(mid) < 0:
        upper = mid
    else:
        lower = mid
    mid = (lower + upper) / 2.0
    
print('Lowest Payment: ' + str(round(mid)))

        