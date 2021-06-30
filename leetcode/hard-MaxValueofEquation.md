Max Value of Equation (Leetcode #1499)
===============================
### Hard

You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where `points[i] = [xi, yi]` such that `xi < xj` for all 
`1 <= i < j <= points.length`. You are also given an integer `k`.

Return the maximum value of the equation `yi + yj + |xi - xj|` where `|xi - xj| <= k` and `1 <= i < j <= points.length`.

It is guaranteed that there exists at least one pair of points that satisfy the constraint `|xi - xj| <= k`.

 

### Example 1:
```
Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
```

### Example 2:
```
Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
 ```

### Constraints:
```
2 <= points.length <= 105
points[i].length == 2
-108 <= xi, yi <= 108
0 <= k <= 2 * 108
xi < xj for all 1 <= i < j <= points.length
xi form a strictly increasing sequence.
```

Solution
========

```python
# Monotonic Priority Queue
# T: O(N log K)
# S: O(K)
# Value = yi + yj + |xi - xj|
# Value = yj - xj + yi + xi  because xi < xj
# max Value = max(yj-xj) + yi+xi for each i
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # store (-diff_xy, x) in min heap
        pq = []
        heapq.heappush(pq, ((-points[0][1] + points[0][0]), points[0][0]))
        ans = float('-inf')
        for xi, yi in points[1:]:
            while pq and xi - pq[0][1] > k:
                heapq.heappop(pq)
            if pq:
                ans = max(ans, -pq[0][0] + xi + yi)
            heapq.heappush(pq, ((-yi+xi), xi))
            
        return ans
    
# # Hash
# # T: O(NxK)
# # S: O(N)
# class Solution:
#     def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
#         mp = defaultdict(list)
#         for x, y in points:
#             mp[x].append([x, y])
        
#         def value(x1, x2, y1, y2):
#             return y1+y2 + abs(x1-x2)
        
#         ans = float('-inf')
#         for x1, y1 in points:
#             for x2, y2 in mp[x1][1:]:
#                 ans = max(ans, value(x1, x2, y1, y2))
            
#             for d in range(1, k+1):
#                 for x2, y2 in mp[x1+d]:
#                     ans = max(ans, value(x1, x2, y1, y2))
#         return ans

```
