#WAP to open three files, files1.txt ,files2.txt, files3. if any these files are not present ,
#a message with out exiting the program must be printed promoting the same
try:
    with open("Advanced_Python/1.txt", "r") as f1:
        print(f1.read())
except Exception as e:
    print(e)
try:
    with open("Advanced_Python/2.txt", "r") as f2:
        print(f2.read())
except Exception as e:
    print(e)
try:
    with open("Advanced_Python/3.txt", "r") as f3:
        print(f3.read())
except Exception as e:
    print(e)

    print("Thank You!")