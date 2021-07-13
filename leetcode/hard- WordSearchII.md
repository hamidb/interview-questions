 Word Search II (Leetcode #212)
===============================
### Hard

Given an `m x n` board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

 

### Example 1
![ex1](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)
```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

### Example 2:
![ex2](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)
```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
``` 

### Constraints:
```
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
```

Solution
========

```python
# T: O(Mx4x3^L), where M is the number of cells in the board and L is the maximum length of words.
# 3^L because in worst case we should visit 3 neigbors (excluding where we came from)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dir_r = [0, 0, 1, -1]
        dir_c = [1, -1, 0, 0]
        rows, cols = len(board), len(board[0])
        ans = []

        def backtrack(r, c, prefix, root):
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] == '#':
                return
            curr = board[r][c]
            if curr not in root:
                return
            prefix += curr
            node = root[curr]
            if '$' in node:  # if end of word
                ans.append(prefix)
                del node['$']  # delete from words
     
            letter = board[r][c]
            board[r][c] = '#'  # visit
            for i in range(4):
                # rr, cc = r + dir_r[i], c + dir_c[i]
                backtrack(r + dir_r[i], c + dir_c[i], prefix, node)
            board[r][c] = letter  # unvisit
            
            # optimization. Gradually remove unused nodes.
            if not node:
                root.pop(curr)
                
            
        # create trie
        trie = {}
        for word in words:
            p = trie
            for c in word:
                p = p.setdefault(c, {})
            p['$'] = 1
            
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, '', trie)
        return ans
```
