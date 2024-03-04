n= int(input("Enter the size of the binary array: "))
nums = []
for i in range(0,n):
    nums.append(int(input("Enter 0 or 1: ")))
max_count = 0
count = 0
for i in nums:
    if i == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print("Maximum number of consecutive 1's:", max_count)
