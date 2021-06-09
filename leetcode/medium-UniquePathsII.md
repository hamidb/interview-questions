Unique Paths II (Leetcode #63)
===============================
### Medium

A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as `1` and `0` respectively in the grid.

Note: `m` and `n` will be at most 100.

### Example 1:
```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
```
Explanation:

There is one obstacle in the middle of the `3x3` grid above.

There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Solution
========
```python
class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         rows = len(obstacleGrid)
#         cols = len(obstacleGrid[0]) if rows != 0 else 0
#         if rows == 0 or cols == 0:
#             return 0
#         return self.dfs(obstacleGrid, 0, 0, rows, cols)
        
#     def dfs(self, grid, r, c, rows, cols):
#         if grid[r][c] == 1:
#             return 0
#         if r == rows-1 and c == cols-1:
#             return 1
#         count = 0
#         if c < cols-1:
#             count += self.dfs(grid, r, c+1, rows, cols)
#         if r < rows-1:
#             count += self.dfs(grid, r+1, c, rows, cols)
#         return count
    
# Bottom up
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0]) if rows else 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        grid = [(cols+1)*[0] for _ in range(rows+1)]
        grid[1][1] = 1
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if (r == 1 and c == 1) or obstacleGrid[r-1][c-1] == 1:
                    continue
                grid[r][c] = grid[r][c-1] + grid[r-1][c]
        return grid[-1][-1]
        
```
