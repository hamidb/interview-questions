Dot Product of Two Sparse Vectors (Leetcode #1570)
===============================
### Medium

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

`SparseVector(nums)` Initializes the object with the vector nums
`dotProduct(vec)` Compute the dot product between the instance of `SparseVector` and `vec`
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two `SparseVector`.

Follow up: What if only one of the vectors is sparse?

### Example 1:
```
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
```

### Example 2:
```
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
```

### Example 3:
```
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
 ```

### Constraints:
```
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100
```

Solution
========

```python
# T: O(N)
# S: O(N)

# class SparseVector:
#     def __init__(self, nums: List[int]):
#         self.m = defaultdict(int)
#         for i in range(len(nums)):
#             n = nums[i]
#             if n == 0: continue
#             self.m[i] = n
        

#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec: 'SparseVector') -> int:
#         result = 0
#         for k, v in self.m.items():
#             result += v * vec.m[k]
#         return result

# T: O(N)
# S: O(N)
# class SparseVector:
#     def __init__(self, nums: List[int]):
#         self.m = []
#         for i in range(len(nums)):
#             n = nums[i]
#             if n == 0: continue
#             self.m.append([i, n])
        

#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec: 'SparseVector') -> int:
#         result = 0
#         i = j = 0
#         while i < len(self.m) and j < len(vec.m):
#             if self.m[i][0] == vec.m[j][0]:
#                 result += self.m[i][1] * vec.m[j][1]
#                 i += 1
#                 j += 1
#             elif self.m[i][0] < vec.m[j][0]:
#                 i+=1
#             else:
#                 j+=1
#         return result

# T: O(N)
# S: O(N)
# Same with binary search
class SparseVector:
    def __init__(self, nums: List[int]):
        self.id, self.val = [], []
        for i in range(len(nums)):
            n = nums[i]
            if n == 0: continue
            self.id.append(i)
            self.val.append(n)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        i = j = 0
        l1, l2 = len(self.id), len(vec.id)
        while i < l1 and j < l2:
            if self.id[i] == vec.id[j]:
                result += self.val[i] * vec.val[j]
                i += 1
                j += 1
            elif self.id[i] < vec.id[j]:
                i = bisect.bisect_left(self.id, vec.id[j], i+1)
            else:
                j = bisect.bisect_left(vec.id, self.id[i], j+1)
        return result
```
