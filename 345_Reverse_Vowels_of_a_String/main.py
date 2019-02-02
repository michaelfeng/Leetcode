class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {'a':1,'e':1,'i':1,'o':1,'u':1, 'A':1,'E':1,'I':1,'O':1,'U':1}
        chars = []
        idxs = []
        for i in range(len(s)):
            if s[i] in d:
                chars.append(s[i])
                idxs.append(i)
        
        j = len(chars)-1
        for i in range(len(idxs)):
            s = s[:idxs[i]] + chars[j] + s[idxs[i]+1:]
            j -= 1
        
        return s
                
                
        
        
