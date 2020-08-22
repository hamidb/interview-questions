Shortest Path in a Grid with Obstacles Elimination (Leetcode #1293)
===============================
### Hard

Given a `m * n` grid, where each cell is either `0` (empty) or `1` (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner `(0, 0)` to the lower right corner `(m-1, n-1)` given that you can eliminate at most `k`
obstacles. If it is not possible to find such walk return `-1`.

 

### Example 1:
```
Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
``` 

### Example 2:
```
Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 ```

### Constraints:
```
grid.length == m
grid[0].length == n
1 <= m, n <= 40`
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
```

Solution
========

```python
# O(M*N)
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        if k >= rows + cols - 3:
            return rows + cols - 2

        steps = 0
        visited = [[-1] * cols for _ in range(rows)]
        visited[0][0] = k
        q = deque([(0, 0, k)])
        while q:
            steps += 1
            for _ in range(len(q)):
                r, c, p = q.popleft()
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    x, y = c + dx, r + dy
                    if x < 0 or x >= cols or y < 0 or y >= rows:
                        continue
                    kk = p-grid[y][x]
                    if kk <= visited[y][x]: # have visited here on a better path.
                        continue
                    # early stop if there's shortcut (-1 because goal cell != 1)
                    # But only applies when, it's unvisited.
                    to_target = rows - y + cols - x - 2  # rows-r-1 + cols-c-1
                    if kk >= to_target-1 and visited[y][x] == -1:
                        return steps + to_target
                    q.append((y, x, kk))
                    visited[y][x] = kk
        return -1
```  
