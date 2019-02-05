# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        queue = [root]
        res = [root.val]
        while queue:
            tmp = []
            while queue:
                node = queue.pop(0)
                if node.left: 
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)   
            if tmp:
                res.append(tmp[-1].val)
            queue = tmp
        return res
