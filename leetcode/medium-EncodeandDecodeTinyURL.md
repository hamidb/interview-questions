Encode and Decode TinyURL (Leetcode #535)
===============================
### Medium

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as
http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Solution
========

```python
class Codec:
    def __init__(self):
        self.base_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.url_table = {}
        random.seed()
        
    def generate_key(self):
        key = ''
        for i in range(6):
            key += self.base_string[random.randint(0, 61)]
        return key
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.generate_key()
        self.url_table[key] = longUrl
        return 'http://tinyurl.com/' + key
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl[-6:]
        return self.url_table[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

```
