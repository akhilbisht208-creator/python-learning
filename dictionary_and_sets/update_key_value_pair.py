# Create an empty dict . allow 4 friends to enter thier fav language as vlaue and use key as their names , Assume that the names are unique


dict={} #dic{name of friend = " lang"}

name= input("Enter your friend name : ")
lang= input("Enter your frind lang : ")
dict.update({name: lang})
name= input("Enter your friend name : ")
lang= input("Enter your frind lang : ")
dict.update({name: lang})
name= input("Enter your friend name : ")
lang= input("Enter your frind lang : ")
dict.update({name: lang})
name= input("Enter your friend name : ")
lang= input("Enter your frind lang : ")
dict.update({name: lang})


print(dict)







#--------------------OR--------------------------
dict={} #dic{name of friend = " lang"}


dict["akhil"]="English"
dict["Ramesh"]="Hindi"
dict["Suresh"]="Urdu"
dict["Ishant"]="Bojpuri"


print(dict)


