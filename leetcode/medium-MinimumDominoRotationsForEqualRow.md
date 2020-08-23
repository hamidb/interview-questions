Minimum Domino Rotations For Equal Row (Leetcode #1007)
===============================
### Medium


In a row of dominoes, `A[i]` and `B[i]` represent the top and bottom halves of the `i`-th domino.  (A domino is a tile with two numbers from `1 to 6` -
one on each half of the tile.)

We may rotate the i-th domino, so that `A[i]` and `B[i]` swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return `-1`.

![Example1](https://assets.leetcode.com/uploads/2019/03/08/domino.png)

### Example 1:

```

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
```

### Example 2:
```
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 ```

### Note:
```
1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
```

Solution
========
### Approach 1: Greedy.
#### Intuition
Let's pick up an arbitrary `i`-th domino element in the configuration. The element has two sides, `A[i]` is an upper side and `B[i]` is a lower side.
![case0](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/Figures/1007/config.png)
There could be three possible situations here

1. One could make all elements of A row or B row to be the same and equal to A[i] value.
For example, if one picks up the 0th element, it's possible to make all elements of A row to be equal to `2`.
![case1](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/Figures/1007/s1.png)

2. One could make all elements of A row or B row to be the same and equal to B[i] value.
For example, if one picks up the 1th element, it's possible to make all elements of B row to be equal to `2`.
![case2](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/Figures/1007/s2.png)

3. It's impossible to make all elements of A row or B row to have the same A[i] or B[i] value.
![case3](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/Figures/1007/s3.png)

The third situation means that it's impossible to make all elements in A row or B row to be equal.

Yes, the only one domino element was checked here, and still it's enough because the rotation is the only allowed operation here.

#### Algorithm

Pick up the first element. It has two sides: `A[0]` and `B[0]`.

Check if one could make all elements in A row or B row to be equal to `A[0]`. If yes, return the minimum number of rotations needed.

Check if one could make all elements in A row or B row to be equal to `B[0]`. If yes, return the minimum number of rotations needed.

Otherwise return `-1`.

```python
# class Solution:
#     def minDominoRotations(self, A: List[int], B: List[int]) -> int:
#         if len(A) == 1:
#             return 0
        
#         def check(val):
#             rotation_a = 0 # rotations needed to make top row all = val
#             rotation_b = 0 # rotations needed to make bottom row all = val
#             # why making bottom row the same as A[0]?
#             # answer: A : [2,5,5,5,5]
#             #         B : [5,2,2,2,2]
#             # min is when you can make bottom row = A[0] = 2.
#             for i in range(len(A)):
#                 # case 1: Can't make it.
#                 if A[i] != val and B[i] != val:
#                     return -1
#                 # Make top row = A[0]
#                 elif A[i] != val:
#                     rotation_a += 1
#                 # Make bottom row = A[0]
#                 elif B[i] != val:
#                     rotation_b += 1 
#             return min(rotation_a, rotation_b)
                
#         # pick first domino.
#         rotation = check(A[0])
#         if rotation != -1 or A[0] == B[0]:  # if both the same, no need to check B[0]
#             return rotation
#         else:
#             return check(B[0])

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        first = set([A[0],B[0]])       
        for a, b in zip(A[1:],B[1:]):
            first = first.intersection({a,b})
        
        if len(first) == 0:
            return -1
        
        goal = list(first)[0]
        a_count = len([val for val in A if val != goal])
        b_count = len([val for val in B if val != goal])
        return min(a_count, b_count)
```
