balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
lp = balance * ( monthlyInterestRate/ ( 1-((1+monthlyInterestRate)**(-12) )))
print("Lowest Payment: " + str(round(lp,2)))
print("Lowest Payment: " + str(int(lp)))
print("Lowest Payment: " + str(int(round(lp,-1))))