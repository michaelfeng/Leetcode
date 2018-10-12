# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
    
    def helper(self, root):
        if not root:
            return None
        
        L = self.helper(root.left)
        R = self.helper(root.right)
        
        if L:
            L.right = root.right
            root.right = root.left
            root.left = None           
        
        if R:
            return R
        if L:
            return L
        
        return root
            
            
            
