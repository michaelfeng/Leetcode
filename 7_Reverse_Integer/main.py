class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNeg = False
        if x < 0:
            isNeg = True
        s = str(x)
        if isNeg:
            s = s[1:]
        arr = list(reversed(s))            
        ans = ''.join(str(x) for x in arr)
        print ans
        if isNeg:
            ans = -1 * float(ans)
        else:
            ans = float(ans)
        
        if ans > ((2<<30)  - 1):
            return 0
        elif ans < (-2<<30):
            return 0
       
        return int(ans)    
        
