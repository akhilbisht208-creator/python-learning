# Write a recursive function to find the sum of digits of a number.

def sum_of_digit(n):

    sum=0
    if(n==0):
        return 0

    return n%10+sum_of_digit(n//10)

print(sum_of_digit(12121))