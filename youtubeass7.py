score=int(input("Enter your score:"))
if(score<35):
    print("You are a Poor Student")
elif(score>=35 and score<70):
    print("You are an Average Student")
elif(score>=70 and score<100):
    print("You are a Good Student")
else:
    print("Score is invalid")
