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
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        self.inorder = []
        self.helper(root)
        return self.get_k_closet(self.inorder, target, k)
        
    def helper(self, root):
        if not root: return None
        self.helper(root.left)
        self.inorder.append(root.val)
        self.helper(root.right)
    
    def get_k_closet(self, arr, target, k):
        left, right = 0, len(arr)-1
        
        while left + 1 < right:
            if arr[left] <= target:
                left += 1
            else:
                right -= 1
                
        
        while len(arr) != k:
            if abs(arr[0]-target) > abs(target-arr[-1]):
                arr.pop(0)
            else:
                arr.pop()
       
        return arr     
            
