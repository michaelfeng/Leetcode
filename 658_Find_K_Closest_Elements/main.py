class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr or len(arr) == 0: return []
        # l = len(arr)
        while len(arr) > k:
            if abs(arr[0] - x) > abs(arr[-1] - x):
                arr.pop(0)
            else:
                arr.pop(-1)
        return arr
            
