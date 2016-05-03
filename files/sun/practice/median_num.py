class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        mid = int(len(nums)/2)
        nums.sort()
        if len(nums)%2 ==0:
            return nums[mid-1]
        else:
            return nums[mid]

print (Solution().median([7,9,4,5,8]))
