# WAP to filter a list of numbers which are divisbile by 5
number=list(range(1,100))
result=list(filter(lambda x: x%5==0,number))
print(result)