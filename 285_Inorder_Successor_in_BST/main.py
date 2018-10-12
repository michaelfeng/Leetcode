"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root: return None
        self.inorder = []
        self.helper(root)
        
        # print self.inorder
        for i in xrange(len(self.inorder)):
            if i < len(self.inorder) - 1 and self.inorder[i].val == p.val:
                return self.inorder[i+1]
        return None   
        
    def helper(self, root):
        if not root: 
            return
        
        self.helper(root.left)
        self.inorder.append(root)
        self.helper(root.right)
        
        
        
        
        
    
