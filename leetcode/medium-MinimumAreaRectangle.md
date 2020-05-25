Minimum Area Rectangle (Leetcode #939)
===============================
### Medium
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

### Example 1:
```
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
```
### example 2:
```
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
```

### Note:
```
1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
```

Solution
========

```python
# T: O(n^2), S: O(n)
import functools

class Solution:
    def comp(self, a, b):
        x1, y1 = a
        x2, y2 = b
        if x1 < x2: return -1
        if x1 == x2: return (y1 > y2) - (y1 < y2)
        return 1
    
    def minAreaRect(self, points: List[List[int]]) -> int:
        # first sort by x then y
        sort = sorted(points, key=functools.cmp_to_key(self.comp))
        # build a dict of x with values equal to list of y's
        columns = collections.defaultdict(list)
        for x, y in sort:
            columns[x].append(y)
        
        minArea = float('inf')
        # for each pair of y1,y2 store their common x
        seen_x = {}
        
        # scan all x in columns
        for x, l in columns.items():
            # for each l in list of values (y) -> build all possible pairs of y 
            for i2, y2 in enumerate(l):
                for i1 in range(i2):
                    y1 = l[i1]
                    # if the pair exists -> compute it's area and update the minimum
                    if (y1, y2) in seen_x:
                        minArea = min(minArea, (x - seen_x[y1, y2])*(y2-y1))
                    seen_x[y1, y2] = x
        return minArea if minArea < float('inf') else 0
```
