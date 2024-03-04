a=[]
b=[]
n=int(input("enter the size:"))
for i in range(0,n):
    ele=int(input("enter the elements:"))
    a.append(ele)
print(a)
for i in a:
    if i not in b:
        b.append(i)
print(b)