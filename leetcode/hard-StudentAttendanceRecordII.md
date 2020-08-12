Student Attendance Record II (Leetcode #552)
===============================
### Hard

Given a positive integer `n`, return the number of all possible attendance records with length `n`, which will be regarded as rewardable.
The answer may be very large, return it after `mod 109 + 7`.

A student attendance record is a string that only contains the following three characters:

```
'A' : Absent.
'L' : Late.
'P' : Present.
```
A record is regarded as rewardable if it doesn't contain more than one `A` (absent) or more than two continuous `L` (late).

### Example 1:
```
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
```

### Note: The value of n won't exceed 100,000.

Solution
========
```python
# O(N)
class Solution:
    def checkRecord(self, n: int) -> int:
        m = 1000000007
        # All valid cases if and only if including one of:
        # state[0]: ending with A
        # state[1]: 0A and ending with P
        # state[2]: 1A and ending with P
        # state[3]: 0A and ending with L
        # state[4]: 1A and ending with L
        # state[5]: 0A and ending with LL
        # state[6]: 1A and ending with LL
        
        # i: 1 -> n
        # prev -> state i-1
        prev= [1, 1, 0, 1, 0, 0, 0]
        
        for _ in range(2, n+1):
            curr = [0, 0, 0, 0, 0, 0, 0]
            curr[0] = ((prev[1] + prev[3]) % m + prev[5]) % m
            curr[1] = curr[0]
            curr[2] = (((prev[0] + prev[2]) % m + prev[4]) % m + prev[6]) % m
            curr[3] = prev[1]
            curr[4] = (prev[0] + prev[2]) % m
            curr[5] = prev[3]
            curr[6] = prev[4]
            
            prev = curr
            
        ans = 0
        for value in prev:
            ans = (ans + value) % m
        return ans
```
