# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder = []
        self.helper(root)
        return self.inorder
        
    def helper(self, root):
        if not root:
            return None
        self.helper(root.left)
        self.inorder.append(root.val)
        self.helper(root.right)
        
