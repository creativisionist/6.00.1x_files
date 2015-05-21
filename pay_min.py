balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12.0
remainingBalance = balance
month = 0
mmp = 0
totalPaid = 0
while month < 12 and remainingBalance > 0:
    month += 1
    mmp = monthlyPaymentRate * remainingBalance
    remainingBalance = remainingBalance - mmp
    remainingBalance = remainingBalance + (remainingBalance * monthlyInterestRate)
    print ("Month: " + str(month))
    print ("Minimum monthly payment: " + str(round(mmp,2)))
    print ("Remaining balance: " + str(round(remainingBalance, 2)))
    totalPaid += mmp
   

print("Total paid: " + str(round((totalPaid),2)))
print ("Remaining balance: " + str(round(remainingBalance,2)))