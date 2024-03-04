nums = input("Enter the numbers separated by spaces: ").split()
nums = [int(num) for num in nums]
nums.sort()
result = [[]]
for num in nums:
    new_result = []
    for perm in result:
        for i in range(len(perm) + 1):
            new_result.append(perm[:i] + [num] + perm[i:])
            if i < len(perm) and perm[i] == num:
                break
    result = new_result

print("Unique permutations:", result)
