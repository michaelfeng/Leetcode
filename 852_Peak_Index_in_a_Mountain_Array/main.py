class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        A[mid-1] > A[mid] --> hi = mid
        A[mid] < A[mid+1] --> lo = mid
        """
        
        lo, hi = 0, len(A)-1
        while lo < hi:
            mid = (lo+hi)//2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] < A[mid]:
                lo = mid
            elif A[mid] > A[mid+1]:
                hi = mid
            
        return mid
        
