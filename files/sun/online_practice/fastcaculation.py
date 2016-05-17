class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n==0:
            return 1%b
        if a==0:
            return 0
        if a%b == 0:
            return 0
        temp = fastPower(a,b,int(n/2))
        if n%2 ==1:
            result = (temp**2 % b)*(a%b)
        else:
            result = temp**2 % b
        return result
