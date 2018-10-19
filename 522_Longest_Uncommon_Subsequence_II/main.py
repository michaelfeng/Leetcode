class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        if not strs: return -1
        
        results = set([])
        minLen = float('inf')
        for i in range(len(strs)):
            self.dfs(strs[i], "", results)
            if len(strs[i]) < minLen:
                minLen = len(strs[i])
            
        # print results
        ans = []
        for substr in results:
            isCommon = False
            dupCount = 0
            for candidate in strs:
                if substr == candidate:
                    dupCount += 1
                elif candidate.find(substr) != -1:
                    isCommon = True
                    break
            if not isCommon and dupCount < 2:
                ans.append(substr)
        
        # print ans
        maxV = -1
        for s in ans:
            if len(s) > maxV:
                maxV = len(s)
        
        return maxV
        
            
    
    def dfs(self, s, substrs, results):
        if substrs:
            results.add(substrs)
        
        for i in range(1,len(s)+1):
            self.dfs(s[i:], substrs + s[:i], results)
        
