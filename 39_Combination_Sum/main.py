class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(list(set(candidates)))
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result
    
    def dfs(self, candidates, target, idx, combination, result):
        if target == 0:
            return result.append(list(combination))
        for i in range(idx, len(candidates)):
            if target < candidates[i]:
                return
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, result)
            combination.pop()
        
