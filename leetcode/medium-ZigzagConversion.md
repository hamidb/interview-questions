Zigzag Conversion (Leetcode #6)
===============================
### Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

`string convert(string s, int numRows);`
 

### Example 1:
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

### Example 2:
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
```

### Explanation:
```
P     I    N
A   L S  I G
Y A   H R
P     I

```

### Example 3:
```
Input: s = "A", numRows = 1
Output: "A"
``` 

### Constraints:
```
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
```

### Solution
```python

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s        
        rows = numRows*[""]

        zig = False  # going down
        r = 0
        for ch in s:
            rows[r] += ch
            if r == 0 or r == numRows - 1:
                zig = not zig
            r = r + 1 if zig else r - 1            
        return "".join(rows)

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         L = len(s)
#         board = [L*[""] for _ in range(numRows)]
#         if numRows == 1:
#             return s
#         zig = True  # going down
#         r, c = 0, 0
#         for ch in s:
#             board[r][c] = ch
#             if zig:
#                 r += 1
#             if r >= numRows:
#                 r -= 1
#                 zig = False
#             if not zig:
#                 r -= 1
#                 c += 1
#             if r < 0:
#                 r += 2
#                 c -= 1
#                 zig = True

#         ans = ""
#         for r in board:
#             ans += "".join(r)
#         return ans

```
