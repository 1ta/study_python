"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        def match_tree(T1,T2):
            if T1 is None and T2 is None:
                return True
            if T1.val != T2.val:
                return False
            return match_tree(T1.left,T2.left) and match_tree(T1.right,T2.right)

        def subtree(T1, T2):
            if T1 is None:
                return False
            # if T1.val == T2.val:
            if match_tree(T1,T2):
                return True
            return subtree(T1.left,T2) or subtree(T1.right,T2)

        if T2 is None:
            return False
        return subtree(T1,T2)
