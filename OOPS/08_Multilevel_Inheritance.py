# Create a class "pets" from a class "Animals " and further create a class "Dog " from "pets" .
# Add a method "bark" to class "Dog"

class Animal:
    pass
class Pets(Animal):
        pass
class Dog(Pets):
    def bark(self):
        print("bark")
o=Dog()
o.bark()
