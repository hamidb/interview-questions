Encode String with Shortest Length (Leetcode #471)
===============================
### Medium

Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times.

#### Note:

1. `k` will be a positive integer.

2. If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them.
 

### Example 1:
```
Input: s = "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
```

### Example 2:
```
Input: s = "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
```

### Example 3:
```
Input: s = "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
```

### Example 4:
```
Input: s = "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
```

### Example 5:
```
Input: s = "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
``` 

### Constraints:
```
1 <= s.length <= 150
s consists of only lowercase English letters.
```

Solution
========
* `case 1: s is not repeated -> use s (e.g. b -> b)`
* `case 2: s is repeated -> collapse to x[y] (e.g. aaaaa -> 5[a])`
* `case 3: slide a split point and split s into 2 piece and compute case 1, 2 (e.g. aaaaaabbbbb -> 6[a]5[b])`
* `take the minimum of case 1, 2, 3`

```python
# T: O(N^3)
# S: O(N^2)

# case 1: s is not repeated -> use s (e.g. b -> b)
# case 2: s is repeated -> collapse to x[y] (e.g. aaaaa -> 5[a])
# case 3: slide a split point and split s into 2 piece and compute case 1, 2 (e.g. aaaaaabbbbb -> 6[a]5[b])
# take the minimum of case 1, 2, 3
    
# Recursive solution
class Solution:
    def encode(self, s: str) -> str:
        dp = {}
        return self._encode(s, dp)
    
    def _encode(self, s, dp):
        if s in dp: return dp[s]
        n = len(s)
        if n < 4: return s
        
        # index of second occurance of the repeated pattern. And its frequency. 
        i = (s+s).find(s, 1)
        dp[s] = s
        if i < n:
            compress = str(n // i) + '[' + self._encode(s[:i], dp) + ']'
            if len(compress) < len(dp[s]):
                dp[s] = compress
        for p in range(1, n):
            splitted = self._encode(s[:p], dp) + self._encode(s[p:], dp)
            if len(splitted) < len(dp[s]):
                dp[s] = splitted
        return dp[s]
    
# Iterative solution
# class Solution:
#     def encode(self, s: str) -> str:
#         n = len(s)
#         if n < 4: return s
#         dp = [n*[''] for _ in range(n)]
        
#         for l in range(1, n+1):
#             for i in range(0, n-l+1):
#                 j = i+l-1
#                 t = s[i:i+l]
#                 pos = (t+t).find(t, 1)
#                 dp[i][j] = str(len(t) // pos) + '[' + dp[i][i+pos-1] + ']' if pos < len(t) else t
                
#                 for k in range(i, j):
#                     left, right = dp[i][k], dp[k+1][j]
#                     if len(left) + len(right) < len(dp[i][j]):
#                         dp[i][j] = left+right
     
#         return dp[0][n-1]

```
