a=[]
n=int(input("enter size:"))
for i in range(0,n):
    ele=int(input("enter elements:"))
    a.append(ele)
a[n-1]=(a[n-1]+1)
for i in range(n - 1, 0, -1):
    if a[0] == 10:
        a[0] = 0
        a[i - 1] += 1
        a.insert(0, 1)
print(a)