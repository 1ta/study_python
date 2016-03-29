def sum13(nums):
    sum = 0
    l = len(nums)
    i = 0
    while i < l:
        if nums[i] == 13:
            i+=1
        else:
            sum+=nums[i]
        i+=1
    return sum

def sum67(nums):
    sum = 0
    l = len(nums)
    i = 0
    while i < l:
        if nums[i]==6:
            i+=1
            while i<l:
                if nums[i]!=7:
                    i+=1
                else:
                    break
        else:
            sum+=nums[i]
        i+=1
    return sum

def sum67(nums):
    sum = 0
    l = len(nums)
    i = 0
    should_add = True
    while i < l:
        if nums[i]==6:
            should_add = False
        if should_add:
            sum+=nums[i]
        if nums[i]==7:
            should_add = True
        i+=1
    return sum

def sum67(nums):
    last_is_2 = False
    for i in nums:
        if i==2:
            if last_is_2:
                return True
            else:
                last_is_2 = True
        else:
            last_is_2 = False
    return False

def has22(nums):
    for i in range(len(num) - 1):
        if num[i] == 2 and num[i+1] == 2:
            return True
    return False
