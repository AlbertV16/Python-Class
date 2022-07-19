# Secret number guessing code using bisection code
# Greet user
print('Hello, please think of a number between 0 and 100')

# Define variables used for guessing number
low = 0
high = 100
guess = (low + high)/2
ans = True

# While loop to guess number using bisection method
while ans:
    
    # Initate guess
    print('Is your secret number ' + str(guess) + '?')
    
    # Is guess correct?
    ind = str(raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly.'))

    # Conditions depending on the user response
    if ind == 'h':
        high = guess
    elif ind == 'l':
        low = guess
    elif ind == 'c':
        ans = False
    else:
        print('Sorry, I did not understand your input')

    guess = (low + high)/2

# Indicate the correct answer has been guessed
print('Game over. Your secret number was: ' + str(guess))