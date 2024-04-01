tam=int(input("Enter your tamil subject marks:"))
eng=int(input("Enter your english subject marks:"))
mat=int(input("Enter your maths subject marks:"))
sci=int(input("Enter your science subject marks:"))
ss=int(input("Enter your social subject marks:"))
total=tam+eng+mat+sci+ss
avg=total/5
print(total, avg)
if(avg<35):
    print("Additional class is required")
else:
    print("You are good to go")
