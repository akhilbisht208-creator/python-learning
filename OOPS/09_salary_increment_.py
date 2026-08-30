# Create a class "Employee " and add salary and increment properties to it.
class Employee:
    def __init__(self,salary,increment,exprience):
        self.salary=salary
        self.increment=increment
        self.exprience=exprience

        if(self.exprience>5 ):
            self.increment=self.increment+self.salary*(5/100)
        else:
            print(self.salary)
o=Employee(120000,10000,6)
print(o.salary)
print(o.increment)

