num1 = input("Enter the first number: ")[::-1]
num2 = input("Enter the second number: ")[::-1]

result = []
carry = 0

for i in range(max(len(num1), len(num2))):
    digit_sum = carry
    if i < len(num1):
        digit_sum += int(num1[i])
    if i < len(num2):
        digit_sum += int(num2[i])
    
    result.append(str(digit_sum % 10))
    carry = digit_sum // 10

if carry:
    result.append(str(carry))

sum_result = ''.join(result[::-1])

print("The sum of the two numbers is:", sum_result)
