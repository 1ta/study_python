class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        if len(nums)< 4:
            return sum(nums)
        else:
            cache=[]
            for i in range(len(nums)-3):
                sum_num = nums[i]+nums[i+1]+nums[i+2]+nums[i+3]
                cache.append(sum_num)
            return max(cache)



print (Solution().maxSubArray([-1,4]))
