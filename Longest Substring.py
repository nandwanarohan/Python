# -*- coding: utf-8 -*-
"""
Created on Wed May 30 17:58:22 2018

@author: HP PC
"""
s = " dfabhdfsaebjggdfgsdghsrgsergaefr"
maxlen = 0
current = s[0]
longest = s[0]

for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        current += s[i+1]
        if len(current) > maxlen:
            maxlen = len(current)
            longest = current
    else:
        current = s[i+1]
        
    i += 1
print("Longest substring possible is:- " + longest)
        