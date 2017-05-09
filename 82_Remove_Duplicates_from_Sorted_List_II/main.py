#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''
import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        pre = ListNode(-1)
        tail = pre
        q = head
        while q is not None:
            n = 0
            p = q
            while p is not None and p.val == q.val:
                n += 1
                p = p.next
            if n == 1:
                tail.next = q
                tail = tail.next
            q = p

        tail.next = None
        return pre.next
                            

if __name__ == '__main__':
    print 'Case 1:'
    node0 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(4)
    node6 = ListNode(5)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    sol = Solution()
    nodes = sol.deleteDuplicates(node0)
    while nodes is not None:
        print nodes.val
        nodes = nodes.next


    print 'Case 2: '
    node0 = ListNode(1)
    node1 = ListNode(1)
    node0.next = node1
    nodes = sol.deleteDuplicates(node0)
    while nodes is not None:
        print nodes.val
        nodes = nodes.next

    print 'Case 3: '
    node0 = ListNode(1)
    nodes = sol.deleteDuplicates(node0)
    while nodes is not None:
        print nodes.val
        nodes = nodes.next

    print 'Case 4: '
    node0 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(2)
    node0.next = node1
    node1.next = node2
    nodes = sol.deleteDuplicates(node0)
    while nodes is not None:
        print nodes.val
        nodes = nodes.next
