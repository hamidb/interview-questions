The kth Factor of n (Leetcode #1492)
===============================
### Medium

Given two positive integers `n` and `k`.

A factor of an integer `n` is defined as an integer `i` where `n % i == 0`.

Consider a list of all factors of `n` sorted in ascending order, return the `kth` factor in this list or return `-1` if `n` has less than `k` factors.

### Example 1:
```
Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
```

### Example 2:
```
Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
```

### Example 3:
```
Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
```

### Example 4:
```
Input: n = 1, k = 1
Output: 1
Explanation: Factors list is [1], the 1st factor is 1.
```

### Example 5:
```
Input: n = 1000, k = 3
Output: 4
Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].
 ```

### Constraints:
```
1 <= k <= n <= 1000
```

Solution
========

```python
# # T: O(N)
# # S: O(1)
# class Solution:
#     def kthFactor(self, n: int, k: int) -> int:
#         cnt = 0
#         for i in range(1, (n // 2) + 1):
#             if n % i == 0:
#                 cnt += 1
#             if k == cnt:
#                 return i
            
#         if k - 1 == cnt:
#             return n
#         else:
#             return -1

# T: O(sqrt(N) * log k)
# S: O(k) using max heap of size k
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        def push(heap, item, k):
            heapq.heappush(heap, item)
            if len(heap) > k:
                heapq.heappop(heap)
    
        h = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                push(h, -i, k)
                if i != n//i:
                    push(h, -(n//i), k)
        if len(h) == k:
            return -h[0]
        else:
            return -1
        
# T: O(sqrt(N))
# S: O( min(k, sqrt(N)) )

# Iterate by i from 1 to \sqrt{N} 
# If i is a divisor of N, decrease k by one. Return i if k == 0.
# We're out of the loop if the kth divisor is not yet found. divisors already contains all "independent" divisors. All other divisors are "paired" ones,
# i.e, the kth divisor could be computed as N / divisors[len(divisors) - k].
# But before that, we need a small correction for the case when N is a perfect square. In that case, the divisor list contains a duplicate.

# class Solution:
#     def kthFactor(self, n: int, k: int) -> int:
#         divisors = []
#         sqr = int(n**0.5)
#         for i in range(1, sqr + 1):
#             if n % i == 0:
#                 divisors.append(i)
#                 k -= 1
#             if k == 0:
#                 return i
            
#         # if perfect square, there's a duplicate to be removed.
#         if n == sqr * sqr:
#             k += 1
            
#         if k <= len(divisors):
#             return n // divisors[-k]
#         else:
#             return -1
        
    
```
