x = int(input("Enter a non-negative integer: "))
sqrt = 0
while sqrt * sqrt <= x:
    sqrt += 1
sqrt -= 1
print("Output:", sqrt)
