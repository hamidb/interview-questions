Permutations II (Leetcode #47)
===============================
### Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


### Example 1:
```
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

### Example 2:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 ```

### Constraints:
```
1 <= nums.length <= 8
-10 <= nums[i] <= 10
```

### Solution
```python
# T: O(N!)
# S: O(N)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def recurse(nums, perm):
            if len(nums) == 0:
                ans.append(perm)
                return
            seen = set()
            for i, n in enumerate(nums):
                if n not in seen:  # do not add if already added
                    seen.add(n)
                    recurse(nums[:i]+nums[i+1:], perm+[n])
        recurse(nums, [])
        return ans

# with sort
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         nums.sort()

#         def recurse(nums, perm):
#             if len(nums) == 0:
#                 ans.append(perm)
#                 return            
#             for i, n in enumerate(nums):
#                 if i == 0 or nums[i] != nums[i-1]: # do not add the same number
#                     recurse(nums[:i]+nums[i+1:], perm+[n])
#         recurse(nums, [])
#         return ans
        
```
