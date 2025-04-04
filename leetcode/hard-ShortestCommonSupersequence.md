Shortest Common Supersequence (Leetcode #1092)
===============================
### Hard

Given two strings `str1` and `str2`, return the shortest string that has both `str1` and `str2` as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string `s`.

### Example 1:
```
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
```

### Example 2:
```
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
``` 

### Constraints:
```
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
```

### Solution

```python
# T: O(MxN)
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        L1 = len(str1)
        L2 = len(str2)
        @lru_cache(maxsize=None)
        def lcs(i, j):
            if i >= L1 or j >= L2:
                return ""
            if str1[i] == str2[j]:
                return str1[i] + lcs(i+1, j+1)
            else:
                seq1 = lcs(i+1, j)
                seq2 = lcs(i, j+1)
                return seq1 if len(seq1) > len(seq2) else seq2

        i, j = 0, 0
        ans = ""
        for c in lcs(0, 0):
            # add elements in str1 until str1[i] == c
            while str1[i] != c:
                ans += str1[i]
                i += 1
            # add elements in st2 until str2[j] == c
            while str2[j] != c:
                ans += str2[j]
                j += 1

            # add c and continue
            ans += c
            i += 1
            j += 1
        # add the remaining of str1 and str2 if there's any
        return ans + str1[i:] + str2[j:]

```
