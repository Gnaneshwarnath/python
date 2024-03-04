x = int(input("Enter the first integer (x): "))
y = int(input("Enter the second integer (y): "))
count = bin(x ^ y).count('1')
print("Hamming distance between", x, "and", y, "is:", count)
