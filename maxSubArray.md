Maximum Subarray (Leetcode #53)
===============================
### Easy
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

### Example:
Input: `[-2,1,-3,4,-1,2,1,-5,4]`,

Output: `6`

Explanation: `[4,-1,2,1]` has the largest `sum = 6`.

### Follow up:
If you have figured out the `O(n)` solution, try coding another solution using
the divide and conquer approach, which is more subtle.


### Solution:

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        curr_max = 0
        global_max = -0x7fffffff
        for i in range(size):
            curr_max = max(nums[i], curr_max+nums[i])
            if global_max < curr_max:
                global_max = curr_max
        return global_max
```

