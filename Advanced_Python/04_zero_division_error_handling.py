# WAP to display a/b where a and b are integers . if b=0 ,
# display infinite by handling the "ZeroDivisionError"

try:
    a=int(input("Enter your number a  :"))
    b=int(input("Enter your number b  :"))
    print(a/b)
except ZeroDivisionError as e:
    print("infinite")
    print(e)