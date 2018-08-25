class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        # length of string
        s_l = len(s)
        # word count
        w_c = len(words)
        # word length
        w_l = len(words[0])
        d = dict.fromkeys(words, 0)
        for word in words:
            d[word] = d[word]+1

        # end index
        e_i = s_l - w_c * w_l;
        for i in range(0, e_i+1):
            state = dict.fromkeys(words, 0)
            count = 0
            for j in range(0, w_c):
                w = s[i+j*w_l:i+(j+1)*w_l]
                if w in d:
                    state[w] = state[w] + 1
                    if state[w] > d[w]:
                        break
                    count = count + 1 
            if count == w_c:
                res.append(i)
        return res

if __name__ == '__main__':
    s = "wordgoodgoodgoodbestword"
    w = ["word","good","best","good"]
    '''
    s = "barfoothefoobarman"
    w = ["foo","bar"]'''
    print Solution().findSubstring(s,w)
