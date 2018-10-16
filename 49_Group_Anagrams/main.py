class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for word in strs:
            val = "".join(sorted(word))
            if val not in dict:
                dict[val] = [word]
            else:
                dict[val] += [word]
        
        ans = []
        for k, v in dict.items():
            ans.append(v)    
            
        # print ans
        return ans
        
