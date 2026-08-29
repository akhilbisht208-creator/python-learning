# WAP to find out whether a file is identical and matches the content of another files


with open("file_input_and_ouput/data.txt", "r") as f:
    content1=f.read()


with open("file_input_and_ouput/data2.txt", "r") as f:
    content2=f.read()
if(content1==content2):
    print("YES THESE FILES ARE IDENTICAL")
else:
    print("NO")