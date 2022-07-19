# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "D:\Canopy\Python Class\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    word = 0
    for i in lettersGuessed:
        for x in range(0,len(secretWord)):          
            if i == secretWord[x]:
                word += 1
            
    return word == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ['_ '] * len(secretWord)
    guess = ''
    for i in lettersGuessed:
        for x in range(0,len(secretWord)):      
            if i == secretWord[x]:  
                word[x] = i
                
    for k in range(0, len(word)):
        guess += word[k]

    return guess


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.ascii_lowercase
    for i in lettersGuessed:
        alphabet = alphabet.replace(i,'')
        
    return alphabet

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    
    # Define variables
    word = str(len(secretWord))
    lettersGuessed = []
    mistakesMade = 0
    x = 8
    
    # print Greetings to indicate start of game
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' +word+ ' letters long.')
    
    # while loop for hangman guesses
    while mistakesMade < 8:
        print('-------------')
        y = str(x)
        print('You have ' + y + ' guesses left.')
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = raw_input('Please guess a letter: ')
        
        # Convert upper case letter to lowercase
        if guess in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            guess = guess.lower()
            
        if guess in lettersGuessed:
            print('''Oops! You've already guessed that letter: ''' + getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
        elif guess in availableLetters:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            mistakesMade += 1
            x -= 1
            
        # Condition to exit loop if word is guessed
        if isWordGuessed(secretWord, lettersGuessed):
            break
            
    # Output Message depening on results
    if isWordGuessed(secretWord, lettersGuessed):
        print('-------------')
        print('Congratulations, you won!')
    else:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.') 





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
