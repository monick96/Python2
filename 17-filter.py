nums = [1,2,3,4,5]
new_nums = filter(lambda x: x % 2 == 0, nums)
new_nums = list(new_nums)
print(new_nums)
print(nums)