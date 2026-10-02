n=int(input("Enter the value of n : "))

for i in range(1,n+1):
    print("*"*i)

# VARIATION 2

for i in range(n,0,-1):
    print("*"*i)

# VARIATION 3
number=0

for i in range(1,n+1):
    number=number*i
    print(number)