# Write a List comprehension to print a list which contains the multilpication table of a user entered number
n=int(input("Enter your number :"))

table=[i*n for i in range(1,11)]
print(table)