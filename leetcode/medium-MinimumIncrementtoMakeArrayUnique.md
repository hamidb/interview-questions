Minimum Increment to Make Array Unique (Leetcode #945)
===============================
### Medium

Given an array of integers `nums`, a move consists of choosing any `nums[i]`, and incrementing it by `1`.

Return the least number of moves to make every value in nums unique.

 

### Example 1:
```
Input: nums = [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
```

### Example 2:
```
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
```


### Note:
```
0 <= nums.length <= 40000
0 <= nums[i] < 40000
```

Solution
========

```python
# T: O(N log N)
# S: O(1) no extra space (use num)
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:  # duplicate or decreasing
                res += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return res

# T: O(N log N)
# S: O(N)
# class Solution:
#     def minIncrementForUnique(self, nums: List[int]) -> int:
#         count = Counter(nums)
#         keys = deque(list(sorted(count.keys())))
#         res = 0
#         while keys:
#             k = keys.popleft()
#             v = count[k]
#             if v > 1:
#                 if count[k+1] == 0:
#                     keys.appendleft(k+1)
#                 count[k+1] += v-1
#                 count[k] = 1
#                 res += v-1
#         return res
                
# T: O(N)
# S: O(N)
# class Solution:
#     def minIncrementForUnique(self, nums: List[int]) -> int:
#         count = Counter(nums)
#         res = 0
#         for k in range(100000):
#             v = count[k]
#             if v > 1:
#                 count[k+1] += v-1
#                 count[k] = 1
#                 res += v-1            
#         return res
```
