# Create a class "Employee" and add salary and increment properties to it.
# Write a method "salaryAfterIncrement" with a @property decorator
# with a setter which changes the value of increment based on the salary.

class Employee:
    salary=230
    increment=20

    @property
    def salaryAfterIncrement(self):
        return(self.salary+self.salary*self.increment*1/100)
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment=((salary/self.salary)-1)*100

e=Employee()
e.salarysalaryAfterIncrement=280
print(e.increment)






#------------------------------------------------WITH IF ELSE-----------------------------------
class Employee:

    def __init__(self, salary, increment):

        # Store salary
        self.salary = salary

        # Store increment
        self.increment = increment

    # GETTER
    # Returns salary after increment
    @property
    def salaryAfterIncrement(self):

        # Salary is incremented by adding increment
        return self.salary + self.increment

    # SETTER
    # Runs when we assign a value to salaryAfterIncrement
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):

        # If salary is less than 120000,
        # salary will get a 30% increment
        if self.salary < 120000:

            # Increase the increment by 30% of salary
            self.increment = self.increment + self.salary * 30 / 100

        else:
            print("NO INCREMENT COMPANY WANT PROFIT")


# Create Employee object
o = Employee(13000, 10000)

# Original salary
print("Original Salary:", o.salary)

# Original increment
print("Original Increment:", o.increment)

# Setter is called
o.salaryAfterIncrement = 0

# Salary after increment
print("Salary After Increment:", o.salaryAfterIncrement)

# Updated increment
print("Updated Increment:", o.increment)