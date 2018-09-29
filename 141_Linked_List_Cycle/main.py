#!/bin/python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        d = {}
        while head.next:
            if head in d: return True
            else:
                d[head] = head
            head = head.next
            
        return False
