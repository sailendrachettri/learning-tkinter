nums = [8, 1, 2, 2, 3]

count = 0
for i in nums:
    for j in nums:
        if i != j and i > j:
            count += 1
    nums.append(count)

print(nums)