Minumum Sum Path (Leetcode #64)
===============================
### Medium
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

### Example:
```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

Solution
========

```python
# DFS (Time Limit Exceeded)
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0]) if rows else 0
#         if rows == 0 or cols == 0:
#             return 0
        
#         sums = [[None for _ in range(cols)] for _ in range(rows)]
        
#         self.dfs(grid, 0, 0, 0, sums)
#         return sums[-1][-1]
    
#     def dfs(self, grid, i, j, prev_sum, sums):
#         if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
#             return

#         new_sum = prev_sum + grid[i][j]
#         if sums[i][j] is None:
#             sums[i][j] = new_sum
#         elif sums[i][j] > new_sum:
#             sums[i][j] = new_sum
#         else:
#             return

#         self.dfs(grid, i, j+1, sums[i][j], sums)
#         self.dfs(grid, i+1, j, sums[i][j], sums)

# Dijkstra's
# import heapq
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         dist = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
#         dist[0][0] = grid[0][0]
#         queue = [(dist[0][0], 0, 0)]
        
#         while queue:
#             v, i, j = heapq.heappop(queue)
#             for p, q in [[i+1, j], [i, j+1]]:
#                 if p < len(grid) and q < len(grid[0]):
#                     new_dist = v + grid[p][q]
#                     if new_dist < dist[p][q]:
#                         dist[p][q] = new_dist
#                         heapq.heappush(queue, (new_dist, p, q))
#                         if p == len(dist) - 1 and q == len(dist[0]) - 1:
#                             return dist[p][q]
#         return dist[-1][-1]

# Bottom Up
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        if rows == 0 or cols == 0:
            return 0
        
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, cols):
            dp[0][i] = dp[0][i-1] + grid[0][i]
            
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]
```
