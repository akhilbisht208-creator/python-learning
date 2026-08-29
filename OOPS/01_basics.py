class Employee:
    salary =1200000
    language="PYTHON"

akhil=Employee()
akhil.name="Akhil"
print(akhil.name,akhil.salary, akhil.language)



#-------------------CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE------------------------------
class Employee:
    salary =1200000
    language="PYTHON"

akhil=Employee()

akhil.name="Akhil"
akhil.language="c++"
print(akhil.name,akhil.salary, akhil.language)



#----------------------------SELF PARAMETER--------------------------------------------

class Employee:
    salary =1200000
    language="PYTHON"

    def getInfo(self):
        print(f"the lanuage is {self.language} and salary is {self.salary}")

akhil=Employee()

akhil.getInfo()


#---------------------------- INIT CONSTUCTOR--------------------------------------------


class Employee:
    salary =1200000
    language="PYTHON"


    def _init_(self,name ,salary , language): #dunder method which is automatically called

        self.name=name
        self.language=language
        self.salary=salary
        print("I AM CREATING AN OBJECT")
    def getInfo(self):
     print(f"the lanuage is {self.language} and salary is {self.salary}")
akhil=Employee("AKHIL",131031091,"JAVA")
print(akhil.name,akhil.salary,akhil.language)