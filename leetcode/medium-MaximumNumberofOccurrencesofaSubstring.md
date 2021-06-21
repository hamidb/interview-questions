Maximum Number of Occurrences of a Substring (Leetcode #1297)
===============================
### Medium

Given a string `s`, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to `maxLetters`.
The substring size must be between `minSize` and `maxSize` inclusive.
 

### Example 1:
```
Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
```

### Example 2:
```
Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
```

### Example 3:
```
Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3
```

### Example 4:
```
Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0
 ```

### Constraints:
```
1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s only contains lowercase English letters.
```

Solution
========

```python

# We move a sliding window of size minSize from 0 to the end keeping track of all character occurences.
# This will optimize out the need to loop for calculating maxLetters condition.
# Same as above. But since we always look for max of results. We don't need to go all the way to maxSize.
# if minSize is computed, any size bigger than it can not hold a better result.
# T: O(N)
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        result = 0
        L = len(s)
        mp = defaultdict(int)
        counter = defaultdict(int)
        # sliding win of size = minSize
        for i in range(L):
            counter[s[i]] += 1
            if i < minSize - 1:
                continue
            if len(counter.keys()) <= maxLetters:
                sub = s[i-minSize+1:i+1]
                mp[sub] += 1
                result = max(result, mp[sub])
            c_id = s[i-minSize+1]
            counter[c_id] -= 1
            if counter[c_id] == 0:
                del counter[c_id]
        return result
        
# # T: O(N^3) -> O(N^2 x maxSize)
# class Solution: 
#     def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
#         result = 0
#         L = len(s)
#         mp = defaultdict(int)
#         # sliding win of size = minSize
#         for i in range(L-minSize+1):
#             j = i + minSize - 1
#             while j <= i + maxSize - 1 and j < L:
#                 sub = s[i:j+1]
#                 letters = len(set(list(sub)))
#                 if letters > maxLetters:
#                     break
#                 mp[sub] += 1
#                 result = max(result, mp[sub])
#                 j += 1
#         return result

# # Same as above. But since we always look for max of results. We don't need to go all the way to maxSize.
# # if minSize is computed, any size bigger than it can not hold a better result.
# # T: O(N x maxSize)
# class Solution:
#     def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
#         result = 0
#         L = len(s)
#         mp = defaultdict(int)
#         # sliding win of size = minSize
#         for i in range(L-minSize+1):
#             j = i + minSize - 1
#             sub = s[i:j+1]
#             letters = len(set(list(sub)))
#             if letters > maxLetters:
#                 continue
#             mp[sub] += 1
#             result = max(result, mp[sub])
#         return result
```
