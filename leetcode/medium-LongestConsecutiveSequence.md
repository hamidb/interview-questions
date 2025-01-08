Longest Consecutive Sequence (Leetcode #128)
===============================
### Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

 

### Example 1:
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### Example 2:
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
``` 

### Constraints:
```
0 <= nums.length <= 105
-109 <= nums[i] <= 109
```

Solution
========

```python
# T: O(N)
# for each element see if next and prev is available
# keep checking while removing the elements from the set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        nums = set(nums)
        ans = 0
        while nums:
            low = high = nums.pop()
            while low-1 in nums or high+1 in nums:
                if low-1 in nums:
                    nums.remove(low-1)
                    low -= 1
                if high+1 in nums:
                    nums.remove(high+1)
                    high += 1
            ans = max(ans, high-low+1)
        return ans

# T: O(N)
# Uses a map where keys represents numbers, and values are the length of a consecutive sequence with 
# that number as either the upper or lower bound of the sequence.
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
      
#         nums = set(nums)
#         h = {}
#         ans = 0
#         for n in nums:
#             lo = h.get(n-1, 0)
#             hi = h.get(n+1, 0)
#             length = 1 + hi + lo
#             h[n-lo] = length
#             h[n+hi] = length
#             ans = max(ans, length)
#         return ans

```
