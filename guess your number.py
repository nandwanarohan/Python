# -*- coding: utf-8 -*-
"""
Created on Thu May 31 18:16:40 2018

@author: HP PC
"""

print("Please think of a number between 0 and 100")
high = 100
low = 0
guessed = False
while not guessed:
      guess = (high + low)//2
      print("Is your Secret number: " + str(guess) + "?")
      userent = input("Enter 'h' to indicate guess is too high. Enter 'l' to indicate guess is too low. Enter 'c' to indicate I guessed it correctly.")
      
      if userent == 'c':
         guessed = True
      elif userent == 'h':
         high = guess
      elif userent == 'l':
         low = guess
      else:
         print("Sorry, I did not understand your input.")
print('Game over. Your secret number was: ' + str(guess))    

      