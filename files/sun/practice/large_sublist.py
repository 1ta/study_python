class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        large_sum = None
        for n in range(1,len(nums)+1):
            for i in range(len(nums)-n):
                sum_num = sum(nums[i:i+n])
                if sum_num > large_sum:
                    large_sum = sum_num

        return large_sum

print (Solution().maxSubArray([-1,4,9]))
