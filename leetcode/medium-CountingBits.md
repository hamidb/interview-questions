Counting Bits (Leetcode #338)
===============================
### Medium
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

### Example 1:
```
Input: 2
Output: [0,1,1]
```
### Example 2:
```
Input: 5
Output: [0,1,1,2,1,2]
```
### Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?

Space complexity should be O(n).

Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

Solution
========

```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        for i in range(1, num+1):
            if i & 1:  # if odd number -> increment last result
                result.append(result[-1]+1)
            else:  # shift to right and we have already computed
                result.append(result[i>>1])
        return result
    
#     def countBits(self, num: int) -> List[int]:
#         result = [0]
#         for i in range(1, num+1):
#             if i & 1:  # if odd number -> increment last result
#                 result.append(result[-1]+1)
#             else: 
#                 result.append(result[-1] + 1 - self.findFirstZero(result[-1]))
#         return result
    
#     def findFirstZero(self, n):              #       100111
#         a = ~n                               #       011000    
#         a_twos =  ~a + 1                     #       101000
#         return int(math.log2(a & a_twos))    # log_2(001000) = 3
```
