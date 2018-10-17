class Solution(object):
    def search(self, A, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(A)-1
        if start < len(A) and A[start] == target:
            return True
        if end >= 0 and A[end] == target:
            return True
        
        while start <= end:
            while start < end and A[start] <= A[start+1]:
                start += 1
                if A[start] == target:
                    return True
            while end >= 1 and A[end] >= A[end-1]:
                end -= 1
                if A[end] == target:
                    return True
            
            if start < len(A) and A[start] == target:
                return True
            if end >= 0 and A[end] == target:
                return True
            
            start += 1
        return False
        
