Maximum Length of Repeated Subarray (Leetcode #718)
===============================
### Medium

Given two integer arrays `nums1` and `nums2`, return the maximum length of a subarray that appears in both arrays.

 

### Example 1:
```
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
```

### Example 2:
```
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
 ```

### Constraints:
```
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
Given an array of integers nums and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.
```


Solution
========

```python
# Rabin-Karl: Binary Search + Rolling Hashi
# We binary search for the length 
# T: O((M+N)xlog(min(M, N)))
# S: O(M)
# Implementation not provided


# Dynamic Programming (Bottom up)
# T: O(MxN)
# S: O(MxN)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        L1 = len(nums1)
        L2 = len(nums2)
        dp = [(L2+1)*[0] for _ in range(L1+1)]
        ans = 0
        for j in range(1, L2+1):
            for i in range(1, L1+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans, dp[i][j])
        return ans

# Binary Search + naive check
# We binary search for the length 
# T: O((M+N)x(min(M,N))xlog(min(M, N)))
# S: O(M^2)
# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
#         # O(length*(M+N))
#         def check(length, nums1, nums2):
#             seen = set()
#             for i in range(0, len(nums1)-length+1):
#                 seen.add(tuple(nums1[i:i+length]))
#             for i in range(0, len(nums2)-length+1):
#                 if tuple(nums2[i:i+length]) in seen:
#                     return True
#             return False
        
#         L1 = len(nums1)
#         L2 = len(nums2)
#         lo = 0
#         hi = min(L1, L2) + 1  # check(min(L1, L2) + 1) is False.
        
#         while lo < hi:
#             mid = (lo + hi) // 2
#             if check(mid, nums1, nums2):
#                 lo = mid+1
#             else:
#                 hi = mid
                
#         return lo-1
```
