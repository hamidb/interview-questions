Kth Smallest Element in a Sorted Matrix (Leetcode #378)
===============================
### Medium
Given an `n x n` matrix where each of the rows and columns are sorted in ascending order, return the `k`th smallest element in the matrix.

Note that it is the `k`th smallest element in the sorted order, not the `k`th distinct element.

 

### Example 1:
```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
```

### Example 2:
```
Input: matrix = [[-5]], k = 1
Output: -5
 ```

### Constraints:
```
n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
```

Solution
========

```python
# we will take the first element of min(N, K) rows where NN represents the number of rows, and add each of these elements to the heap.
# It's important to know what row and column an element belongs to. Without knowing that, we won't be able to move forward in that
# particular list. So, apart from adding an element to the heap, we also need to add its row and column number.
# Hence, our min-heap will contain a triplet of information (value, row, column).
# The heap will be arranged on the basis of the values and we will use the row and column number to add a replacement for
# the next element in case it gets popped off the heap.
# At this point, our heap contains min(N,K) elements. Now we start a loop that goes until we iterate over K elements.
# At each step, we remove the minimum element from the heap. The element will tell us which row should be further consumed. Using the row and column
# information we will add the next element to the heap. Specifically, if the current minimum element was from row r and had a column position c,
# then the next element to be added to the heap will be (r, c+1).

# T: O(X + Klog(X)) where X is min(K, N)
# S: O(X)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # store cell, r, c in min heap.
        pq = [(matrix[i][0], i, 0) for i in range(min(k, n))]  # first element of each row (up to min(k, n))
        heapq.heapify(pq)
        while pq:
            value, r, c = heapq.heappop(pq)
            if k == 1:
                return value
            if c < n - 1:
                heapq.heappush(pq, (matrix[r][c+1], r, c+1))
            k -= 1
        
```
