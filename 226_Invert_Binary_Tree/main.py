# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return root
        
    def dfs(self, root):
        if not root: return
        root.left, root.right = root.right, root.left
        if root.right: self.dfs(root.right)
        if root.left: self.dfs(root.left)
        
        
