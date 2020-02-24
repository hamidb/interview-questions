Unique Binray Search Tree (Leetcode #96)
===============================
### Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

### Example:

```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```
Solution
========
Refer to [leetcode 95](./medium-UniqueBinraySearchTreeII.md).
Solution is based on Memoization.

```python
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [1]  # value for  i=0
        for i in range(1, n+1):
            nums.append(self._numTrees(i, nums))
        return nums[n]

    def _numTrees(self, n, nums):
        if n == 1:
            return 1
        size = 0
        for i in range(1, n+1):
            # leftLength = i-1
            # rightLength = n-i
            size += nums[n-i]*nums[i-1]
        return size
```
