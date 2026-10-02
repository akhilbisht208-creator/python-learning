#Reverse a Number

n=int(input("Enter the value of n : "))
reverse=0
digit=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10

print(reverse)