Interval List Intersections (Leetcode #986)
===============================
### Medium

You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [starti, endi]` and `secondList[j] = [startj, endj]`.
Each list of intervals is pairwise **disjoint** and in **sorted** order.

Return the intersection of these two interval lists.

A closed interval `[a, b] (with a < b)` denotes the set of real numbers `x` with `a <= x <= b`.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of `[1, 3]`
and `[2, 4]` is `[2, 3]`.

 

### Example 1:
![ex1](https://assets.leetcode.com/uploads/2019/01/30/interval1.png)

```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

### Example 2:
```
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
```

### Example 3:
```
Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []
```

### Example 4:
```
Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]
``` 

### Constraints:
```
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109
endj < startj+1
```

Solution
========

```python
# more optimized
# T: O(min(M, N))
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:   
        # interval intersect
        def intersect(x1, y1, x2, y2):
            start = max(x1, x2)
            end = min(y1, y2)
            return [start, end]
            
        L1, L2 = len(firstList), len(secondList)
        if L1 == 0 or L2 == 0:
            return []
        
        ans = []
        p1, p2 = 0, 0
        while p2 < L2 and p1 < L1:
            A = firstList[p1]
            B = secondList[p2]

            if A[1] < B[0]:  # no overlap: if e_a < s_b
                pass
            elif B[1] < A[0]:  # no overlap if e_b < s_a
                pass
            else:
                ans.append(intersect(A[0], A[1], B[0], B[1]))
            
            if A[1] == B[1]:
                p1 += 1
                p2 += 1
            elif A[1] > B[1]:
                p2 += 1
            else:
                p1 += 1
        return ans

# T: O(min(M, N))
# class Solution:
#     def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
#         # interval intersect
#         def intersect(x1, y1, x2, y2):
#             start = max(x1, x2)
#             end = min(y1, y2)
#             if start <= end:
#                 return [start, end]
#             return []
            
#         L1, L2 = len(firstList), len(secondList)
#         if L1 == 0 or L2 == 0:
#             return []
        
#         ans = []
#         p1, p2 = 0, 0
#         while p2 < L2 and p1 < L1:
#             A = firstList[p1]
#             B = secondList[p2]
#             overlap = intersect(A[0], A[1], B[0], B[1])
#             if A[1] == B[1]:
#                 p1 += 1
#                 p2 += 1
#             elif A[1] > B[1]:
#                 p2 += 1
#             else:
#                 p1 += 1
                
#             if overlap != []:
#                 ans.append(overlap)
#         return ans
```
