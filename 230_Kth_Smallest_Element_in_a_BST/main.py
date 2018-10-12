# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        inorder = []
        self.helper(root, inorder)
        if k > len(inorder):
            return None
        # print inorder
        return inorder[k-1]
        
    def helper(self, root, inorder):
        if not root:
            return inorder
        self.helper(root.left, inorder)
        inorder.append(root.val)
        self.helper(root.right, inorder)
