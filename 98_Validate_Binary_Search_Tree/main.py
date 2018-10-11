# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, min=float('-inf'), max = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return min <= root.val < max and self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val+1, max)
        
