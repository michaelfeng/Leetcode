#!/bin/python

class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0: return 0

        res_sum = 0
        ans = 0
        m = {}
        #print(m)
        for i,v in enumerate(nums):
            res_sum +=  -1 if v == 0 else 1
            if res_sum == 0:
                ans = i + 1
            elif res_sum in m:
                ans = max(ans, i - m[res_sum])
            else:
                m[res_sum] = i

            #print(m)
        return ans
                    

            

if __name__ == "__main__":
    nums = [0,1]    # 2
    #nums = [0,1,0] # 2
    nums = [0,0,1]  # 2
    print(Solution().findMaxLength(nums))
