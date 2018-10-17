class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        ans = []
        if len(nums1) > len(nums2):
            for num in nums2:
                if num in dict:
                    dict[num] += 1
                else:
                    dict[num] = 1
            for num in nums1:
                if num in dict:
                    if dict[num] == 0:
                        del dict[num]
                    else:
                        dict[num] -= 1
                        ans.append(num)
        else:
            for num in nums1:
                if num in dict:
                    dict[num] += 1
                else:
                    dict[num] = 1
            for num in nums2:
                if num in dict:
                    if dict[num] == 0:
                        del dict[num]
                    else:
                        dict[num] -= 1
                        ans.append(num)
        return ans
