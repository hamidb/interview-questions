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
### Using binary search
1. Observation:

   * The smallest element in the matrix is at the top-left corner (matrix[0][0]).
   * The largest element in the matrix is at the bottom-right corner (matrix[n-1][n-1]).
   * The kth smallest element lies between these two values.

2. Binary Search on Value Range:

   * Perform binary search on the range [matrix[0][0], matrix[n-1][n-1]].
   * For each midpoint mid, count how many elements in the matrix are less than or equal to mid.
   
3. Counting Elements ≤ mid:

   * Use the sorted property of rows and columns to efficiently count how many elements are less than or equal to mid:
       * Start from the bottom-left corner.
       * Move right if the value is ≤ mid.
       * Move up if the value is > mid.
4. Adjust the Search Range:

    * If the count of elements ≤ mid is less than k, increase mid (search in the right half).
 Otherwise, decrease mid (search in the left half).

```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        def count_less_equal(mid):
            # Counts how many elements are ≤ mid
            count = 0
            row, col = n - 1, 0  # Start from bottom-left corner
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1  # All elements in this row up to `row` are ≤ mid
                    col += 1  # Move to the next column
                else:
                    row -= 1  # Move up to a smaller value
            return count
        
        # Binary search over the value range
        low, high = matrix[0][0], matrix[n-1][n-1]
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1  # Search in the larger half
            else:
                high = mid  # Search in the smaller half
        
        return low
```
#### Time Complexity:

Binary search runs O(log(max-min)) where max-min is the range of values in the matrix.

Counting elements in the matrix takes: O(n) per midpoint.

Total:  O(n⋅log(max-min))

Space Complexity: O(1) since no additional data structures are used.

### Using heap
We use a min-heap to efficiently extract the smallest element at each step. Here's the step-by-step explanation:

1. Start with the smallest element:
 The smallest element in the matrix is at matrix[0][0] (top-left corner).

 Push the first element of each row into the heap (row 0, column 0 through k or n elements, whichever is smaller).
 
3. Extract the smallest element k times:
   
 Use the heap to repeatedly extract the smallest element.

 After popping the smallest element, push the next element from the same row into the heap (if it exists).
 
4. Stop after k pops:

The kth pop from the heap gives the kth smallest element.
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
