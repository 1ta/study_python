class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        def FindCross(nums,left,right):
            mid = int((left+right+1)/2)
            l_sum,sum_l = -float("inf"),0
            for i in nums[left:mid][::-1]:
                sum_l += i
                if sum_l > l_sum:
                    l_sum = sum_l
            r_sum,sum_r = -float("inf"),0
            for j in nums[mid:right]:
                sum_r += j
                if sum_r > r_sum:
                    r_sum = sum_r
            return l_sum+r_sum
        def FindSubArr(nums, left, right):
            if left == right - 1:
                return nums[left]
            else:
                mid = int((right + left + 1) /2)
                l_sum = FindSubArr(nums, left, mid)
                r_sum = FindSubArr(nums, mid, right)
                c_sum = FindCross(nums, left, right)
                print([l_sum, r_sum , c_sum])
            return max([l_sum, r_sum , c_sum])
        left = 0
        right = len(nums)
        if right <= 1:
            return sum(nums)
        return FindSubArr(nums,left,right)


print (Solution().maxSubArray([-1,4,9]))
