# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        
        head = ListNode(-1)
        pre = head
        while heap:
            val = heapq.heappop(heap)
            pre.next = ListNode(val)
            pre = pre.next
        
        return head.next
            
        
        
        
        
