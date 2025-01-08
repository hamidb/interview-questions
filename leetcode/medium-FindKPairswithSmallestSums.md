Find K Pairs with Smallest Sums (Leetcode #373)
===============================
### Medium

You are given two integer arrays `nums1` and `nums2` sorted in non-decreasing order and an integer `k`.

Define a pair `(u, v)` which consists of one element from the first array and one element from the second array.

Return the `k` pairs `(u1, v1), (u2, v2), ..., (uk, vk)` with the smallest sums.

 

### Example 1:
```
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

### Example 2:
```
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```

### Constraints:
```
1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length
```


Solution
========

```python
# Time limit Exceed
# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         n1 = len(nums1)
#         n2 = len(nums2)

#         q = []
#         for i in range(min(n1, k)):
#             a = nums1[i]
#             for j in range(min(n2, k)):
#                 b = nums2[j]
#                 heapq.heappush(q, (-a-b, (a, b)))
#                 if len(q) > k:                             
#                     heapq.heappop(q)
#         print(q)
#         return [elem[1] for elem in q]

# T: O(K*logK)
# We know two arrays are sorted, i.e, the smallest sum would be nums1[0] + nums2[0]
# the next smallest is either nums1[1], nums2[0] or nums1[0], nums2[1]
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        n1, n2 = len(nums1), len(nums2)
        visited = set()
        q = [(nums1[0]+nums2[0], (0,0))]        
        visited.add((0,0))  # To avoid adding a pair twice        
        while k and q:
            val, (i,j) = heapq.heappop(q)
            ans.append([nums1[i], nums2[j]])

            if i+1 < n1 and (i+1, j) not in visited:
                heapq.heappush(q, (nums1[i+1] + nums2[j], (i+1, j)))
                visited.add((i + 1, j))

            if j+1 < n2 and (i, j+1) not in visited:
                heapq.heappush(q, (nums1[i] + nums2[j+1], (i, j+1)))
                visited.add((i, j+1))

            k -= 1

        return ans

```
