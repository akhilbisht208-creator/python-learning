# A list contains the multipliaction table of 7 . WAP to convert it to vertical string of same number

# Method 1
table=[str(7*i) for i in range(1,11) ]
s= "\n".join(table)
print(s)


# Method 2

multipliation_of_7=[7,14,21,28,35,42,49,56,63 ,70]

for i in multipliation_of_7:
    print(str(i))