Tiling a Rectangle with the Fewest Squares (Leetcode #1240)
===============================
### Hard

Given a rectangle of size `n x m`, find the minimum number of integer-sided squares that tile the rectangle.

### Example 1:
![example1](https://assets.leetcode.com/uploads/2019/10/17/sample_11_1592.png)

```
Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
```

### Example 2:
![example2](https://assets.leetcode.com/uploads/2019/10/17/sample_22_1592.png)

```
Input: n = 5, m = 8
Output: 5
```

### Example 3:
![example3](https://assets.leetcode.com/uploads/2019/10/17/sample_33_1592.png)
```
Input: n = 11, m = 13
Output: 6
```

### Constraints:
```
1 <= n <= 13
1 <= m <= 13
```

Solution
========

credit: @MarcoChang from Leetcode

This task is insteresting,
and the given examples are already the hints we can use.

I'd like to share the best solution(best runtime without shortcut) credited to thoithoi98,
and give more explanation in simple words and improved code as below.

We can divide the original rectangle into

**base case**: use complete `height` (`height < width`, like official given example 1 and 2)

**adapted case**: decrease height of base case, and keep 2 squares and 3 rectangles (like given example 3).

The figures of these two cases are like figure1 and figure2 provided by thoithoi98.

I made the figure of adapted case more explicit as below.
![image](https://assets.leetcode.com/users/images/31038997-8ef0-41be-ad69-61e1a116738a_1604390938.0187716.png)

This version is like a combination of greedy, dp, backtracking,
I think it is more straightforward and more efficient than naive dp, backtracking even in larger num than `13`
because we can use symmetry of square1 and square2 to decrease search space a bit.

### Complexity
#### T: O(m x n^2) where n < m

Consider the complext case in which the width or height of the center square (`rect3`) can vary from `0` to `H`.
it means there are `H` possibilities and for each possibility, the bottom-left corner of that square can be anywhere in range of `(0,0)` to `(H, W)` 

```python
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        
        @lru_cache(None)
        def dfs(h, w):
            if h == 0 or w == 0:
                return 0
            if h == w:
                return 1
            if h > w:
                h, w = w, h  # swap
            
            # base case
            cnt = 1 + dfs(w-h, h)
            
            # complex case
            # square1 is (h-b)x(h-b) where b: 1-> h-1
            # square2 is kxk where k: b -> d
            for b in range(1, h):
                d = w - h + b
                for k in range(b, d+1):
                    if h > k:
                        rect1 = dfs(b, w-k)
                        rect2 = dfs(d, h-k)
                        rect3 = dfs(d-k, k-b)
                        cnt = min(cnt, rect1+rect2+rect3+2)
            return cnt
        return dfs(n, m)
```

