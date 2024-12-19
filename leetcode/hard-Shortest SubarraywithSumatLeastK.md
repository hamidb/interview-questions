Shortest Subarray with Sum at Least K (Leetcode #862)
===============================
### Hard

Return the length of the shortest, non-empty, contiguous subarray of nums with sum at least `k`.

If there is no non-empty subarray with sum at least `k`, return `-1`.

 

### Example 1:
```
Input: nums = [1], k = 1
Output: 1
```

### Example 2:
```
Input: nums = [1,2], k = 4
Output: -1
```

### Example 3:
```
Input: nums = [2,-1,2], k = 3
Output: 3
 ```

### Note:
```
1 <= nums.length <= 50000
-105 <= nums[i] <= 105
1 <= k <= 109
```

Solution
========

```python
# Monotonic deque to store indices where the accumulative_sum[i] is increasing.
# So for each i in the deque, if we find j that satisfies the condition, we don't have to
# check other indices smaller than j.
# To creater such monotonic queue, we each element, we should remove from right until the elements
# are bigger than current prefix_sum.
# From the left side, we should remove elements until p[i]-p[elements] >= k.
# T: O(N)
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx_len = n+1
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(num+prefix_sum[-1])
        
        q = deque([]) # keeps index only in monotonically decreasing order
        for i in range(n+1):
            # keep poping until right of q >= current sum
            while q and prefix_sum[q[-1]] >= prefix_sum[i]: 
                q.pop()

            # check from left to find the best index that satisfies the condition
            while q and prefix_sum[i] - prefix_sum[q[0]] >= k:
                mx_len = min(mx_len, i-q.popleft())
            q.append(i)

        return mx_len if mx_len != n+1 else -1
```
