# WAP to print third , fifth and seventh element from a list using enumerrate function
list=[1,2,3,4,5,6,7,8]

for i ,item in enumerate(list):
    if(i==2 or i==4 or i==6):
        print(item)


#-----------------GENERALIZED FORM-------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i, item in enumerate(numbers):
    if i % 2 == 0 and i >= 2:
        print(item)