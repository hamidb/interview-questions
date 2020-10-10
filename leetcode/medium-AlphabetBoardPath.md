Alphabet Board Path (Leetcode #1138)
===============================
### Medium

On an alphabet board, we start at position `(0, 0)`, corresponding to character `board[0][0]`.

Here, `board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]`, as shown in the diagram below.

![example](https://assets.leetcode.com/uploads/2019/07/28/azboard.png)

We may make the following moves:
```
'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
```
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

 

### Example 1:
```
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
```

### Example 2:
```
Input: target = "code"
Output: "RR!DDRR!UUL!R!"
``` 

### Constraints:
```
1 <= target.length <= 100
target consists only of English lowercase letters.
```

Solution
========

```python

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ans = ''
        a = ord('a')
        r, c = 0, 0
        for t in target:
            rt, ct = divmod(ord(t)-a, 5)
            if c > ct:
                ans += (c-ct) * 'L'
            if rt > r:
                ans += (rt-r) * 'D'
            if r > rt:
                ans += (r-rt) * 'U'
            if ct > c:
                ans += (ct-c) * 'R'
            ans += '!'
            r, c = rt, ct
        return ans
```
