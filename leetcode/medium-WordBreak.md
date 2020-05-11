Word Break (Leetcode #139)
===============================
### Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
### Example 1:

```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
```
Explanation: Return true because "leetcode" can be segmented as "leet code".
### Example 2:
```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
```
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
### Example 3:
```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

Solution
========
![Bottom up approach](images/image0009.png)
![Memoization approach](images/image0010.png)

```python
class Solution:
# O(n^2) (Memoization)
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         seen = {}
#         return self._wordBreak(s, wordDict, seen)

#     def _wordBreak(self, s: str, wordDict: List[str], seen) -> bool:
#         if s in wordDict:
#             return True
#         if s in seen:
#             return seen[s]
#         for i in range(len(s)):
#             if s[0:i+1] in wordDict and self._wordBreak(s[i+1:], wordDict, seen):
#                 seen[s[i+1:]] = True
#                 return True
#         seen[s] = False
#         return False

# O(n^2) (DP bottom up)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        wb = [False for _ in range(0, len(s)+1)]
        wb[0] = True
        for i in range(1, len(s)+1):
            if s[0:i] in wordDict:
                wb[i] = True
                continue
            for j in range(0, i):
                if wb[j] and s[j:i] in wordDict:
                    wb[i] = True
                    break
        return wb[-1]
```
