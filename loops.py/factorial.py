# WAP to calculate the factorial of a given numbers using for loop

n=int(input("Enter you number : "))

factorial=1
for i in range(1,n+1):

        factorial=factorial*i
      
print(factorial)