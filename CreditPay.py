# Paying Minimum on Credit Cards
# Balance, annualInterestRate and monthlyPaymentRate are defined
# Define variables
MinMonpay = 0
Totalpaid = 0

# for loop to print balance in months
for month in range(0,12):
    MinMonpay = balance * monthlyPaymentRate
    Unpaidbalance = balance - MinMonpay
    balance = Unpaidbalance + annualInterestRate/12 * Unpaidbalance
    print ('Month: ' + str(month+1))
    print ('Minimum monthly payment: ' + str(round(MinMonpay,2)))
    print ('Remaining balance: ' + str(round(balance,2)))
    Totalpaid += MinMonpay
    
# Final balance
print('Total paid: ' + str(round(Totalpaid,2)))
print('Remaining balance: ' + str(round(balance,2)))
    