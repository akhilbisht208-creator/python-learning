# WAP to calculate the grade of a student from his marks from the following scheme

marks= float(input("Enter your marks : "))

if(marks>=90 and marks<=100):
    print(" GRADE : Excelent ")
elif(marks>=80 and marks<90 ):
    print("GRADE : A ")
elif(marks<=80 and marks>=70):
    print("GRADE : B")
elif(marks<=70 and marks>=60):
    print("GRADE : C")
elif(marks<=60 and marks>=50):
    print("GRADE : D ")
else:
    print("GRADE : F ")
