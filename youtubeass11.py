cibscr=int(input("Enter you cibil score:"))
if(cibscr<=500):
    print("Your Cibil Score is",cibscr,"You are cibilscore is low and you are not eligible for loan")
elif(cibscr>500 and cibscr<600):
    print("Your Cibil Score is",cibscr,"So,you are eligible for loan amount 20,000")
elif(cibscr>600 and cibscr<700):
    print("Your Cibil Score is",cibscr,"So,You are eligible for loan amount 30,000")
elif(cibscr>700 and cibscr<800):
    print("Your Cibil Score is",cibscr,"So,You are eligible for loan amount 40,000")
elif(cibscr>800 and cibscr<=900):
    print("Your Cibil Score is",cibscr,"So,You are eligible for loan amount 50,000")
else:
    print("You are enter invalid cibilscore. Please enter 0-900 between values")
