def isPalindrome(aString):
    '''
    aString: a string
    returns True is aString is a palindrome
    False, otherwise
    '''
    if len(aString) == 1 or aString == '':
        return True
    else:
        return aString[0] == aString[-1] and isPalindrome(aString[1:-1])