# Write a recursive function to count the number of digits in a number.




def count_digit(n):

    if(n==0):
     return 0
    return 1+count_digit(n//10)


  

print(count_digit(1221))
