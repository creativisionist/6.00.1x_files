balance = 235
annualInterestRate = 0.25

remainingBalance = balance
monthlyInterestRate = annualInterestRate/12.0
mmp = 0
totalPaid = 0
while remainingBalance > 0:
    remainingBalance = balance
    month = 0
    mmp += 10
    while month < 12 and remainingBalance > 0:
        month += 1
        remainingBalance = remainingBalance - mmp
        remainingBalance = remainingBalance + (remainingBalance * monthlyInterestRate)
        print ("Month: " + str(month))
        print ("Minimum monthly payment: " + str(round(mmp,2)))
        print ("Remaining balance: " + str(round(remainingBalance, 2)))
        totalPaid += mmp
   
print("Lowest Payment: " + str(mmp))
print("Total paid: " + str(round((totalPaid),2)))
print ("Remaining balance: " + str(round(remainingBalance,2)))