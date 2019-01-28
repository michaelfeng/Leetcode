class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        d = {}
        for i,c in enumerate(S):
            d[c] = i
        ans = []
        start, last = 0, 0
        for i in range(len(S)):
            last = max(last,d[S[i]])
            if i == last:
                ans.append(last-start+1)
                start = i+1
                
        return ans
