nums = [4, 8, 15, 16, 23]
target = int(input("Find: "))
if target in nums:
    print("Found at index", nums.index(target))
else:
    print("Not found")
