# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        flat = []
        self.inorder(root, flat)
        vals = sorted([x.val for x in flat])
        for i in range(len(flat)):
            flat[i].val = vals[i]
            
    def inorder(self, root, flat):
        if not root: return
        self.inorder(root.left, flat)
        flat.append(root)
        self.inorder(root.right, flat)
        
