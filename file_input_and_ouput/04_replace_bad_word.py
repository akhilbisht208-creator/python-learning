# A file contains a word "DONKEY" multiple times  ,
# You need to write a program which replace this word with ##### by updating the same file.

def replace_word():
    with open("file_input_and_ouput/data.txt", "r")as f:
        data=f.read()
        data=data.replace("DONKEY", "#####")
        

    with open("file_input_and_ouput/poem.txt","w")as f:
        f.write(data)
        print(data)

replace_word()
