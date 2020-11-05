Longest Line of Consecutive One in Matrix (Leetcode #)
===============================
### Medium

Given a `01` matrix `M`, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

### Example:
```
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
```

### Hint: 
The number of elements in the given matrix will not exceed 10,000.

Solution
========

```python

# T: O(mn)
# S: O(mn)
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        rows = len(M)
        cols = len(M[0]) if rows else 0
    
        dp0 = [cols*[0] for _ in range(rows)]  # horizontal
        dp1 = [cols*[0] for _ in range(rows)]  # vertical
        dp2 = [cols*[0] for _ in range(rows)]  # diagonal
        dp3 = [cols*[0] for _ in range(rows)]  # counter diagonal   
        mx = 0
        for y in range(rows):
            for x in range(cols):
                if not M[y][x]:
                    continue
                dp0[y][x] = 1+dp0[y][x-1] if x>0 else 1
                dp1[y][x] = 1+dp1[y-1][x] if y>0 else 1
                dp2[y][x] = 1+dp2[y-1][x-1] if x>0 and y>0 else 1
                dp3[y][x] = 1+dp3[y-1][x+1] if x<cols-1 and y>0 else 1
                mx = max(mx, dp0[y][x], dp1[y][x], dp2[y][x], dp3[y][x])
        return mx
```
