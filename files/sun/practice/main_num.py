class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        for num in nums:
            if nums.count(num)>len(nums)/2:
                return num
