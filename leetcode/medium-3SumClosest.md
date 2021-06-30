3Sum Closest (Leetcode #16)
===============================
### Medium

Given an array `nums` of `n` integers and an integer `target`, find three integers in nums such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

 

### Example 1:
```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
``` 

### Constraints:
```
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
```

Solution
========

```python
# T: O(N^2)
# S: O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        ans = None
        for i in range(len(nums)-2):
            n = nums[i]
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                total = nums[lo] + nums[hi] + n - target
                if abs(total) < min_diff:
                    min_diff = abs(total)
                    ans = total + target
                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    return target
        return ans
```
