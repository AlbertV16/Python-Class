# Program to count vowels
# Define variables
s = 'asdf'
vowel = 0

# For loop to count vowels
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowel +=1

# Print number of vowels
print('Number of vowels =' + str(vowel))