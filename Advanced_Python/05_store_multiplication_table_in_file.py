# store the multiplication tables  in file named Tables.txt

n=int(input("Enter your number :"))

table=[i*n for i in range(1,11)]
print(f"Table of {n} : {table}\n")

with open("Advanced_Python/Table.txt","w") as f:
    f.write(f"Table of {n} : {table}\n")
    #if we are using string ("") so not need to use str conversion