Unique Paths (Leetcode #62)
===============================
### Medium

A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a `7 x 3` grid.

### Example 1:
```
Input: m = 3, n = 2
Output: 3
```
Explanation:

From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
### Example 2:
```
Input: m = 7, n = 3
Output: 28
```

### Constraints:
`1 <= m, n <= 100`
It's guaranteed that the answer will be less than or equal to `2 * 10 ^ 9`.

Solution
========
```python
class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return self.dfs(0, 0, m, n)
    
#     def dfs(self, col, row, m, n):
#         if row == n-1 and col == m-1:
#             return 1
#         count = 0
#         if row < n-1:
#             count += self.dfs(col, row+1, m, n)
#         if col < m-1:
#             count += self.dfs(col+1, row, m, n)
#         return count

# Bottom up
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(m+1)] for j in range(n+1)]
        grid[1][1] = 1
        row = 1
        while row < n+1:
            col = 1
            while col < m+1:
                if col == 1 and row == 1:
                    col += 1
                    continue
                grid[row][col] = grid[row-1][col] + grid[row][col-1]
                col += 1
            row += 1
        return grid[n][m]
```
