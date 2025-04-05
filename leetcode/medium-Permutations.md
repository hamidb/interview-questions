Permutations (Leetcode #46)
===============================
### Medium
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

### Example 1:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2:
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Example 3:
```
Input: nums = [1]
Output: [[1]]
``` 

### Constraints:
```
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
```

Solution
========

```python
# T: O(n^2 x n!)
# n! is number of permutations
# n for recursion tree
# n for slicing
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)

        def recurse(nums, result, results):
            if len(result) == L:
                results.append(result[:])
            
            for i in range(len(nums)):
                n = nums[i]
                result.append(n)
                recurse(nums[:i]+nums[i+1:], result, results)
                result.pop(-1)
        results = []
        recurse(nums, [], results)
        return results
```
