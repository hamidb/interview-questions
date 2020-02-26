Number of Islands (Leetcode #200)
===============================
### Medium
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Example 1:
```
Input:
11110
11010
11000
00000

Output: 1
```
### Example 2:
```
Input:
11000
11000
00100
00011

Output: 3
```

Solution
========

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols == 0:
            return 0
        mat = [[x for x in y] for y in grid]
        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != '0':
                    num_islands += 1
                    self.zeroOutAdjacents(r, c, mat)
        return num_islands

    def zeroOutAdjacents(self, r, c, mat):
        mat[r][c] = '0'
        if r+1 < len(mat) and mat[r+1][c] != '0':
            self.zeroOutAdjacents(r+1, c, mat)
        if c+1 < len(mat[0]) and mat[r][c+1] != '0':
            self.zeroOutAdjacents(r, c+1, mat)
        if c > 0 and mat[r][c-1] != '0':
            self.zeroOutAdjacents(r, c-1, mat)
        if r > 0 and mat[r-1][c] != '0':
            self.zeroOutAdjacents(r-1, c, mat)


``
