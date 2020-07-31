Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (Leetcode #1438)
===============================
### Medium
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between
any two elements of this subarray is less than or equal to limit.

### Example 1:
```
Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
```

### Example 2:
```
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
```

### Example 3:
```
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
```

### Constraints:
```
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
```
Solution
========
[![Explanation](https://img.youtube.com/vi/h5cz7rA77ik/0.jpg)](https://youtu.be/h5cz7rA77ik)

```python
# O(n) solution
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ, maxQ = deque(), deque()
        ans = 0
        left = 0
        for right in range(len(nums)):
            while minQ and minQ[-1] > nums[right]:
                minQ.pop()
            minQ.append(nums[right])
            while maxQ and maxQ[-1] < nums[right]:
                maxQ.pop()
            maxQ.append(nums[right])
            if maxQ[0] - minQ[0] <= limit:
                ans = max(ans, right-left+1)
            else:
                if maxQ[0] == nums[left]:  # if max was the left
                    maxQ.popleft()
                if minQ[0] == nums[left]:  # if min was the left
                    minQ.popleft()
                left += 1  # shrink window
        return ans
```
