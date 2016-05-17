class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        def findlist(matrix,target):
            plist = []
            if matrix = None:
                return None
            for i in range (len(matrix)):
                if matrix[i][0] <= target:
                    plist.append(matrix[i])
            return plist

        def countno(ls,target):
            count = 0
            for j in ls:
                if target in j:
                    count = count + 1
            return count

        r = findlist(matrix,target)
        h = countno(r,target)
        return h
