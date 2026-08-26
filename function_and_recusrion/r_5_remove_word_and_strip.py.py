# Write a python function to remove a given word from a list ad strip it at the same time
def remove_word_from_list(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["Akhil","Rohan","Sohan","Ramesh","Harry"]

print(remove_word_from_list(l,"han"))