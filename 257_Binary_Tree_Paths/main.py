# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        if not root.left and not root.right:
            return [str(root.val)]
        
        paths = []
        # paths.append(str(root.val))
        if root.left:
            for path in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + "->" + path)
            
        if root.right:
            for path in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + "->" + path)
        
        return paths
            
