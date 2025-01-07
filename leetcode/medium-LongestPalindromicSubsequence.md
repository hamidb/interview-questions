Longest Palindromic Subsequence (Leetcode #516)
===============================
### Medium

Given a string `s`, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

### Example 1:
```
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
```

### Example 2:
```
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 ```

### Constraints:
```
1 <= s.length <= 1000
s consists only of lowercase English letters.
``` 

Solution
========

```python
# Longest palindromic subsequence = longest common subsequence of S and reverse S.
# Reverse the string.
# Find the longest common subsequence (LCS) between the original string and the reversed string.
# T: O(N^2)
# S: O(N^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        L = len(s)  
        reverse = s[::-1]
        @lru_cache(None)
        def lcs(i, j):
            if i >= L or j >= L:
                return 0
            if s[i] == reverse[j]:
                return 1 + lcs(i+1, j+1)
            else:
                return max(lcs(i+1, j), lcs(i, j+1))
        return lcs(0, 0)


        
```
