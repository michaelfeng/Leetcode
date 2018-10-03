class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == "" and B == "": return True
        if not A or not B: return False
        if A == B: return True

        l = len(A) - 1
        s = ""
        i = 0
        while i <= l:
            A = A[l] + A[0:l]
            if A == B:
                return True
            i += 1
            #print A
        return False
