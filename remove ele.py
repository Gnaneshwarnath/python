a=[]
n=int(input("enter the size:"))
for i in range(0,n):
    ele=int(input("enter elements:"))
    a.append(ele)
print(a)
n1=int(input("enter a value:"))
for i in a:
    a.remove(n1)
print(a)