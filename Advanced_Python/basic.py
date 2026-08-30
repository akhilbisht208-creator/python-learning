# 1. WALRUS OPERATOR

if(n:= len([1,2,34,5,6]))>3:
    print(f"List is too long ({n} elements, expected <=3)")

# 2. TYPE DEFINATION
    #varible :dataype = value


# 3. ADVANCED TYPE HINT   

from typing import List ,Tuple ,Dict,Union
numbers : List[int]=[1,2,3,4]
indentifier : Union[int,str]="ID123"
#varible : list/tuple/dict/union[data type ]=value (and bracet according to datatype)

# 4.MATCH CASE

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 300:
            return "YES"
        case _:
            return "NOT FOUND"
print(http_status(2003))


#5. DICTINOARY MERGE AND UPDATE OPERATIOR

#merged=dict1|dict2

#with (
#    open("file1.txt") as f1,
#    open("file2.txt") as f2,
#):


# 6.EXCEPTIONAL HANDLING

try:
    a=int(input("Hey! , Enter the number --->>"))
    print(a)
except ValueError as v:
    print("hi")
    print(v)
except Exception as e:
    print(e)