user_input = input("Enter the array of integers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

max_sum = nums[0]
current_sum = 0

for num in nums:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print("Maximum subarray sum:", max_sum)
