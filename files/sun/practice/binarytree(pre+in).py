"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        def genTree(preorder,inorder):
            if len(preorder)==0:
                return None
            root_val = preorder[0]
            root = TreeNode(root_val)
            n = inorder.index(root_val)
            left_preorder = preorder[1:n+1]
            left_inorder = inorder[:n]
            right_preorder = preorder[n+1:]
            right_inorder= inorder[n+1:]
            if len(left_preorder) > 0:
                root.left = genTree(left_preorder, left_inorder)
            if len(right_preorder) > 0:
                root.right = genTree(right_preorder, right_inorder)
            return root
        root = genTree(preorder, inorder)
        return root
