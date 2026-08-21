#Write a program that asks the user to enter 5 numbers, stores them in a list, and prints their sum.

numbers = []

number1=int(input("Enter number 1 : "))
numbers.append(number1)
number2=int(input("Enter number 2 : "))
numbers.append(number2)
number3=int(input("Enter number 3 : "))
numbers.append(number3)
number4=int(input("Enter number 4 : "))
numbers.append(number4)
number5=int(input("Enter number 5 : "))
numbers.append(number5)

print(sum(numbers))