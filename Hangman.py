# Hangman game


import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:

        if letter not in lettersGuessed:

            return False

    return True
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    userin = ''
    
    for letter in secretWord:
    
        if letter in lettersGuessed:
        
            userin += letter
        
        else:
        
            userin += ' _ '

    return userin



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
   
    alpha = string.ascii_lowercase
    
    availableletters = ''
    
    for letter in alpha:
    
        if letter not in lettersGuessed:
        
            availableletters += letter
    
    return availableletters
    

def hangman(secretWord):
    
    print("Welcome to the game, Hangman!")
    
    print("I am thinking of a word that is {0} letters long".format(len(secretWord)))
    
    print("-----------")
    
    guesses = 8
    
    lettersGuessed = []
    
    while True:
    
        print("You've {0} guesses left.".format(guesses))
        
        print("Available Letters: {0}".format(getAvailableLetters(lettersGuessed)))
        
        guess = (input("Please guess a letter:")).lower()
        
        if guess in lettersGuessed:
        
            print("Oops! You've already guessed that letter:{0}".format(getGuessedWord(secretWord, lettersGuessed)))
            
            continue
        
        if guess in secretWord:
        
            print("Good Guess:{0}".format(getGuessedWord(secretWord, lettersGuessed)))
        
        elif guess not in secretWord:
        
            print("Oops! That letter is not in my word:{0}".format(getGuessedWord(secretWord, lettersGuessed)))
           
            guesses -= 1
      
      
        print("----------")
        
            
        
        if isWordGuessed(secretWord, lettersGuessed):
           
            print("Congratulations!! You've Won")
            
            break
        
        if guesses == 0:
        
            print("Sorry you ran out of guesses. The word was {0}".format(secretWord))
           
            break
            
    
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

