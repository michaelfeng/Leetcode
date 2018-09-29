# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        
        while pre.next and pre.next.next:
            if pre.next.val == pre.next.next.val:
                nextVal = pre.next.val
                while pre.next and nextVal == pre.next.val:
                    pre.next = pre.next.next
            else:    
                pre = pre.next
            
        return dummy.next
