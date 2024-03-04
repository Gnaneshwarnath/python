n=input("enter string:")
c=0
for i in range(len(n)):
    if(n[i]==" "):
        c=0
    else:
        c=c+1
print(c)