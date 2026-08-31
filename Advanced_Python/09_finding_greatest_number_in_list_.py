# WAP to find maximum of the numbers in a list using the reduce function
from functools import reduce
l=[2,3,4,56,7,5454,5454]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,l))
