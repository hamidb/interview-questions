Binary Tree Maximum Path Sum (Leetcode #124)
===============================
### Hard

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

 

### Example 1:
![ex1](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)
```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

### Example 2:
![ex2](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)
```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 ```

### Constraints:
```
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
```

Solution
========

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# T: O(N)
# S: O(H) recursion depth is equal to height of tree
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        def max_gain(root):
            if root is None:
                return 0
            nonlocal ans
            left_gain = max(0, max_gain(root.left))  # negative gain is not desired.
            right_gain = max(0, max_gain(root.right))
            
            # case 0: where root the connecting node of two subtrees
            # if root is not part of the path while the subtrees are, ans already contains answer.
            ans = max(ans, root.val + left_gain + right_gain)
            
            # case 1: where root and 0 or 1 subtree is part of the path.
            return root.val + max(left_gain, right_gain)
        
        max_gain(root)
        return ans
```
