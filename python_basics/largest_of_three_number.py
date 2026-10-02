a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))    
c=int(input("Enter the value of c:"))

if(a>b and a>c):
    print(f"{a} is the largest number")
elif(b>c):
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")

