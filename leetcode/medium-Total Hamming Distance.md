Total Hamming Distance (Leetcode #477)
===============================
### Medium

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums. 

### Example 1:
```
Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
```

### Example 2:
```
Input: nums = [4,14,4]
Output: 4
``` 

### Constraints:
```
1 <= nums.length <= 104
0 <= nums[i] <= 109
The answer for the given input will fit in a 32-bit integer.
```

Solution
========

```python
# T: O(N)
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # for each bit count number of zeros and number of ones
        # answer is sum(ones*zeros)
        ans = 0
        for i in range(32):
            ones = 0        
            for n in nums:
                ones += (n >> i) & 1                                
            ans += ones*(len(nums)-ones)  # number of ones x number of zeros

        return ans
```

