Magic Squares In Grid (Leetcode #840)
===============================
### Medium

A `3 x 3` magic square is a `3 x 3` grid filled with distinct numbers from `1` to `9` such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many `3 x 3` "magic square" subgrids are there?  (Each subgrid is contiguous).

 

### Example 1:
![example1](https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg)

```
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
```
![example1.1](https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg)
```
while this one is not:
```
![example1.2](https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg)
```
In total, there is only one magic square inside the given grid.
```

### Example 2:

```
Input: grid = [[8]]
Output: 0
```

### Example 3:
```
Input: grid = [[4,4],[3,3]]
Output: 0
```

### Example 4:
```
Input: grid = [[4,7,8],[9,5,1],[2,3,6]]
Output: 0
 ```
 
### Constraints:
```
row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
```

Solution
========

```python
class Solution:
    def __init__(self):
        # All possible cases
        self.pre =  [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]], 
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        ]
        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        if rows < 3 or cols < 3:
            return 0
        black_list = set()
        ans = 0
        for r in range(rows-2):
            for c in range(cols-2):
                if (r, c) in black_list:
                    continue
                if self.isMagic(grid, r, c):
                    ans += 1
                    black_list.add((r+1, c))
                    black_list.add((r, c+1))
                    black_list.add((r+1, c+1))
        return ans
    
    def isMagic(self, grid, r, c):
        if grid[r+1][c+1] != 5:
            return False
        sub_grid = [[grid[y][x] for x in range(c,c+3)] for y in range(r, r+3)]
        if sub_grid in self.pre:
            return True
        return False
   
```
