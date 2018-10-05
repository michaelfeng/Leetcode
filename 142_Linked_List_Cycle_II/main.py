# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return None
        slow, fast = head, head
        while fast:
            if not fast.next: return None
            slow = slow.next
            fast = fast.next.next  
            if slow == fast: 
                break
        slow = head
        while fast and slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
