Reaching Points (Leetcode #780)
===============================
### Hard

Given four integers `sx, sy, tx,` and `ty`, return `true` if it is possible to convert the point `(sx, sy)` to the point `(tx, ty)` through some operations,
or `false` otherwise.

The allowed operation on some point `(x, y)` is to convert it to either `(x, x + y)` or `(x + y, y)`.

 
### Example 1:
```
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
```

### Example 2:
```
Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: false
```

### Example 3:
```
Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: true
 ```

### Constraints:
```
1 <= sx, sy, tx, ty <= 109
```

Solution
========

### Intuition:

#### Approach #3: Work Backwards (Naive Variant) [Time Limit Exceeded]
Every parent point `(x, y)` has two children, `(x, x+y)` and `(x+y, y)`. However, every point `(x, y)` only has one parent candidate `(x-y, y)` if `x >= y`,
else `(x, y-x)`. This is because we never have points with negative coordinates.

![Diagram of successive parents of the target point](https://leetcode.com/problems/reaching-points/Figures/780/tree.png)

Looking at previous successive parents of the target point, we can find whether the starting point was an ancestor. For example, if the target point is `(19, 12)`,
the successive parents must have been `(7, 12)`, `(7, 5)`, and `(2, 5)`; so `(2, 5)` is a starting point of `(19, 12)`.

Repeatedly subtract the smaller of `{tx, ty}` from the larger of `{tx, ty}`. The answer is `true` if and only if we eventually reach `sx, sy`.


### Modulo

As in Approach #3, we work backwards to find the answer, trying to transform the target point to the starting point via applying the parent operation `(x, y) -> (x-y, y)`
or `(x, y-x)` depending on which one doesn't have negative coordinates.

We can speed up this transformation by bundling together parent operations.

Say `tx > ty`. We know that the next parent operations will be to subtract ty from `tx`, until such time that `tx = tx % ty`. When both `tx > ty` and `ty > sy`, 
we can perform all these parent operations in one step, replacing while `tx > ty: tx -= ty` with `tx %= ty`.

Otherwise, if say `tx > ty` and `ty <= sy`, then we know ty will not be changing (it can only decrease). Thus, only `tx` will change, and it can only change by subtracting
by ty. Hence, `(tx - sx) % ty == 0` is a necessary and sufficient condition for the problem's answer to be True.

The analysis above was for the case `tx > ty`, but the case `ty > tx` is similar. When `tx == ty`, no more moves can be made.

```python
# T: O(log(max(tx,ty)))
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # (2, 3) -> (12, 17+100*12)
        if tx < sx or ty < sy:
            return False
        if tx == sx and ty == sy:
            return True
        if tx == ty:
            return tx == sx and ty == sy
        elif tx < ty:
            if tx > sx:  # (2, 3) -> (12, 17+100*12),
                return self.reachingPoints(sx, sy, tx, ty % tx)  # (2, 3) -> (12, 5)
            else:  # (2, 3) -> (2, 5)
                return (ty-sy) % tx == 0  
        else:
            if ty > sy:  # (2, 3) -> (12, 5)
                return self.reachingPoints(sx, sy, tx % ty, ty)  # (2, 3) -> (2, 5)  
            else:
                return (tx-sx) % ty == 0
```

or

```python
# T: O(log(max(tx,ty)))
# S: O(1)
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy
```
