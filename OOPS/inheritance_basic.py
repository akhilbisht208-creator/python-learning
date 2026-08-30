"""class Employee:
    company = "ITC"
    name = "Default Name"

    def show(self):
        print(f"The name of the Employee is {self.name}")
        print(f"The company is {self.company}")


class Coder:
    language = "Python"

    def printlang(self):
        print(f"Out of all the languages, here is your language: {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showlanguage(self):
        print(f"The company is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printlang()
b.showlanguage()"""


#---------------------------SUPER METHOD-------------------------
 
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1
 
class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b=2
 
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c=3
"""
o=Employee()
print(o.a)

o=Programmer()
print(o.a,o.b)
"""
o=Manager()
print(o.a,o.b,o.c)