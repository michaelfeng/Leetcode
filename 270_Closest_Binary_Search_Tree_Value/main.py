"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        self.closestVal = None
        self.distance = float('inf')
        self.helper(root, target)
        return self.closestVal
    
    def helper(self, root, target):
        if not root: return None
        self.helper(root.left, target)
        if abs(root.val - target) < self.distance:
            self.distance = abs(root.val - target)
            self.closestVal = root.val
        self.helper(root.right, target)
        
