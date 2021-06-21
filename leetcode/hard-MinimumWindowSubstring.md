Minimum Window Substring (Leetcode #76)
===============================
### Hard

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates)
is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.


### Example 1:
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

### Example 2:
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

### Example 3:
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 ```

### Constraints:
```
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 ```

Follow up: Could you find an algorithm that runs in O(m + n) time?

Solution
========

```python
# Since you have to find the minimum window in S which has all the characters from T, you need to expand and contract the window
# using the two pointers and keep checking the window for all the characters. This approach is also called Sliding Window Approach.
# L ------------------------ R , Suppose this is the window that contains all characters of T                         
# L----------------- R , this is the contracted window. We found a smaller window that still contains all the characters in T
# When the window is no longer valid, start expanding again using the right pointer.

# T: O(N+M)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        count = 0
        min_size = float('inf')
        min_str = ""
        l, r = 0, 0
        while r < len(s):
            t_count[s[r]] -= 1
            
            # s[r] is in t
            if t_count[s[r]] >= 0:
                count += 1
            
            # we have all t chars in substring
            if count == len(t):
                while l <= r and count == len(t):
                    if r-l+1 < min_size:
                        min_size = r - l + 1
                        min_str = s[l:r+1]
                    
                    # remove leftmost char from sub window
                    t_count[s[l]] += 1
                    # if the leftmost char being removed is in t
                    if t_count[s[l]] > 0:
                        count -= 1
                    l += 1
            r += 1
        return min_str
```
