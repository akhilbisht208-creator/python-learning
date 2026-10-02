n=int(input("Enter value of  n : "))
reverse=0
original=n
while(n>0):
    d=n%10  #last digit
    reverse=reverse*10+d  #puting last value one by one
    n=n//10   #erease decimal number


if reverse==original:  
    print(f"Yes {original} is plaindrome number")
else:
    print(f"No {original} is not a palindrome number")