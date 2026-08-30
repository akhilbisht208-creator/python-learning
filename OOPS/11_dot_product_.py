# Write a class vector representing a vector of n dimensions.
# Overload the + and * operators to calculate
# the sum and dot product of two vectors.


class vector:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Overload + operator
    def __add__(self, other):
        result = self.a + other.a, self.b + other.b, self.c + other.c
        return result

    # Overload * operator for dot product
    def __mul__(self, other):
        result = self.a * other.a + self.b * other.b + self.c * other.c
        return result

    # Display vector
    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"


v1 = vector(2, 3, 4)
v2 = vector(3, 4, 5)

print("First vector is:", v1)
print("Second vector is:", v2)

print("Sum of the vectors is:", v1 + v2)

print("Dot product of the vectors is:", v1 * v2)

        
        