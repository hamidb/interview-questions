Decode Ways (Leetcode #91)
===============================
### Medium
A message containing letters from A-Z is being encoded to numbers using the following mapping:
```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```
Given a non-empty string containing only digits, determine the total number of ways to decode it.

### Example 1:
```
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```
### Example 2:
```
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```
Solution
========
```python
# "01" -> 0
# "10" -> 1
# "30" -> 0
# "00" -> 0
class Solution:
    # def numDecodings(self, s: str) -> int:
    #     size = len(s)
    #     if size == 0: return 0
    #     if size == 1: return 0 if s[0] == "0" else 1
    #     dp = size*[0]
    #     if s[0] == "0": return 0
    #     if s[1] == "0":
    #         if s[0] == "1" or s[0] == "2": 
    #             dp[0], dp[1] = 1, 1
    #         else: # 30, 40, ...
    #             return 0
    #     else:
    #         dp[0] = 1
    #         dp[1] = 2 if int(s[0:2]) <= 26 else 1
    #     for i in range(2, size):
    #         if s[i] == "0":
    #             if s[i-1] == "1" or s[i-1] == "2":
    #                 dp[i] = dp[i-2]
    #                 continue
    #             else: return 0
    #         dp[i] = dp[i-1]
    #         if int(s[i-1:i+1]) <= 26 and s[i-1] != "0":
    #             dp[i] += dp[i-2]
    #     return dp[-1]
    
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0 or s[0] == "0": return 0

        dp = [1, 1]
        for i in range(1, size):
            tmp = 0
            if s[i] != "0":
                tmp = dp[1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                tmp += dp[0]
            dp = [dp[1], tmp]
        return dp[1]
        
```
