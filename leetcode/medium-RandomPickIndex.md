Random Pick Index (Leetcode #398)
===============================
### Medium

Given an integer array `nums` with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist
in the array.

### Implement the Solution class:

* `Solution(int[] nums)` Initializes the object with the array nums.
* `int pick(int target)` Picks a random index `i` from nums where `nums[i] == target`. If there are multiple valid `i`'s,
then each index should have an equal probability of returning.
 

### Example 1:
```
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
 ```

### Constraints:
```
1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
target is an integer from nums.
At most 104 calls will be made to pick.
```

Solution
========
```python
# # T: O(N) for creation
# # T: O(1) for pick
# # S: O(N)
# class Solution:

#     def __init__(self, nums: List[int]):
#         self.m = defaultdict(list)
#         for i in range(len(nums)):
#             self.m[nums[i]].append(i)
        

#     def pick(self, target: int) -> int:
#         l = self.m[target]
#         return l[random.randint(0, len(l)-1)]

# T: O(N) for creation
# T: O(N) for pick
# S: O(1)
# Reservoir sempling -> p(each id) = 1/cnt
class Solution:

    def __init__(self, nums: List[int]):
        self.m = nums
        
    def pick(self, target: int) -> int:
        cnt = 0
        ans = 0
        for i in range(len(self.m)):
            if self.m[i] == target:
                cnt += 1
                if random.randint(1, cnt) == cnt:  # p(i) = 1/cnt
                    ans = i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```
