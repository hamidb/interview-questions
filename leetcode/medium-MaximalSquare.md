Maximal Square (Leetcode #221)
===============================
### Medium

Given an `m x n` binary matrix filled with `0`'s and `1`'s, find the largest square containing only `1`'s and return its area.
 

### Example 1:
![ex](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)
```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
```

### Example 2:
![ex2](https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg)
```
Input: matrix = [["0","1"],["1","0"]]
Output: 1
```

### Example 3:
```
Input: matrix = [["0"]]
Output: 0
 ```

### Constraints:
```
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
```

Solution
========
```python
# # T: O(MxN)
# # S: O(MxN)
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         rows, cols = len(matrix), len(matrix[0])
#         dp = [(cols+1)*[0] for _ in range(rows+1)]
        
#         ans = 0
#         for c in range(cols-1, -1, -1):
#             for r in range(rows-1, -1, -1):
#                 if matrix[r][c] == "0":
#                     continue
#                 dp[r][c] = 1 + min(dp[r+1][c+1], dp[r][c+1], dp[r+1][c])
#                 ans = max(ans, dp[r][c])
#         return ans*ans

# T: O(MxN)
# S: O(N)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = (rows+1)*[0] 
        ans, prev = 0, 0
        for c in range(cols-1, -1, -1):
            for r in range(rows-1, -1, -1):
                tmp = dp[r]
                if matrix[r][c] != "0":
                    dp[r] = 1 + min(dp[r], dp[r+1], prev)
                    ans = max(ans, dp[r])
                else:
                    dp[r] = 0
                prev = tmp
        return ans*ans
```
