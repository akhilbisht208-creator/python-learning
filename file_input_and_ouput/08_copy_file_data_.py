 # WAP to make a copy of text file "this.txt"

with open("file_input_and_ouput/data.txt", "r") as f:
    content=f.read()

with open("file_input_and_ouput/data.copy", "w") as f:
    f.write(content)
