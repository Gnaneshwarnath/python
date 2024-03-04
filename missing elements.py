# Take user input for the value of n
n = int(input("Enter the value of n: "))

# Take user input for the list of numbers directly
nums = []
for i in range(n):
    num = int(input("Enter number {}: ".format(i + 1)))
    nums.append(num)

# Create a list of all numbers in the range [1, n]
all_nums = [i for i in range(1, n + 1)]

# Iterate through nums and remove numbers that appear in nums from all_nums
for num in nums:
    if num in all_nums:
        all_nums.remove(num)

# Print the numbers that do not appear in nums
print("Numbers that do not appear in nums:", all_nums)
