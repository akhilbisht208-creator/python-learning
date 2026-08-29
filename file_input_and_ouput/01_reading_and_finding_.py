# WAP to read the text from a given file "poem.txt" and find out whether it contains the word "twinkle"

with open("file_input_and_ouput/poem.txt", "r") as f:
    text=f.read()

    if("twinkle" in text):
        print("YES TWINKLE IS PRESENT ")
    else:
        print("YES TWINKLE IS NOT  PRESENT ")

#print(text)

