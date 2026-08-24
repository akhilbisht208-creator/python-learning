# Make a RING from using "*"
n=int(input("Enter your number :"))
for i in range(1,n+1):
    if(1==i or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")