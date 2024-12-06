Encode String with Shortest Length (Leetcode #471)
===============================
### Hard

Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times.

#### Note:

1. `k` will be a positive integer.

2. If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them.
 

### Example 1:
```
Input: s = "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
```

### Example 2:
```
Input: s = "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
```

### Example 3:
```
Input: s = "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
```

### Example 4:
```
Input: s = "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
```

### Example 5:
```
Input: s = "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
``` 

### Constraints:
```
1 <= s.length <= 150
s consists of only lowercase English letters.
```

Solution
========
* `case 1: s is not repeated -> use s (e.g. b -> b)`
* `case 2: s is repeated -> collapse to x[y] (e.g. aaaaa -> 5[a])`
* `case 3: slide a split point and split s into 2 piece and compute case 1, 2 (e.g. aaaaaabbbbb -> 6[a]5[b])`
* `take the minimum of case 1, 2, 3`

### GPT solution
Use a DP table dp[i][j] to represent the shortest encoded string for the substring s[i:j+1].

Steps:

Base Case:

* If the substring length is 1, dp[i][j] = s[i:j+1].

Check for Repetition:
* For a substring s[i:j+1], check if it can be formed by repeating a smaller substring. For example:
"aaaa" → "4[a]".

* Check all possible segment lengths k, such that k divides the substring length L.

Partition the Substring:
* Divide the substring into two parts at every possible position k and combine the results:
  
* dp[i][j] = dp[i][k] + dp[k+1][j].

Choose the Shortest:
* For each substring s[i:j+1], store the shortest encoding.
  
```python
def encode(s: str) -> str:
    n = len(s)
    dp = [[""] * n for _ in range(n)]
    
    for length in range(1, n + 1):  # Length of the substring
        for i in range(n - length + 1):  # Start index
            j = i + length - 1  # End index
            substring = s[i:j+1]
            
            # Initialize with the substring itself
            dp[i][j] = substring
            
            # Try splitting the substring into two parts
            for k in range(i, j):
                if len(dp[i][k]) + len(dp[k+1][j]) < len(dp[i][j]):
                    dp[i][j] = dp[i][k] + dp[k+1][j]
            
            # Try encoding the entire substring
            for k in range(1, length // 2 + 1):  # k is the segment length
                if length % k == 0 and substring[:k] * (length // k) == substring:
                    encoded = f"{length // k}[{dp[i][i + k - 1]}]"
                    if len(encoded) < len(dp[i][j]):
                        dp[i][j] = encoded

    return dp[0][n-1]

```

```python
# T: O(N^3)
# S: O(N^2)

# case 1: s is not repeated -> use s (e.g. b -> b)
# case 2: s is repeated -> collapse to x[y] (e.g. aaaaa -> 5[a])
# case 3: slide a split point and split s into 2 piece and compute case 1, 2 (e.g. aaaaaabbbbb -> 6[a]5[b])
# take the minimum of case 1, 2, 3
    
# Recursive solution
class Solution:
    def encode(self, s: str) -> str:
        dp = {}
        return self._encode(s, dp)
    
    def _encode(self, s, dp):
        if s in dp: return dp[s]
        n = len(s)
        if n < 4: return s
        
        # index of second occurance of the repeated pattern. And its frequency. 
        i = (s+s).find(s, 1)
        # if i N n then it means s is a repeating pattern.
        dp[s] = s
        if i < n:
            compress = str(n // i) + '[' + self._encode(s[:i], dp) + ']'
            if len(compress) < len(dp[s]):
                dp[s] = compress
        for p in range(1, n):
            splitted = self._encode(s[:p], dp) + self._encode(s[p:], dp)
            if len(splitted) < len(dp[s]):
                dp[s] = splitted
        return dp[s]
    
# Iterative solution
# class Solution:
#     def encode(self, s: str) -> str:
#         n = len(s)
#         if n < 4: return s
#         dp = [n*[''] for _ in range(n)]
        
#         for l in range(1, n+1):
#             for i in range(0, n-l+1):
#                 j = i+l-1
#                 t = s[i:i+l]
#                 pos = (t+t).find(t, 1)
#                 dp[i][j] = str(len(t) // pos) + '[' + dp[i][i+pos-1] + ']' if pos < len(t) else t
                
#                 for k in range(i, j):
#                     left, right = dp[i][k], dp[k+1][j]
#                     if len(left) + len(right) < len(dp[i][j]):
#                         dp[i][j] = left+right
     
#         return dp[0][n-1]

```
