Maximal Rectangle (Leetcode #85)
===============================
### Hard
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

### Example:
```
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

Solution
========
### Approach 2: Dynamic Programming - Better Brute Force on Histograms
#### Algorithm
We can compute the maximum width of a rectangle that ends at a given coordinate in constant time. We do this by keeping track of the number of consecutive ones each
square in each row. As we iterate over each row we update the maximum possible width at that point. This is done using `row[i] = row[i - 1] + 1 if row[i] == '1'`.

Once we know the maximum widths for each point above a given point, we can compute the maximum rectangle with the lower right corner at that point in linear time.
As we iterate up the column, we know that the maximal width of a rectangle spanning from the original point to the current point is the running minimum of each maximal
width we have encountered.

We define:
```
maxWidth = min(maxWidth, widthHere)

curArea = maxWidth * (currentRow - originalRow + 1)

maxArea = max(maxArea, curArea)
```
The following animation makes this more clear. Given the maximal width of all points above it, let's calculate the maximum area of any rectangle at the bottom yellow 
square:
Repeating this process for every point in our input gives us the global maximum.
Note that our method of precomputing our maximum width essentially breaks down our input into a set of histograms,
with each column being a new histogram. We are computing the maximal area for each histogram.

As a result, the above approach is essentially a repeated use of the better brute force approach detailed in 84 - Largest Rectangle in Histogram.

### Approach 3: Using Histograms - Stack
#### Algorithm

In the previous approach we discussed breaking the input into a set of histograms - one histogram representing the substructure at each column. 
To compute the maximum area in our rectangle, we merely have to compute the maximum area of each histogram and find the global maximum
(note that the below approach builds a histogram for each row instead of each column, but the idea is still the same).

Since Largest Rectangle in Histogram is already a problem on leetcode, we can just borrow the fastest stack-based solution here and apply it onto each histogram
we generate. For an in-depth explanation on how the Largest Rectangle in Histogram algorithm works, please use the links above.

```python
# O(N x M): N:rows, M: cols
class Solution:
    def largestRectangleArea(self, heights):
        length = len(heights)
        max_area = 0
        stack = [-1]
        for i in range(length):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()]*(length-stack[-1]-1))
        return max_area            
        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [0] * len(matrix[0])  # stores height histogram for each row.
        max_area = 0
        for j in range(len(matrix)):
            for i in range(len(matrix[0])):
                dp[i] = dp[i] + 1 if matrix[j][i] == '1' else 0
            max_area = max(max_area, self.largestRectangleArea(dp))
        return max_area

# # O(N^2 x M): N:rows, M: cols
# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         rows = len(matrix)
#         cols = len(matrix[0]) if rows else 0
#         dp = [[0]*(cols+1) for _ in range(rows)]
#         max_area = 0
#         for j in range(rows):
#             for i in range(cols):
#                 if matrix[j][i] == '0':
#                     continue
#                 width = dp[j][i] = dp[j][i-1] + 1
#                 for k in range(j, -1, -1):
#                     height = j-k+1
#                     width = min(width, dp[k][i])
#                     max_area = max(max_area, width*height)
#         return max_area
```
