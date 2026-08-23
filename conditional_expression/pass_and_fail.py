# WAP to find out whether a student has  passed or failes if it requires a total of 40% and at least 33% in each subjesct . Assume 3 subjects and take marks as an input from the user.

marks_hindi= int(input("Enter the marks of Hindi : "))
marks_english= int(input("Enter the marks of english : "))
marks_maths= int(input("Enter the marks of maths : "))


total_percentage= ((marks_english+marks_hindi+marks_maths)*100) /300 
if(total_percentage <= 40 and marks_english <=33 and marks_hindi <=33 and marks_maths <=33 ):
    print("You are Fail and you total percentage is ",total_percentage) 

else:
    print("You are Pass and you total percentage is ",total_percentage)

    