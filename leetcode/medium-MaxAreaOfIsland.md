Max Area of Island (Leetcode #695)
===============================
### Medium
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

### Example 1:
```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
```
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

### Example 2:
`[[0,0,0,0,0,0,0,0]]`
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

Solution
========

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols == 0:
            return 0

        mat = [[x for x in y] for y in grid]
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != 0:
                    area = self.computeArea(r, c, mat)
                    if area > max_area:
                        max_area = area
        return max_area

    def computeArea(self, row, col, mat):
        area = 1
        mat[row][col] = 0
        if row+1 < len(mat) and mat[row+1][col] != 0:
            area += self.computeArea(row+1, col, mat)
        if row-1 >=0 and mat[row-1][col] != 0:
            area += self.computeArea(row-1, col, mat)
        if col+1 < len(mat[0]) and mat[row][col+1] != 0:
            area += self.computeArea(row, col+1, mat)
        if col-1 >= 0 and mat[row][col-1] != 0:
            area += self.computeArea(row, col-1, mat)

        return area
```
### **C++**
```c++
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size();
        if (rows == 0) return 0;
        int cols = grid[0].size();
        if (cols == 0) return 0;
        int max_area = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                max_area = std::max(max_area, dfsArea(grid, r, c));
            }
        }
        return max_area;
    }
    
    int dfsArea(vector<vector<int>>& grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] == 0)
            return 0;
        grid[r][c] = 0;
        int area = 1 + dfsArea(grid, r+1, c);
        area += dfsArea(grid, r-1, c);
        area += dfsArea(grid, r, c+1);
        area += dfsArea(grid, r, c-1);
        return area;
    }
};
```
