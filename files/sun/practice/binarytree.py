"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        def genTree(inorder,postorder):
            if len(inorder)==0:
                return None
            root_val = postorder[-1]
            root = TreeNode(root_val)
            n = inorder.index(root_val)
            left_inorder = inorder[:n]
            left_postorder = postorder[:n]
            right_inorder = inorder[n+1:]
            right_postorder= postorder[n:len(postorder)-1]
            if len(left_inorder) > 0:
                root.left = genTree(left_inorder, left_postorder)
            if len(right_inorder) > 0:
                root.right = genTree(right_inorder, right_postorder)
            return root
        root = genTree(inorder, postorder)
        return root
