# Paying Off Credit Card in a year
# Balance, annualInterestRate are defined
# Define variables
MinMonpay = 10
balance = 3329
annualInterestRate = 0.2

# Nested while and for loop to calculate minimum payment to pay off credit in a year
while  True:
    bal = balance
    
    # For loop to calculate payment
    for month in range(0,12):
        Unpaidbalance = bal - MinMonpay
        bal = Unpaidbalance + annualInterestRate/12 * Unpaidbalance
  
    # If statement to exit while loop
    if bal <= 0:
        break
    else:
        MinMonpay += 10

# Lowest Payment
print('Lowest Payment: ' + str(MinMonpay))
    