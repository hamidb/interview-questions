Escape a Large Maze (Leetcode #1036)
===============================
### Hard

There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are (x, y).

We start at the source = [sx, sy] square and want to reach the target = [tx, ty] square. There is also an array of blocked squares, where each blocked[i] = [xi, yi] represents a blocked square with coordinates (xi, yi).

Each move, we can walk one square north, east, south, or west if the square is not in the array of blocked squares. We are also not allowed to walk outside of the grid.

Return true if and only if it is possible to reach the target square from the source square through a sequence of valid moves.

 

### Example 1:
```
Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: The target square is inaccessible starting from the source square because we cannot move.
We cannot move north or east because those squares are blocked.
We cannot move south or west because we cannot go outside of the grid.
```

### Example 2:
```
Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: Because there are no blocked cells, it is possible to reach the target square.
```

### Constraints:
```
0 <= blocked.length <= 200
blocked[i].length == 2
0 <= xi, yi < 106
source.length == target.length == 2
0 <= sx, sy, tx, ty < 106
source != target
It is guaranteed that source and target are not blocked.
```

Solution
========

```python
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        blocked = set([(b[0], b[1]) for b in blocked])
        # do 2 bfs path:
        # one from source to target and one from target to source
        # at each level in bfs if manhatan dist is over > 200 (len of blocks), we can scape around
        def dfs(source, target):  
            visited = {tuple(source)}
            q = [tuple(source)]            
            while q:
                r, c = q.pop()
                if abs(source[0] - r) + abs(source[1] - c) > 200 or (r, c) == target: # manhatan dist
                    return True                
                for rr, cc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:                    
                    if rr < 0 or cc < 0 or rr >= 1e6 or cc >= 1e6 or (rr, cc) in visited or (rr, cc) in blocked:
                        continue
                    q.append((rr, cc))
                    visited.add((rr, cc))
            return False

        return dfs(source, target) and dfs(target, source)
```
                



    
