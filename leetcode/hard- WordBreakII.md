 Word Break II (Leetcode #140)
===============================
### Hard

Given a string s and a dictionary of strings `wordDict`, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

### Example 1:
```
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
```

### Example 2:
```
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
```

### Example 3:
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
``` 

### Constraints:
```
1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
```

Solution
========

```python
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         words = set(wordDict)
#         memo = defaultdict(list)
#         def recurse(s):
#             if len(s) == 0:
#                 return [[]]
#             if s in memo:
#                 return memo[s]
            
#             for i in range(1, len(s)+1):
#                 prefix = s[:i]
#                 if prefix in words:
#                     for suffix in recurse(s[i:]):
#                         memo[s].append([prefix]+suffix)
#             return memo[s]
        
#         recurse(s)
#         return [' '.join(words) for words in memo[s]]

# T: O(N^2 + 2^N + W)
# S: O(N * 2^N + W)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)  # O(W)

        @lru_cache(None)  # worst case: 2^N combinations each N chars
        def recurse(idx):
            if idx == len(s):
                return [""]
            res = []
            for i in range(1, len(s)+1):
                prefix = s[idx:i]
                if prefix in words:
                    for suffix in recurse(i):
                        if len(suffix) != 0: 
                            res.append(prefix+" "+suffix)
                        else:
                            res.append(prefix)
            return res
        return recurse(0)
        
```
