num = int(input("Enter the integer: "))
base_7_str = ''

# Check if the number is zero
if num == 0:
    base_7_str = '0'

# Convert the number to its base 7 representation
while num != 0:
    base_7_str = str(abs(num) % 7) + base_7_str
    num //= 7

# If the original number was negative, add a minus sign to the base 7 representation
if num < 0:
    base_7_str = '-' + base_7_str

print("Base 7 representation:", base_7_str)
