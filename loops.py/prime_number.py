# WAP to find whether a given number is prime or not
number=int(input("Enter your number : "))

is_prime =True 

for divisor in range(2,number):
    if(number%divisor==0):
        is_prime=False
        break
if is_prime:
    print(number,"Prime number")
else:
    print(number,"Not a Prime number")