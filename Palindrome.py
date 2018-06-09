# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:42:50 2018

@author: HP PC
"""

def isPalindrome(s):
    def Chars(s):
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(Chars(s))

print(" Is eve a Palindrome ?")
print(isPalindrome("eve"))