# Add a static method in problem  2, to grret the user with hello



class calculator:
    def __init__(self, number):
        self.number = number
        self.square = self.number ** 2
        self.cube = self.number ** 3
        self.square_root = self.number ** 0.5


@staticmethod
def hello():
    print("Hello there !")
    
number = calculator(int(input("Enter your number: ")))

a=hello()
print("Square of", number.number, "is", number.square)
print("Cube of", number.number, "is", number.cube)
print("Square root of", number.number, "is", number.square_root)