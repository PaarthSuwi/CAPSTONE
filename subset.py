nums = [1,2,3]
subset = [[]]
for num in nums:
    subset += [curr+[num]for curr in subset]
print("subsets",subset[1:])
    