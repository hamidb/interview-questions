Sliding Window Maximum (Leetcode #239)
===============================
### Hard

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right.
You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

### Example 1:
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

### Example 2:
```
Input: nums = [1], k = 1
Output: [1]
```

### Example 3:
```
Input: nums = [1,-1], k = 1
Output: [1,-1]
```

### Example 4:
```
Input: nums = [9,11], k = 2
Output: [11]
```

### Example 5:
```
Input: nums = [4,-2], k = 2
Output: [4]
 ```

### Constraints:
```
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
```

Solution
========

```python
# # T: O(NlogK)
# # S: O(K)
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         pq = []
#         for i in range(k):
#             heapq.heappush(pq, (-nums[i], i))
#         ans = [-pq[0][0]]
#         for i in range(0, n-k):
#             heapq.heappush(pq, (-nums[i+k], i+k))
#             # remove all the elments which are not in the current window
#             while pq[0][1] < i+1:
#                 heapq.heappop(pq)
#             ans.append(-pq[0][0])
#         return ans

# T: O(N)
# S: O(K)
# Use a monotonic queue and keep it in a decreasing order.
# Store index of elements
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque([])
        ans = []
        for i in range(0, n):
            # pop from left until only elements in the current subwindow exist.
            # subwindow [i-k+1 i]
            while q and q[0] < i-k+1:
                q.popleft()

            # pop from right until the elements are smaller than nums[i].
            # to keep in decreasing order. So q[0] always is the max element.
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            if i >= k-1:
                ans.append(nums[q[0]])
        return ans
```
