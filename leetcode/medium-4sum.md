4Sum (Leetcode #18)
===============================
### Medium

Given an array nums of n integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

`0 <= a, b, c, d < n`

`a, b, c,` and `d` are distinct.
`nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in any order.

 

### Example 1:
```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

### Example 2:
```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 ```

### Constraints:
```
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

```


### Solution
```python
# T: O(NlogN + N^3)
# S: O(N) or O(NlogN) based on sort()
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        # i -> first of 4
        for i in range(len(nums)-3):
            # some optimization knowing nums is sorted.
            if target < nums[i]*4 or nums[-1]*4 < target:
                break

            if i==0 or (nums[i]!=nums[i-1]):  # skip duplicate
                self.threeSum(i, nums, ans, target, p)
        return ans

    # T: O(N^2)
    def threeSum(self, i, nums, ans, target, p):
        # j -> second of 4
        for j in range(i+1, len(nums)-2):            
            # some optimization knowing nums is sorted.
            if target < nums[i]+nums[j]*3 or nums[i]+nums[-1]*3 < target:
                break

            if j==i+1 or nums[j] != nums[j-1]:  # skip duplicate
                self.twoSum(i, j, nums, ans, target)

    # T: O(N)
    def twoSum(self, i, j, nums, ans, target):        
        n4, n3 = nums[i], nums[j]
        lo, hi = j+1, len(nums)-1
        while lo < hi:
            total = n4 + n3 + nums[lo] + nums[hi] 
            if total > target:
                hi -= 1
            elif total < target:
                lo += 1
            else:
                ans.append([n4, n3, nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:  # skip duplicate
                    lo += 1
```
