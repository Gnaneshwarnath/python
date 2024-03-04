n = list(map(int, input("Enter the numbers: ").split()))
b = []
for i in n:
    b.append(i * i)
b.sort()
print("Output:",b)


