# WAP  to find out whether a given post talking about "AKHIL "OR NOT.

from operator import pos


post=" AKHIL IS BRILLINAT BOY AND WANT TO BECOME IN THE TOP 10 % ENGINEER IN THE INDIA "

if( "AKHIL".lower() in post.lower()):
    print("YES POST IS TALKING ABOUT AKHIL")
else:
    print("NO POST IS NOT TALKING ABOUT AKHIL")
