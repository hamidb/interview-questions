Partition Equal Subset Sum (Leetcode #416)
===============================
### Medium
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

### Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

### Example 1:

```
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

### Example 2:

```
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

Solution
========

```python
class Solution:
    # special case of #698 where k=2
#     def canPartition(self, nums: List[int]) -> bool:
#         d, rem = divmod(sum(nums), 2)
#         if rem: return False
#         buckets = 2 * [0]
#         return self.search(buckets, nums, d)
    
#     def search(self, buckets, nums, cap):
#         if len(nums) == 0: return True
#         v = nums.pop()
#         for i, b in enumerate(buckets):
#             if b + v <= cap:
#                 buckets[i] += v
#                 if self.search(buckets, nums, cap): return True
#                 buckets[i] -= v
#             if b == 0: break
#         nums.append(v)
#         return False
    
    # recursive + memo (top down)
    def canPartition(self, nums: List[int]) -> bool:
        d, rem = divmod(sum(nums), 2)
        if rem: return False
        return self.search(tuple(nums), 0, d)
    
    @lru_cache(maxsize=None)
    def search(self, nums, i, d):
        if d == 0:
            return True
        if i == len(nums) or d < 0:
            return False
        result = self.search(nums, i+1, d-nums[i]) or self.search(nums, i+1, d) 
        return result
        
    # Dynamic programming since nums are non-negative.
    def canPartition(self, nums: List[int]) -> bool:
        d, rem = divmod(sum(nums), 2)
        if rem: return False
        
        # 1D DP
        # target:       0, 1, 2, . . . d
        # can add up?   T, F, F, . . . F
        dp = (d+1)*[False]
        dp[0] = True
        for n in nums:
            i = d
            while i >= n:
                dp[i] = dp[i] or dp[i-n]
                if dp[d]: return True
                i -= 1
        return dp[d]
        
#         # 2D DP -> Knapsack 0/1 (Pick num[i-1] or not Pick it)
#         N = len(nums)
#         dp = [(d+1)*[False] for _ in range(N+1)]
#         for i in range(N+1):
#             dp[i][0] = True
#         for i in range(1, N+1):
#             for j in range(1, d+1):
#                 if nums[i-1] > j:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
#         return dp[N][d]        
        

```
