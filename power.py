x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
result = 1.0
if n < 0:
    x = 1 / x
    n = -n
for i in range(n):
    result *= x
print("Result:", result)
