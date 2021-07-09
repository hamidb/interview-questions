Longest Repeating Substring (Leetcode #1062)
===============================
### Medium

Given a string `s`, find out the length of the longest repeating `substring(s)`. Return `0` if no repeating substring exists.

 

### Example 1:
```
Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.
```

### Example 2:
```
Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
```

### Example 3:
```
Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
```

### Example 4:
```
Input: s = "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
 ```

### Constraints:
```
The string s consists of only lowercase English letters from 'a' - 'z'.
1 <= s.length <= 1500
```

Solution
========

```python
# Binary search + rolling hash (Rabin-Karp)
# T: O(N log N)
# S: O(N)
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        N = len(s)
        base = 31
        mod = 10**9 + 7
        def check_rabin_karp(s, L):
            mod_inv = base**(L-1) % mod
            h = 0
            for i in range(L):
                h = (h*base + s[i]) % mod
            
            seen = {h}
            for i in range(1, N-L+1):
                h = ((h - s[i-1]*mod_inv)*base + s[i+L-1]) % mod
                if h < 0: h += mod
                if h in seen:
                    return True
                seen.add(h)
            return False
        
        arr = [ord(a)-ord('a') for a in s]
        lo, hi = 1, N
        ans = 0
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if check_rabin_karp(arr, mid):
                lo = mid + 1
                ans = max(ans, mid)
            else:
                hi = mid - 1
        return ans

# # Binary search + hash map
# # T: O(N^2 log N)
# # S: O(N)
# class Solution:
#     def longestRepeatingSubstring(self, s: str) -> int:
#         N = len(s)
#         def check(s, L):
#             seen = set()
#             for i in range(N-L+1):
#                 ss = s[i:i+L]
#                 if ss in seen:
#                     # for j in seen[ss]:
#                     #     if ss == s[j:j+L]:
#                     return True
#                 seen.add(ss)
#             return False
        
#         lo, hi = 1, N
#         ans = 0
#         while lo <= hi:
#             mid = lo + (hi-lo) // 2
#             if check(s, mid):
#                 lo = mid + 1
#                 ans = max(ans, mid)
#             else:
#                 hi = mid - 1
#         return ans
```
