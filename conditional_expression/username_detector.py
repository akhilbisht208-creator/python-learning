#  WAP to find whether a given username  contains less than 10 characters or not.

username=input("Enter your ussername : ")

if(len(username)>=10):
    print("Your username is approved and your username is ",username)
else:
    print("Enter another user name and your username shuould have minimun 10 character ")