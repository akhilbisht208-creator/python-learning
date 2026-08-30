# Create a class (2-D vector) and use it to create
# another class representing a 3-D vector


# Parent class
class twoDvector:

    # Constructor of 2-D vector
    def __init__(self, i, j):

        # Store the value of i in the object
        self.i = i

        # Store the value of j in the object
        self.j = j

    # Method to display the 2-D vector
    def show(self):

        # Print i and j
        print(f"The 2-D vector is {self.i}i + {self.j}j")


# Child class
# threeDvector inherits from twoDvector
class threeDvector(twoDvector):

    # Constructor of 3-D vector
    def __init__(self, i, j, k):

        # Call the constructor of the parent class
        # This initializes i and j
        super().__init__(i, j)

        # Store the value of k in the object
        self.k = k

    # Method to display the 3-D vector
    def show(self):

        # Print i, j and k
        print(f"The 3-D vector is {self.i}i + {self.j}j + {self.k}k")


# Create an object of the parent class
v1 = twoDvector(2, 3)

# Call the show method
v1.show()


# Create an object of the child class
v2 = threeDvector(2, 3, 5)

# Call the show method
v2.show()
