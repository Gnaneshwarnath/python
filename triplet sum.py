nums = input("Enter the list of numbers separated by spaces: ").split()
nums = [int(num) for num in nums]

result = []

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                result.append([nums[i], nums[j], nums[k]])

print("Triplets with sum equal to zero:", result)
