def fun():


    # FUNCTION DEFINATION
    a=int(input("Enter your number : "))
    b=int(input("Enter your number : "))
    c=int(input("Enter your number : "))

    avg=(a+b+c)/3
    print(avg)

#FUNCTION CALL
fun()
print("Thank you")
fun()
fun()


def goodday():

    #FUNCTION DEFINATION
    name=input("Enter your name : ")
    print(f"GOO DAY {name}")

goodday()


def func(name ,ending):

    print("Good Day"+ name)
    print(ending)

func("AKHIL","THANK YOU")
func("RAHUL","Thanks")



 # How do you prevent a python print() function to print a new line at the end .


print("hello")
print("World")
print("hello",end="")
print("World",end="")
