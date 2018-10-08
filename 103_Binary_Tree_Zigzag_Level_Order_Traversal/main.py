# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = collections.deque([root])
        ans = []
        leftToRight = False
        while queue:
            res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            leftToRight = not leftToRight
            
            if leftToRight:
                ans.append(res)
            else:
                res.reverse()
                ans.append(res)
            
        return ans
        
