class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y): return cmp(y+x, x+y)
        if all(n == 0 for n in nums): return '0'
        return ''.join(sorted((str(n) for n in nums), cmp=compare))
        
        
