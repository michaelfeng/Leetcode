class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    Clarification
Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.
Example
If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.

Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
    """
    def strStr(self, source, target):
        # Write your code here
        if target == "" and source == "": return 0
        if target == "" and len(source) > 0: return 0
        if source == "" and len(target) > 0: return -1
        lt = len(target)
        i = 0
        while i < len(source) and i+lt <= len(source):
            print source[i:i+lt], target
            if source[i:i+lt] == target:
                return i
            else:
                i += 1
        return -1                
