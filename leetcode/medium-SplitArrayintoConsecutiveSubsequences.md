Split Array into Consecutive Subsequences (Leetcode #659)
===============================
### Medium

Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

### Example 1:
```
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
```

### Example 2:
```
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
```

### Example 3:
```
Input: [1,2,3,4,4,5]
Output: False
 ```

### Constraints:
```
1 <= nums.length <= 10000
```

Solution
========
[![Explanation](https://img.youtube.com/vi/uJ8BAQ8lASE/0.jpg)](https://www.youtube.com/watch?v=uJ8BAQ8lASE)
```python
# O(N)
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = {}
        hypo = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for i in range(len(nums)):
            n = nums[i]
            # 1. Already added to chain.
            if freq.get(n, 0) <= 0: 
                continue
            # 2. There's a chain waiting for it.
            elif hypo.get(n, 0) > 0:
                freq[n] -= 1
                hypo[n] -= 1
                hypo[n+1] = hypo.get(n+1, 0) + 1
            # 3. Should create a new chain if can find two more cards.
            elif freq.get(n+1, 0) and freq.get(n+2, 0):
                freq[n] -= 1
                freq[n+1] -= 1
                freq[n+2] -= 1
                hypo[n+3] = hypo.get(n+3, 0) + 1
            else: 
                return False
        return True
```
