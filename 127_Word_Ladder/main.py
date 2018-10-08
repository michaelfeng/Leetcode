class Solution(object):
    def ladderLength(self, start, end, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = collections.deque([start])
        visit = set([start])
        dicts = set(wordList)
        # dicts.add(end)
        level = 0
        while queue:
            level += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return level
                for word in self.getTransforms(word):
                    if word in visit or word not in dicts:
                        continue
                    queue.append(word)
                    visit.add(word)
        return 0
    
    def getTransforms(self, word):
        res = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in string.ascii_lowercase:
                newWord = word[:i] + char + word[i+1:]
                if newWord != word:
                    res.append(newWord)
        return res
            
            
        
        
