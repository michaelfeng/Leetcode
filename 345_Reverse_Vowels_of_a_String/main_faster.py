class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {'a':1,'e':1,'i':1,'o':1,'u':1, 'A':1,'E':1,'I':1,'O':1,'U':1}
        lst = list(s)
        vowels_str = "aeiouAEIOU"
        vowels_list = [item for item in lst if item in d]
        vowels_list.reverse()
        vowels_index = 0
        for index, item in enumerate(lst):
            if item in d:
                lst[index] = vowels_list[vowels_index]
                vowels_index += 1
        return ''.join(lst)
                
                
        
        
