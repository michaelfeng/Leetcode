class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        dict = {0:-1}
        leng, prefix_sum = 0, 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum-k in dict:
                leng = max(leng, i - dict[prefix_sum-k])
            
            if prefix_sum not in dict:
                dict[prefix_sum] = i
 
        return leng
                
