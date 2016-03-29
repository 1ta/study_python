def count_evens(nums):
    count = 0
    for num in nums:
        if num%2 == 0:
            count += 1
    return count

def big_diff(nums):
    return max(nums)-min(nums)

def centered_average(nums):
    a = max(nums)
    b = min(nums)
    nums.remove(a)
    nums.remove(b)
    return sum(nums)/len(nums)

def has22(nums):
    for i in r
