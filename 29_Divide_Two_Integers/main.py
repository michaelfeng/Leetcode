class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0 or abs(dividend) < abs(divisor): 
            return 0
        isNeg = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            isNeg = True
        dividend, divisor = abs(dividend), abs(divisor)
        sumV = divisor
        multi = 1
        while sumV+sumV < dividend:
            sumV += sumV
            multi += multi
        ans = 0
        if isNeg:
            ans = - (multi + self.divide(dividend-sumV, divisor))
        else:
            ans = multi + self.divide(dividend-sumV, divisor)
        
        if ans > 2147483647:
            return 2147483647
        if ans < -2147483648:
            return -2147483648 
        return ans
