import string
import random
class Codec:

    def __init__(self):
        self.chars = [c for c in string.digits] + [c for c in string.letters]
        self.urlMap = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        alias = ""
        for i in range(6):
            alias += self.chars[random.randint(0, len(self.chars)-1)]
        self.urlMap[alias] = longUrl
        print alias
        return "https://tinyurl.com/"+ alias

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urlMap[shortUrl.split('/')[-1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
