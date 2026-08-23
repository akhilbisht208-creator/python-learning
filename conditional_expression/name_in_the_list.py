# WAP which finds out whether a given name is present in a list or not

list=["Ramesh ","Suresh ","Rajesh","Mukesh"]
given_name=input("Enter the given name : ")

if(given_name in list ):
    print("Yes ", given_name, "is present in the list  ")
else:
    print("No given name is not in the list ")