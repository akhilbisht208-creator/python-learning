# WAP  to find the greatest of four numbers entered by the user

numb1=int(input("Enter the number :  "))
numb2=int(input("Enter the number :  "))
numb3=int(input("Enter the number :  "))
numb4=int(input("Enter the number :  "))

if(numb1>numb2 and numb1>numb3 and numb1>numb4):
    print("Greatest",numb1)
elif(numb2>numb1 and numb2>numb3 and numb2>numb4):
    print("Greatest",numb2)
elif(numb3>numb1 and numb3>numb2 and numb3>numb4):
    print("greatest",numb3)

elif(numb4>numb1 and numb4>numb2 and numb4>numb3):
    print("greatest",numb4)