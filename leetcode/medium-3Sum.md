3Sum (Leetcode #15)
===============================
### Medium

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

 

### Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

### Example 2:
```
Input: nums = []
Output: []
```

### Example 3:
```
Input: nums = [0]
Output: []
 ```

### Constraints:
```
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
```

Solution
========

```python

# T: O(NlogN + N^2)
# S: O(N) or O(NlogN) based on sort()

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, ans)
        return ans
    
    # T: O(N)
    # S: O(1)
    def twoSum(self, nums, i, ans):
        lo, hi = i+1, len(nums)-1
        n = nums[i]
        while lo < hi:
            total = nums[lo] + nums[hi] + n
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            else:
                ans.append([nums[lo], nums[hi], n])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:  # skip duplicates
                    lo += 1
                    
    # def twoSum(self, nums, i, res):
    #     seen = set()
    #     j = i + 1
    #     while j < len(nums):
    #         complement = -nums[i] - nums[j]
    #         if complement in seen:
    #             res.append([nums[i], nums[j], complement])
    #             while j + 1 < len(nums) and nums[j] == nums[j + 1]:
    #                 j += 1
    #         seen.add(nums[j])
    #         j += 1
```
