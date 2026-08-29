#WAP to find out the line number where "LAPTOP" is prensent 
lineno=1

with open("file_input_and_ouput/data.txt", "r") as f:
    lines=f.readlines()
    for line in lines:
        if("LAPTOP" in line):
            print(f"YES LAPTOP IS  PRESNET IN  LINE NUMBER {lineno}")
            break
        else:
            print("NO LAPTOP IS NOT PRESNET IN ANY ROW OF THE CONTENT")
        lineno+=1
