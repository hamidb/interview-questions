Implement strStr() (Leetcode #28)
===============================
### Easy

Implement `strStr()`.

Return the index of the first occurrence of needle in haystack, or `-1` if needle is not part of haystack.

### Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return `0` when needle is an empty string. This is consistent to C's `strstr()` and Java's `indexOf()`.

 

### Example 1:
```
Input: haystack = "hello", needle = "ll"
Output: 2
```

### Example 2:
```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

### Example 3:
```
Input: haystack = "", needle = ""
Output: 0
 ```

### Constraints:
```
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
```

Solution
========

```python

# KPM Knuth-Morris-Pratt algorithm.
# T: O(N+M)
# S: O(M)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # length of (proper) prefix that is also suffix.
        # T: O(M)  # average
        # T: Worst case is hard to compute.
        # S: O(M)
        def lps(needle):
            L = len(needle)
            lps = L * [0]
            i = 1
            l = 0
            while i < L:
                if needle[i] == needle[l]:
                    l += 1
                    lps[i] = l
                    i += 1
                else:
                    if l == 0:  # beginning and not matched.
                        lps[i] = 0
                        i += 1
                    else:
                        l = lps[l-1]  # tricky part
            return lps
            
        if needle == '':
            return 0
        L1 = len(haystack)
        L2 = len(needle)
        lps = lps(needle)
        i, j = 0, 0
        while i < L1:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j-1]  # length of (proper) prefix that is also suffix.
                else:
                    i += 1  # start of the pattern
            if j == L2:
                return i-j
        return -1


# # Brute force
# # T: O(MxN)
# # S: O(1) 
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> (int):
#         len_h = len(haystack)
#         len_n = len(needle)
#         if len_n > len_h:
#             return -1
#         i = 0
#         while i <= len_h - len_n:
#             if haystack[i:i + len_n] == needle:
#                 return i
#             i += 1
#         return -1
```
