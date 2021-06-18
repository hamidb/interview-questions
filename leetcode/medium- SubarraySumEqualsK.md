Subarray Sum Equals K (Leetcode #560)
===============================
### Medium

Given an array of integers nums and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

### Example 1:
```
Input: nums = [1,1,1], k = 2
Output: 2
```

### Example 2:
```
Input: nums = [1,2,3], k = 3
Output: 2
```

### Constraints:
```
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
```

Solution
========

```python
# # T: O(N^2)
# # S: O(1)
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         L = len(nums)
#         i = 0
#         cnt = 0
#         while i < L:
#             j = i + 1
#             total = nums[i]
#             while j < L:
#                 total += nums[j]
#                 if total == k:
#                     cnt += 1
#                 j += 1
#             i += 1
#         return i
```

We start from 0 to Length and compute current accumulative sum.

We store accumulative sum in a **`hash map: acc_sum -> freq`** so that we know how many times we have seen the current `acc_sum`.

Let assume `k = 3` and say we are currently at position `j` with `acc_sum = 7`.

If we have seen `4=7-3` in accumulative sums before (at position `i`), `sum(j-i) = k`

```python
# T: O(N)
# S: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        curr_acc_sum = 0
        m = defaultdict(int)
        for n in nums:
            curr_acc_sum += n
            if curr_acc_sum == k:
                cnt += 1
            cnt += m[curr_acc_sum - k]
            m[curr_acc_sum] += 1
        return cnt
```
