# Paying Off Credit Card in a year
# Balance, annualInterestRate are defined
# Define variables
low = balance/12
high = (balance * (1 + annualInterestRate)**12)/12
epsilon = 0.01

# Nested while and for loop to calculate minimum payment to pay off credit in a year
while  True:
    bal = balance
    MinMonpay = (high + low)/2
    
    # For loop to calculate payment
    for month in range(0,12):
        Unpaidbalance = bal - MinMonpay
        bal = Unpaidbalance + annualInterestRate/12 * Unpaidbalance

    # If statement to exit while loop
    if abs(bal) <= epsilon:
        break
    elif bal > 0:
        low = MinMonpay
    else:
        high = MinMonpay
 
# Lowest Payment
print('Lowest Payment: ' + str(round(MinMonpay,2)))