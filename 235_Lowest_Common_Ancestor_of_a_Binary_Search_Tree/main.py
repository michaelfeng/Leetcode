# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        node = self.helper(root, p, q)
        return node
    
    def helper(self, root, p, q):
        if not root: return
        if root == p or root == q: return root
        leftNode = self.helper(root.left, p, q)
        rightNode = self.helper(root.right, p, q)
        if leftNode and rightNode: return root
        if not leftNode: return rightNode
        if not rightNode: return leftNode
    
        
