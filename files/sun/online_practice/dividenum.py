class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] % 2 == 0:
                temp = nums[i]
                nums[i] = nums [j]
                nums[j] = temp
                j = j-1
            else:
                i = i+1
        return nums


ls = [402,25,42,538,741,473,310,112,682,622,287,242,439]
h = Solution().partitionArray(ls)
print(h)
