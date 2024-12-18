Wildcard Matching (Leetcode #44)
===============================
### Hard

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

### Example 1:
```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

### Example 2:
```
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
```

### Example 3:
```
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```

### Constraints:
```
0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
```

### Solution

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            
            if i<len(s) and (p[j] == s[i] or p[j] == '?'):
                return dfs(i+1, j+1)
            if p[j] == '*':
                choice1 = dfs(i, j+1)
                choice2 = (i < len(s)) and dfs(i+1, j)
                return choice1 or choice2
            return False
        
        return dfs(0, 0)
```
