#Create a class "Programmer " for storing information of  few programmers working at Microsoft

# Create a class "Programmer" for storing information of
# a few programmers working at Microsoft

class Programmer:
    company = "Microsoft"

    def __init__(self, name, age, salary, experience):
        self.name = name
        self.age = age
        self.salary = salary
        self.experience = experience


akhil = Programmer("AKHIL", 17, 313131331122, 15)
rahul = Programmer("RAHUL", 88, 250000, 5)
saloni = Programmer("SALONI", 91, 300000, 7)


print(f"NAME OF THE PROGRAMMER: {akhil.name}\n"
      f"AGE OF THE PROGRAMMER: {akhil.age}\n"
      f"SALARY OF THE PROGRAMMER: {akhil.salary}\n"
      f"EXPERIENCE OF THE PROGRAMMER: {akhil.experience}\n\n")

print(f"NAME OF THE PROGRAMMER: {rahul.name}\n"
      f"AGE OF THE PROGRAMMER: {rahul.age}\n"
      f"SALARY OF THE PROGRAMMER: {rahul.salary}\n"
      f"EXPERIENCE OF THE PROGRAMMER: {rahul.experience}\n\n")

print(f"NAME OF THE PROGRAMMER: {saloni.name}\n"
      f"AGE OF THE PROGRAMMER: {saloni.age}\n"
      f"SALARY OF THE PROGRAMMER: {saloni.salary}\n"
      f"EXPERIENCE OF THE PROGRAMMER: {saloni.experience}")