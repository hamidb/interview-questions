Minimum Moves to Move a Box to Their Target Location (Leetcode #1263)
===============================
### Hard

Storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by a grid of size `m x n`, where each element is a wall, floor, or a box.

Your task is move the box `'B'` to the target position `'T'` under the following rules:

* Player is represented by character `'S'` and can move up, down, left, right in the grid if it is a floor (empy cell).
* Floor is represented by character `'.'` that means free cell to walk.
* Wall is represented by character `'#'` that means obstacle  (impossible to walk there). 
* There is only one box `'B'` and one target cell `'T'` in the grid.
* The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
* The player cannot walk through the box.

Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return `-1`.

 

### Example 1:
![ex1](https://assets.leetcode.com/uploads/2019/11/06/sample_1_1620.png)

```
Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.
```

### Example 2:
```
Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1
```

### Example 3:
```
Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation:  push the box down, left, left, up and up.
```

### Example 4:
```
Input: grid = [["#","#","#","#","#","#","#"],
               ["#","S","#",".","B","T","#"],
               ["#","#","#","#","#","#","#"]]
Output: -1
 ```

### Constraints:
```
m == grid.length
n == grid[i].length
1 <= m <= 20
1 <= n <= 20
grid contains only characters '.', '#',  'S' , 'T', or 'B'.
There is only one character 'S', 'B' and 'T' in the grid.
```

Solution
========
```python

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        S, B, T = self.find(grid)
        q = deque([(B, S, 0)])  # state: box, player, curr_moves
        visited = set()  # we mark visited only if the cell was visited from "the same entry".
        while q:
            B, S, moves = q.popleft()
            if B == T:
                return moves
            for rr, cc in self.neighbors(B[0], B[1], rows, cols):
                push_cell = 2*B[0] - rr, 2*B[1] - cc
                if (rr, cc, push_cell) in visited or grid[rr][cc] == '#':
                    continue
                if not self.canReach(grid, S , push_cell, B):
                    continue
                visited.add((rr, cc, push_cell))  # we mark visited only if the cell was visited from "the same entry".
                q.append([(rr, cc), B, moves+1])
        return -1
                
    def canReach(self, grid, start, end, box):
        q = deque([start])
        visited = [len(grid[0])*[0] for _ in grid] 
        visited[start[0]][start[1]] = 1
        visited[box[0]][box[1]] = 1
        while q:
            r, c = q.popleft()
            if (r, c) == end:
                return True
            for rr, cc in self.neighbors(r, c, len(grid), len(grid[0])):
                if visited[rr][cc] or grid[rr][cc] == '#':
                    continue
                visited[rr][cc] = 1
                q.append([rr, cc])
        return False
        
                
    def neighbors(self, r, c, rows, cols):
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0 <= rr < rows and 0 <= cc < cols:
                yield rr, cc
                
    def find(self, grid):
        S, B, T = None, None, None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'S':
                    S = (r, c)
                elif grid[r][c] == 'B':
                    B = (r, c)
                elif grid[r][c] == 'T':
                    T = (r, c)
                if None not in [S, B, T]:
                    return S, B, T
        return S, B, T
```
