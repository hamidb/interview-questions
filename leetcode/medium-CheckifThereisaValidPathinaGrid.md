Check if There is a Valid Path in a Grid (Leetcode #1391)
===============================
### Medium

Given a `m x n` grid. Each cell of the grid represents a street. The street of `grid[i][j]` can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


You will initially start at the street of the upper-left cell `(0,0)`. A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

![1](https://assets.leetcode.com/uploads/2020/03/05/main.png)

### Example 1:
```
Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid
to reach (m - 1, n - 1).
```
![1](https://assets.leetcode.com/uploads/2020/03/05/e1.png)

### Example 2:
![2](https://assets.leetcode.com/uploads/2020/03/05/e2.png)
```
Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of
any other cell and you will get stuck at cell (0, 0)
```

###Example 3:
```
Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
```

### Example 4:
```
Input: grid = [[1,1,1,1,1,1,3]]
Output: true
```

### Example 5:
```
Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true
```

### Constraints:
```
m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
```

Solution
========

```python
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # code-> 'L R U D'
        lut = {1:[1, 1, 0, 0],
               2:[0, 0, 1, 1],
               3:[1, 0, 0, 1],
               4:[0, 1, 0, 1],
               5:[1, 0, 1, 0],
               6:[0, 1, 1, 0]}
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        if cols == 0 or rows  == 0:
            return False
        visited = [cols*[0] for _ in range(rows)]
        return self.dfs(grid, 0, 0, -1, visited, lut)
    
    def dfs(self, grid, i, j, entry, visited, lut):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if visited[i][j]:
            return False
        if entry != -1 and lut[grid[i][j]][entry] == 0:
            return False
        if i == len(grid)-1 and j == len(grid[0])-1:
            return True
        visited[i][j] = 1
        directions = lut[grid[i][j]]
        if directions[0]: # go left
            if self.dfs(grid, i, j-1, 1, visited, lut): return True
        if directions[1]: # go right
            if self.dfs(grid, i, j+1, 0, visited, lut): return True
        if directions[2]: # go up
            if self.dfs(grid, i-1, j, 3, visited, lut): return True
        if directions[3]: # go down
            if self.dfs(grid, i+1, j, 2, visited, lut): return True
        return False
```

```python
# simple BFS
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        q = deque([[0, 0]])
        while q:
            r, c = q.popleft()
            if r == m-1 and c == n-1:
                return True
            if grid[r][c] in [1, 3, 5] and c > 0 and grid[r][c-1] in [1, 4, 6]:
                q.append([r, c-1])
            if grid[r][c] in [1, 4, 6] and c < n-1 and grid[r][c+1] in [1, 3, 5]:
                q.append([r, c+1])
            if grid[r][c] in [2, 5, 6] and r > 0 and grid[r-1][c] in [2, 3, 4]:
                q.append([r-1, c])
            if grid[r][c] in [2, 3, 4] and r < m-1 and grid[r+1][c] in [2, 5, 6]:
                q.append([r+1, c])
            grid[r][c] = 0  # visited
        return False
```

### **C++**
```c++
class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        std::deque<std::vector<int>> q;
        q.push_back({0, 0});
        while (!q.empty()) {
            const auto elem = q.front(); q.pop_front();
            int r = elem[0], c = elem[1];
            if (r == m-1 && c == n-1)
                return true;
            if (isIn(grid[r][c], {1, 3, 5}) && c > 0 && isIn(grid[r][c-1], {1, 4, 6}))
                q.push_back({r, c-1});
            if (isIn(grid[r][c], {1, 4, 6}) && c < n-1 && isIn(grid[r][c+1], {1, 3, 5}))
                q.push_back({r, c+1});
            if (isIn(grid[r][c], {2, 5, 6}) && r > 0 && isIn(grid[r-1][c], {2, 3, 4}))
                q.push_back({r-1, c});
            if (isIn(grid[r][c], {2, 3, 4}) && r < m-1 && isIn(grid[r+1][c], {2, 5, 6}))
                q.push_back({r+1, c});
            grid[r][c] = 0;
        }
        return false;
    }
    
    bool isIn(int value, const vector<int>& target) {
        for (const auto& v : target) {
            if (value == v)
                return true;
        }
        return false;
    }
};

```
