Repeated String Match (Leetcode #686)
===============================
### Medium

Given two strings `a` and `b`, return the minimum number of times you should repeat string `a` so that string `b` is a substring of it. If it is impossible for
`b` to be a substring of `a` after repeating it, return `-1`.

Notice: string `"abc"` repeated `0` times is `""`,  repeated `1` time is `"abc"` and repeated `2` times is `"abcabc"`.

 

### Example 1:
```
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
```

### Example 2:
```
Input: a = "a", b = "aa"
Output: 2
```

### Example 3:
```
Input: a = "a", b = "a"
Output: 1
```

### Example 4:
```
Input: a = "abc", b = "wxyz"
Output: -1
``` 

### Constraints:
```
1 <= a.length <= 104
1 <= b.length <= 104
a and b consist of lower-case English letters.
```

Solution
========

```python
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        la, lb = len(a), len(b)
        if lb == 0:
            return 0
        if la == 0:
            return -1
            
        if len(set(b)-set(a)) > 0:
            return -1

        def helper(ia, a, b, la, lb):
            ans = 1
            ib = 0
            while ia < la and ib < lb:
                if a[ia] != b[ib]:
                    return -1
                ia += 1
                ib += 1
                if ia == la and ib < lb:
                    ans += 1
                    ia = 0
            return ans
        
        for ia in range(la):
            if a[ia] == b[0]:
                ans = helper(ia, a, b, la, lb)
                if ans != -1:
                    return ans
        return -1

# KPM string matching
# T: O(N+M)
# S: O(N)
# Keep repeating a, until b is present in a or a length < b.
# For string comparion used KMP instead of contains() method.
# Note: contains(): Time complexity is (O(m*n)). Where as, KMP Time complexity is (O(m + n)).

# class Solution:
#     def repeatedStringMatch(self, a: str, b: str) -> int:
#         def kpm(a, b):  # is b in a ?
#             lps = len(b) * [0]
#             l, i = 0, 1
#             while i < len(b):
#                 if b[i] == b[l]:
#                     l += 1
#                     lps[i] = l
#                     i += 1
#                 else:
#                     if l == 0:
#                         lps[i] = 0
#                         i += 1
#                     else:
#                         l = lps[l-1]
#             i, j = 0, 0
#             while i < len(a):
#                 if a[i] == b[j]:
#                     i += 1
#                     j += 1
#                 else:
#                     if j == 0:
#                         i += 1
#                     else:
#                         j = lps[j-1]
#                 if j == len(b):
#                     return True
#             return False
            
#         la, lb = len(a), len(b)
#         if lb == 0:
#             return 0
#         if la == 0:
#             return -1

#         ans = 1
#         tmp_a = a
#         while la < lb:
#             a += tmp_a
#             la = len(a)
#             ans += 1
            
#         if kpm(a, b):
#             return ans
#         if kpm(a+tmp_a, b):
#             return ans + 1
#         return -1
```
