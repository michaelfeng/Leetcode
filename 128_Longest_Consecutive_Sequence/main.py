class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        l, r, maxV = 0, 0, 0
        for num in nums:
            if num not in dict:
                l = dict.get(num-1, 0)
                r = dict.get(num+1, 0)
                leng = l+r+1
                
                maxV = max(leng, maxV)
                
                dict[num] = leng
                dict[num-l] = leng
                dict[num+r] = leng      
                
        return maxV
