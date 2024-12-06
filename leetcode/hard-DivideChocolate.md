Divide Chocolate (Leetcode #1231)
===============================
### Hard

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your `K` friends so you start cutting the chocolate bar into `K+1` pieces using `K` cuts,
each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

### Example 1:
```
Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
```

### Example 2:
```
Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
```

### Example 3:
```
Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
``` 

### Constraints:
```
0 <= K < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5
```

Solution
========

```python

# Brute force (TLE)
# T: O(N*K)
# class Solution:
#     def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
#         if K == 0:
#             return sum(sweetness)
#         max_sweetness = 0
#         i, j = 0, 0  # start and end chunk for myself
#         while i < len(sweetness):
#             for j in range(i, len(sweetness)): 
#                 curr_sweetness = sum(sweetness[i:j+1])
#                 if curr_sweetness <= max_sweetness:
#                     continue
#                 k_left = k_right = -1
#                 if len(sweetness[:i]) > 0:
#                     k_left = self.maxChunkGreaterThanLimit(sweetness[:i], curr_sweetness)
#                 if len(sweetness[j+1:]) > 0:
#                     k_right = self.maxChunkGreaterThanLimit(sweetness[j+1:], curr_sweetness)
                
#                 if k_left != -1 and k_left == 0:
#                     break
#                 if k_right != -1 and k_right == 0:
#                     break
#                 if max(k_left, 0) + max(k_right, 0) < K:
#                     break
#                 max_sweetness = max(max_sweetness, curr_sweetness)
#             i += 1
#         return max_sweetness
        
#     def maxChunkGreaterThanLimit(self, sweetness, limit):
#         if len(sweetness) < 1:
#             return 0
#         for j in range(len(sweetness)):
#             if sum(sweetness[:j+1]) < limit:
#                 continue
#             return 1 + self.maxChunkGreaterThanLimit(sweetness[j+1:], limit)
#         return 0

    
# Binary Search
# T: O(NlogN)
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        lo, hi = min(sweetness), sum(sweetness) // (K+1) 
        # search in [lo-hi] to find the minimum total sweetness per chunk.
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if self.canDivide(sweetness, mid) < K+1:  # can divide into k+1 chunks with min sweatness = mid
                hi = mid-1
            else:
                lo = mid+1
        return lo
            
    def canDivide(self, sweetness, val):
        div = 0
        curr_sum = 0
        for swt in sweetness:
            curr_sum += swt
            if curr_sum > val:
                div += 1
                curr_sum = 0
        return div
```
