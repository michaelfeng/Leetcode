"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        sum = 0
        depth = 1
        queue = collections.deque([])
        for n in nestedList:
            queue.append((n, 1))
        
        while queue:
            node, dep = queue.popleft()
            if node and node.isInteger():
                sum += node.getInteger()*dep
            else:
                lists = node.getList()
                for i in lists:
                    queue.append((i, dep+1))
                
        return sum
            
