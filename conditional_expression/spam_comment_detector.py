#  A spam comment is defined as a text containing following keywords ;
#"Make a lot of money ", "but now ","subscribe this ","click this". WAP to detect these spams.

comment=input("Enter the comment : ")
spam_word1="Make a lot of money "
spam_word2= "but now "
spam_word3="subscribe this "
spam_word4="click this"

if(spam_word1 in comment or spam_word2 in comment  or spam_word3 in comment or spam_word4 in comment ):
    print("this comment is spam comment")
else:
    print("This is Not a  spam comment ")