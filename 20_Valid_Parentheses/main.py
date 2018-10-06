class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == "{":
                stack.append("}")
            elif c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            else:
                if len(stack) == 0 or stack.pop() != c:
                    return False
        return len(stack) == 0
        
