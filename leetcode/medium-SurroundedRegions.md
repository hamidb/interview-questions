Surrounded Regions Leetcode #130)
===============================
### Medium
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

### Example:
```
X X X X
X O O X
X X O X
X O X X
```
After running your function, the board should be:
```
X X X X
X X X X
X X X X
X O X X
```
Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Solution
========
```python
class Solution:
# Approach 1
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         rows = len(board)
#         cols = len(board[0]) if rows > 0 else 0
#         if rows <= 2 or cols <= 2:
#             return board
#         for i in range(1, cols-1):
#             for j in range(1, rows-1):
#                 visited = set()
#                 if board[j][i] == 'O' and self.canCapture(i, j, visited, board, rows, cols):
#                     for r, c in visited:  # to save time
#                         board[r][c] = 'X'
        
#     def canCapture(self, i, j, visited, board, rows, cols):
#         if i == 0 or j == 0 or i == cols-1 or j == rows-1:
#             return False
#         visited.add((j, i))
#         if (j-1, i) not in visited and board[j-1][i] == 'O':
#             if not self.canCapture(i, j-1, visited, board, rows, cols):
#                 return False
#         if (j, i-1) not in visited and board[j][i-1] == 'O':
#             if not self.canCapture(i-1, j, visited, board, rows, cols):              
#                 return False
#         if (j, i+1) not in visited and board[j][i+1] == 'O':
#             if not self.canCapture(i+1, j, visited, board, rows, cols):              
#                 return False
#         if (j+1, i) not in visited and board[j+1][i] == 'O':
#             if not self.canCapture(i, j+1, visited, board, rows, cols):              
#                 return False
#         return True
            
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        if rows <= 2 or cols <= 2:
            return board
        
        # add to visited all 'O's connected to an 'O' on boundaries.
        visited = [[False for i in range(cols)] for j in range(rows)]
        
        for j in range(0, cols):
            if board[0][j] == 'O':
                self.dfs(0, j, board, visited, False)
            if board[rows-1][j] == 'O':
                self.dfs(rows-1, j, board, visited, False)   

        for i in range(0, rows):
            if board[i][0] == 'O':
                self.dfs(i, 0, board, visited, False)
            if board[i][cols-1] == 'O':
                self.dfs(i, cols-1, board, visited, False)

        # Now, flip all unvisited 'O's
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if board[i][j] == 'O' and not visited[i][j]:
                    self.dfs(i, j, board, visited, True)
                    
    def dfs(self, i, j, board, visited, flip):
        if i < 0 or j < 0 or j > len(board[0])-1 or i > len(board)-1:
            return
        if visited[i][j]: return
        if board[i][j] == 'X': return
        if flip:
            board[i][j] = 'X'
        visited[i][j] = True
        self.dfs(i+1, j, board, visited, flip)
        self.dfs(i-1, j, board, visited, flip)
        self.dfs(i, j+1, board, visited, flip)
        self.dfs(i, j-1, board, visited, flip)
        
```
