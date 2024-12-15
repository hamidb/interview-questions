Shortest Path in Binary Matrix (Leetcode #1091)
===============================
### Medium

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

### Example 1:
```
Input: grid = [[0,1],[1,0]]
Output: 2
```
### Example 2:
```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```
### Example 3:
```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```

### Constraints:
```
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
```

Solution
========

```python

# dijkstra
#Time Complexity: O(NlogN) (N = rows*cols)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        if grid[0][0] == 1:
            return -1
        visited = [cols*[0] for _ in range(rows)]
        costs = [cols*[float("inf")] for _ in range(rows)]
        costs[0][0] = 1
        q = []
        pq = heapq.heappush(q, (1, 0, 0))        
        while q:
            cost, r, c = heapq.heappop(q)            
            if (r, c) == (rows-1, cols-1):
                return cost
            if costs[r][c] < cost:
                continue
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                rr = r + dx
                cc = c + dy
                if rr < 0 or cc < 0 or rr >= rows or cc >= cols or grid[rr][cc]!=0 or visited[rr][cc]:
                    continue
                visited[rr][cc] = 1
                heapq.heappush(q, (cost+1, rr, cc))
                costs[rr][cc] = min(cost+1, costs[rr][cc])
        return -1

# # Simple BFS
# #Time Complexity: O(N^2) (N = rows*cols)
# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0]) if rows else 0
#         if grid[0][0] == 1:
#             return -1
#         visited = [cols*[0] for _ in range(rows)]
#         q = deque([(1, 0, 0)])                
#         while q:
#             cost, r, c = q.popleft()
#             if (r, c) == (rows-1, cols-1):
#                 return cost            
#             for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
#                 rr = r + dx
#                 cc = c + dy
#                 if rr < 0 or cc < 0 or rr >= rows or cc >= cols or grid[rr][cc]!=0 or visited[rr][cc]:
#                     continue
#                 visited[rr][cc] = 1
#                 q.append((cost+1, rr, cc))                
#         return -1
```
