K-diff Pairs in an Array (Leetcode #532)
===============================
### Medium

Given an array of integers nums and an integer `k`, return the number of unique `k-diff` pairs in the array.

A `k-diff` pair is an integer pair `(nums[i], nums[j])`, where the following are true:

* `0 <= i < j < nums.length`
* `|nums[i] - nums[j]| == k`
Notice that `|val|` denotes the absolute value of val.

 

### Example 1:
```
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
```

### Example 2:
```
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
```

### Example 3:
```
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
```

### Example 4:
```
Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2
```

### Example 5:
```
Input: nums = [-1,-2,-3], k = 1
Output: 2
 ```

### Constraints:
```
1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107
```

Solution
========

```python
# O(N) -> using counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        count = Counter(nums)
        for n in count:
            if k > 0 and n+k in count:
                cnt += 1
            elif k == 0 and count[n] > 1:
                cnt += 1
        return cnt
        
# T: O(N^2)
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         seen = set()
#         cnt = 0
#         for i in range(len(nums)):
#             j = i + 1
#             while j < len(nums):
#                 if (nums[i], nums[j]) in seen:
#                     j += 1
#                     continue
#                 diff = nums[j] - nums[i]
#                 if diff > k:
#                     break
#                 if diff == k:
#                     seen.add((nums[i], nums[j]))
#                     cnt += 1
#                     break
#                 j += 1
#         return cnt

# # O(N log(N))
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         seen = set()
#         cnt = 0
#         L = len(nums)
#         for i in range(L):
#             ni = nums[i]
#             j = bisect.bisect_left(nums, ni+k, i+1)
#             if j == L:
#                 continue
#             nj = nums[j]
#             if (ni, nj) in seen:
#                 continue
#             if nj == ni + k:
#                 cnt += 1
#                 seen.add((ni, nj))
#         return cnt

# O(N log(N)) -> two pointer
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         L = len(nums)
#         cnt = 0
#         left, right = 0, 1
        
#         while left < L and right < L:
#             if nums[right] - nums[left] < k or left == right:
#                 right += 1
#             elif nums[right] - nums[left] > k:
#                 left += 1
#             else:
#                 left += 1
#                 while left < L and nums[left] == nums[left-1]:
#                     left += 1
#                 cnt += 1
#         return cnt
                
```
