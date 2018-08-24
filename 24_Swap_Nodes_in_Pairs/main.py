#!/bin/python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        head = dummy 
        while head.next and head.next.next:
            n1, n2, n3 = head.next, head.next.next, head.next.next.next
            head.next = n2
            n2.next = n1
            n1.next = n3
            head = n1
            
        return dummy.next

if __name__ == '__main__':
    # Given:  1->2->3->4
    # Expect: 2->1->4->3
    d = ListNode(4)
    c = ListNode(3)
    b = ListNode(2)
    a = ListNode(1)
    a.next = b
    b.next = c
    c.next = d

    head = a
    while head != None:
        print head.val
        head = head.next
    print '------'

    head = a
    s = Solution()
    new_head = s.swapPairs(head)

    # Check result
    #print new_head
    while new_head != None:
        print new_head.val
        new_head = new_head.next

    
