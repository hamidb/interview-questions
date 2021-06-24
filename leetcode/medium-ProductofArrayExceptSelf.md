Product of Array Except Self (Leetcode #238)
===============================
### Medium

Given an integer array nums, return an array answer such that `answer[i]` is equal to the product of all the elements of nums except `nums[i]`.

The product of any prefix or suffix of nums is guaranteed to fit in a `32-bit` integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

 

### Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

### Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 ```

### Constraints:
```
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 ```

Follow up: Can you solve the problem in `O(1)` extra space complexity? (The output array does not count as extra space for space complexity analysis.)



Solution
========

```python
# T: O(N)
# S: O(1) meaning use output array
# compute product of right subarray and put it in output array.
# compute prod of left subarray in O(1) using curr = prev * nums[i] 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        res = L*[1]
        prod = 1
        for i in range(L-1, -1, -1):
            res[i] = prod
            prod *= nums[i]
        tmp = 1
        for i in range(L):
            prod = tmp * res[i]
            res[i] = prod
            tmp *= nums[i]
        return res
        
# # T: O(N)
# # S: O(N)
# # compute product of left sub array and right subarray first.
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         L = len(nums)
#         left, right = L*[1], L*[1]
#         prod = 1
#         for i in range(L):
#             left[i] = prod
#             prod *= nums[i]
#         prod = 1
#         for i in range(L-1, -1, -1):
#             right[i] = prod
#             prod *= nums[i]
#         res = L* [1]
#         for i in range(L):
#             res[i] = left[i] * right[i]
#         return res
```
