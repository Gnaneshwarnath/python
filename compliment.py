num = int(input("Enter the integer: "))

binary_str = bin(num)[2:]

complement_str = ''

for bit in binary_str:
    if bit == '0':
        complement_str += '1'
    elif bit == '1':
        complement_str += '0'

complement = int(complement_str, 2)

print("Complement of", num, "is:", complement)
