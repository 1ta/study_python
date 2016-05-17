class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        def findlist(matrix,target):
            if matrix is None:
                return None
            if len(matrix) == 1:
                return matrix[0]
            for i in range(len(matrix)-1):
                if matrix[i][0]<= target< matrix[i+1][0]:
                    return matrix[i]
                if target >= matrix[-1][0]:
                    return matrix[-1]

        def searchlist(list,target):
            if list is None:
                return False
            if target in list:
                return True
            else:
                return False

        r = findlist(matrix,target)
        h = searchlist(r,target)
        return h
