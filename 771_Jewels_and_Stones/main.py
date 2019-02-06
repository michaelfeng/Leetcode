class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict = {J[i]:1 for i in range(len(J))}
        ans = 0
        for i in range(len(S)):
            if S[i] in dict:
                ans += 1
        return ans 
        
