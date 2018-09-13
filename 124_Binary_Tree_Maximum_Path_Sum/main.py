# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = None
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.search(root)
        return self.ans
    
    def search(self, root):
        if root is None:
            return 0
        leftMax = self.search(root.left)
        rightMax = self.search(root.right)
        self.ans = max(max(leftMax, 0) + max(rightMax, 0) + root.val, self.ans)
        return max(leftMax, rightMax, 0) + root.val
        
