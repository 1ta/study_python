def first_last6(nums):
    if nums[0]==6 or nums[len(nums)-1]==6:
        return True
    else:
        return False

def same_first_last(nums):
    return(len(nums)>=1 and nums[0]== nums[len(nums)-1])

def common_end(a, b):
    return(a[0]==b[0] or a[len(a)-1]==b[len(b)-1])

def sum3(nums):
    return(sum(nums))

def rotate_left3(nums):
    item = nums.pop(0)
    nums.insert(2, item)
    return nums
def reverse3(nums):
    nums.reverse()
    return nums
def max_end3(nums):
    big = max(nums[0],num[2])
    num[1]=num[2]=num[0]=big
    return(nums)
def sum2(nums):
    if len(nums)==0:
        return 0
    elif len(nums)==1:
        return sum(nums)
    else:
        sum = nums[0]+nums[1]
        return sum

def middle_way(a, b):
  return [a[1],b[1]]

def has23(nums):
  if 2 in nums or 3 in nums:
      return True
  else:
      return False
