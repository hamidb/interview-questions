 Longest Happy Prefix (Leetcode #1392)
===============================
### Hard

A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string `s`, return the longest happy prefix of `s`. Return an empty string `""` if no such prefix exists.

 

### Example 1:
```
Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
```

### Example 2:
```
Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
```

### Example 3:
```
Input: s = "leetcodeleet"
Output: "leet"
```

### Example 4:
```
Input: s = "a"
Output: ""
 ```

### Constraints:
```
1 <= s.length <= 105
s contains only lowercase English letters.
```

Solution
========

```python
# T: O(N)
# T: worst case: hard to compute.
# S: O(M)
class Solution:
    def longestPrefix(self, s: str) -> str:
        L = len(s)
        if L <= 1:
            return ""
        lhp = L * [0]
        i = 1
        length = 0
        while i < L:
            if s[i] == s[length]:
                length += 1
                lhp[i] = length
                i += 1
            else:
                if length == 0:
                    lhp[i] = 0
                    i += 1
                else:
                    length = lhp[length-1]
        return s[-length:] if length != 0 else ""
```
