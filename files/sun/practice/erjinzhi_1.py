class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        count = 0
        while num != 0:
            if num%2 == 1:
                count += 1
            num = num/2
        return count

print(Solution().countOnes(32))
