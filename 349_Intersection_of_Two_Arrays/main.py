class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        ans = set([])
        if len(nums1) > len(nums2):
            for num in nums2:
                if num in dict:
                    continue
                dict[num] = 0
            for num in nums1:
                if num in dict:
                    ans.add(num)
        else:
            for num in nums1:
                if num in dict:
                    continue
                dict[num] = 0
            for num in nums2:
                if num in dict:
                    ans.add(num)
        return list(ans)
            
