n=int(input("enter no.of input:"))
a=[]
count=0
for i in range(0,n):
    ele=int(input(""))
    a.append(ele)
print(a)
m=max(set(a),key=a.count)
print(m)
