# A list contains such words to be censored  ,
# You need to write a program which replace this words with ##### by updating the same list.
words=["DONKEY","BAD","GANDE"]

with open("file_input_and_ouput/data.txt", "r") as f:
    content=f.read()

    for word in words:
        content=content.replace(word,"#"*len(word))

        with open("file_input_and_ouput/data.txt", "w") as f:
            f.write(content)