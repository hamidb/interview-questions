Combination Sum II (Leetcode #40)
===============================
### Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

### Example 1:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

### Example 2:
```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 ```

### Constraints:
```
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
```

Solution
========

```python
# # T: O(2^N)  backtracking
# # S: O(N)
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         ans = []
#         N = len(candidates)
#         candidates.sort()
#         seen = set()
#         def recurse(nums, target, result, ans):
#             if tuple(result) in seen:  # optimization
#                 return
#             if target == 0:
#                 ans.append(result.copy())
#                 return
#             for i in range(len(nums)):
#                 curr = nums[i]
#                 if target < curr:
#                     break
#                 result.append(curr)
#                 recurse(nums[i+1:], target-curr, result, ans)
#                 seen.add(tuple(result))
#                 result.pop()
#         recurse(candidates, target, [], ans)
#         return ans

# T: O(2^N)  backtracking
# S: O(N)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        N = len(candidates)
        candidates.sort()
        def recurse(target, idx, result, ans):
            if target == 0:
                ans.append(result.copy())
                return
            for i in range(idx, N):
                curr = candidates[i]
                if i > idx and curr == candidates[i-1]:  # we have seen it already
                    continue
                if target < curr:
                    break
                result.append(curr)
                recurse(target-curr, i+1, result, ans)
                result.pop()
        recurse(target, 0, [], ans)
        return ans
```
