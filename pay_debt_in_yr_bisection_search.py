balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0
lowerBound = balance/12
upperBound = (balance * (1 + ((monthlyInterestRate**12))/12.0))

remainingBalance = balance
mmp = 0
n = 0
while remainingBalance != 0 and n < 30:
    #print("Upper: " + str(upperBound))
    #print("Lower: " + str(lowerBound))
    remainingBalance = balance
    month = 0
    mmp = (upperBound + lowerBound)/2
    #print("Testing Payment: " + str(mmp))
    while month < 12 and remainingBalance > 0:
        month += 1
        remainingBalance = remainingBalance - mmp
        remainingBalance = remainingBalance + (remainingBalance * monthlyInterestRate)
    n+=1
    #print("After one year we owe: " + str(remainingBalance))
    if remainingBalance > 0:
        lowerBound = mmp
    elif remainingBalance < 0:
        upperBound = mmp
    else:
        break
print("Lowest Payment: " + str(round(mmp,2)))