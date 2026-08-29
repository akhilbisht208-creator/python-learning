# Create a class with a class attribute a ; create an object from it and set "a" directly using object.a=o .
#  Does this changes the class attribute ?

class Demo:
    a=3

o=Demo() 
print(o.a)# Prints the class attribute because instance attribute is not present
o.a=0  # Instance attribute is set
print(o.a) # Prints the instance aatribute beacuse instance attribute is presnet
print(Demo.a) # Prints the class attributed
