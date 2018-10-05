class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        a = headA
        b = headB
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
       
