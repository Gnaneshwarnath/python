n=int(input("enter a number:"))
temp=n
s=0
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
if(temp==s):
    print("true")
else:
    print("false")