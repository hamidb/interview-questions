Regular Expression Matching (Leetcode #10)
===============================
### Hard
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

### Example 1:
```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

### Example 2:
```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

### Example 3:
```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 ```

### Constraints:
```
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
```

### Solution
```python
# T: O(mxn) size of s and p
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top Down DP with memoization
        @lru_cache(None)
        def dfs(i, j):
            # Base cases
            if i >= len(s) and j >= len(p):
                return True   # s=a  p= a
            if j >= len(p):
                return False  # s= aa  p= a
            # if i >= len(s)-> we don't know for example s="", p= "*a"

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j+1 < len(p) and p[j+1] == "*":                            
                choice1 = dfs(i, j+2)           # don't use the char before *
                choice2 = match and dfs(i+1, j) # use the char before *
                return choice1 or choice2
            if match:
                return dfs(i+1, j+1)
            return False
        
        return dfs(0, 0)

# # without lru_cache
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         # Top Down DP with memoization
#         cache = {}        
#         def dfs(i, j):
#             if (i, j) in cache:
#                 return cache[(i, j)]
#             # Base cases
#             if i >= len(s) and j >= len(p):
#                 return True   # s=a  p= a
#             if j >= len(p):
#                 return False  # s= aa  p= a
#             # if i >= len(s)-> we don't know for example s="", p= "*a"

#             match = i < len(s) and (s[i] == p[j] or p[j] == ".")
#             if j+1 < len(p) and p[j+1] == "*":                            
#                 choice1 = dfs(i, j+2)           # don't use the char before *
#                 choice2 = match and dfs(i+1, j) # use the char before *
#                 cache[(i, j)] = choice1 or choice2
#                 return cache[(i, j)]
#             if match:
#                 cache[(i, j)] = dfs(i+1, j+1)
#                 return cache[(i, j)]

#             cache[(i, j)] = False
#             return False
        
#         return dfs(0, 0)


```
