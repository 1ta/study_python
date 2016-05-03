class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        left_B = 1
        B =[]
        for i in range(len(A)):
            if i == 0:
                left_B = 1
            else:
                left_B = left_B*A[i-1]
            right_B = 1
            for j in range(i+1,len(A)):
                right_B = right_B * A[j]
            result = left_B * right_B
            B.append(result)
        return B

print(Solution().productExcludeItself([1,2,4]))
