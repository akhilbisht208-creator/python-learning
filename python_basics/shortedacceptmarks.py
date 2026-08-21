#WAP to accept marks of 6 students and display them in a solted manner.

from operator import sub


subject=[]

akhil =int(input("Enter marks  of akhil :"))
subject.append(akhil)
rahul =int(input("Enter marks of rahul : "))
subject.append(rahul)
kushi =int(input("Enter marks kushi : "))
subject.append(kushi)
saloni =int(input("Enter marks  of saloni :"))
subject.append(saloni)
aditi =int(input("Enter marks of aditi  : "))
subject.append(aditi)
lokesh =int(input("Enter marks of lokesh : "))
subject.append(lokesh)

subject.sort()

print(subject)