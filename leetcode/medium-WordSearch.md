Word Search (Leetcode #79)
===============================
### Medium

Given an `m x n` grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

 

### Example 1:
![ex1](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

### Example 2:
![ex2](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

### Example 3:
![ex3](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
``` 

### Constraints:
```
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
``` 

#### Follow up:
Could you use search pruning to make your solution faster with a larger board?

Solution
========

```python
# T: O(Nx3^L)  N number of cells and L length of word
# worst case we have to process all cells. for each cell, we have 3 directions to go (excluding the cell we came from).
# S: O(L) recursion depth
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(r, c, level):
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] == '#':
                return False
            curr = board[r][c]
            if word[level] != curr:
                return False
            if len(word) == level+1:
                return True
            board[r][c] = '#'  # visit the cell
            for rr, cc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if dfs(r+rr, c+cc, level+1):
                    return True
            board[r][c] = curr  # unvisit
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
```
