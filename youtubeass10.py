salary=int(input("Enter your salary:"))
age=int(input("Enter you age:"))
if(salary>=20000 or age<=25):
    loanamt=int(input("Required Loan Amount:"))
    if(loanamt<=50000):
        print("you are eligible for loan")
    elif(loanamt>50000):
        print("Maximum loan amount is 50000")
else:
    print("You are not eligible for loan")
