a=[]
c=[]
n1=int(input("enter size of a:"))
for i in range(0,n1):
    a1=int(input("enter elements of a1:"))
    a.append(a1)
print(a)
b=[]
n2=int(input("enter size of a:"))
for i in range(0,n2):
    b1=int(input("enter elements of a1:"))
    b.append(b1)
print(b)
for i in a:
    c.append(i)
for i in b:
    c.append(i)
print("Merged and sorted list c:", sorted(c))