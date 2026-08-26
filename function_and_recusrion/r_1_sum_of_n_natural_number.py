# WAP a recursive function to calculate the sum of first n natural numbers.

def sum_n_natural(n):
    if(n==1):
        return 1
    return sum_n_natural(n-1)+n

print(sum_n_natural(5))
