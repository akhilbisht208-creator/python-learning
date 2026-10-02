#Count the number of digits in a positive integer
n=int(input("Enter the value of n : "))
digit=0
count=0

while n>0:
    n//=10
    count=count+1

print(count)
