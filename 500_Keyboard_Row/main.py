class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dict = {'Q':0,'W':0,'E':0,'R':0,'T':0,'Y':0,'U':0,'I':0,'O':0,'P':0,
        'A':1,'S':1,'D':1,'F':1,'G':1,'H':1,'J':1,'K':1,'L':1,
        'Z':2,'X':2,'C':2,'V':2,'B':2,'N':2,'M':2}
        ans = []
        for word in words:
            s = set([])
            for c in word:
                row = dict[c.upper()]
                s.add(row)
            if len(s) == 1:
                ans.append(word)
        
        return ans
