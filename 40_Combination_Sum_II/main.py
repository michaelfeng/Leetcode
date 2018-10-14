class Solution(object):
    def combinationSum2(self, num, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        if not num or len(num) == 0:
            return results
        num.sort()
        self.dfs(num, target, 0, [], results)
        return results
        
    def dfs(self, num, target, idx, subsets, results):
        if target == 0:
            return results.append(list(subsets))
        for i in range(idx, len(num)):
            if target < num[i]:
                return
            if i - 1 >= 0 and num[i] == num[i-1] and i > idx:
                continue
            subsets.append(num[i])
            self.dfs(num, target - num[i], i+1, subsets, results)
            subsets.pop()
