class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sp, pp = 0, 0
        star = -1
        match = 0
        while sp < len(s):
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == "?"):
                sp, pp = sp+1, pp+1
            elif pp < len(p) and p[pp] == "*":
                star = pp
                match = sp
                pp += 1
            elif star != -1:
                pp = star + 1
                match += 1
                sp = match
            else:
                return False
            
        while pp < len(p) and p[pp] == "*":
            pp += 1
            
        return pp == len(p)
