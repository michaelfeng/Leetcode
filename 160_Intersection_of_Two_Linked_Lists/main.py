# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        if lenA > lenB:
            while headA and lenA != lenB:
                lenA -= 1
                headA = headA.next
        else:
            while headB and lenA != lenB:
                lenB -= 1
                headB = headB.next
            
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA    
        
    def getLength(self, head):
        ans = 0
        while head:
            ans += 1
            head = head.next
        return ans
