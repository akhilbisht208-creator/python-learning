# WAP to generate multiplication table from 2 to 20 and write it to the diffenert files,
# place these files in a folder for a 13 - year old


def calclulatetable(n):

    table=""
    for i in range(1,11):
        table+=f"{n} X {i} ={n*i}\n"

    with open(f"file_input_and_ouput/tables/table_{n}.txt", "w") as f:
     f.write(table)

for i in range(2,21):
    calclulatetable(i)




















""" 
1. file_input_and_ouput/tables/table_{n}
# main folder / subfolder in main folder in which output files are stored/ individual file under sub folder in which table written

2. f.write(table)
   table ke andar jo written data/multiplication table hai, usko f file ke andar write/store karna.

3.calclulatetable(i)
    “First, iteration happens in the for loop, and one by one the current value of i is passed to the function as n through calclulatetable(i).” 
"""