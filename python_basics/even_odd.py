numbers = [10 , 15, 22, 31, 40, 51]
even_count=0
odd_count=0
for i in numbers:
    if i%2==0:
        even_count=even_count+1

    else:
        odd_count=odd_count+1
print(odd_count)
print(even_count)

