Unique Paths III (Leetcode #980)
===============================
### Hard

On a 2-dimensional grid, there are 4 types of squares:

* `1` represents the starting square.  There is exactly one starting square.
* `2` represents the ending square.  There is exactly one ending square.
* `0` represents empty squares we can walk over.
* `-1` represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

### Example 1:
```
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
```

### Example 2:
```
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
```

### Example 3:
```
Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
```

### Note:
```
1 <= grid.length * grid[0].length <= 20
```

Solution
========

```python
# T: O(3^N)  3 ways to choose (excluding self)
# S: O(N) depth of recursion
# Backtracking
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        start, end = (0, 0), (0, 0)
        zeros = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 0:
                    zeros += 1
        self.ans = 0
        def recurse(r, c, zeros):
            if grid[r][c] == 2 and zeros == 0:  # Goal
                self.ans += 1
                return
            if zeros == 0 or grid[r][c] == 2:  # Early exit
                return
            grid[r][c] = -1  # mark visited
            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:  # choices
                rr, cc = dr+r, dc+c
                # check constraints
                if rr < 0 or rr >= rows or cc < 0 or cc >= cols or grid[rr][cc] == -1:
                    continue
                recurse(rr, cc, zeros-1)
            grid[r][c] = 0  # unvisit, backtrack
        
        recurse(start[0], start[1], zeros+1)
        return self.ans
```
