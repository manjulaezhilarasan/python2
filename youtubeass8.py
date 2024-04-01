a=int(input("a:"))
b=int(input("b:"))
user=str(input("What you want add/sub/mul/div please tell me:"))
if(user=="add"):
    print(a+b)
elif(user=="sub"):
    print(a-b)
elif(user=="mul"):
    print(a*b)
elif(user=="div"):
    print(a/b)
else:
    print("Please enter correct code.")
