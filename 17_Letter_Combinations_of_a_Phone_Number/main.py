KEYBOARD = {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r','s'],
    '8': ['t','u','v'],
    '9': ['w','x','y','z'],
}
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        results = []
        self.dfs(digits, 0, "", results)
        return results
    
    def dfs(self, digits, idx, stringlist, results):
        if idx == len(digits):
            results.append(stringlist)
            return 
        for char in KEYBOARD[digits[idx]]:
            self.dfs(digits, idx+1, stringlist+char, results)
        
        
