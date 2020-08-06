Flip Equivalent Binary Trees (Leetcode #951)
===============================
### Medium

For a binary tree `T`, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree `X` is flip equivalent to a binary tree `Y` if and only if we can make `X` equal to `Y` after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes `root1` and `root2`.

 

### Example 1:

![Flipped Trees Diagram](https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png)
```
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
```
 

### Note:
```
Each tree will have at most 100 nodes.
Each value in each tree will be a unique integer in the range [0, 99].
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
# class Solution:
#     def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
#         # one None the other not None -> False
#         if (not root1 and root2) or (not root2 and root1):
#             return False
#         # both are None -> True
#         if root1 is None and root2 is None:
#             return True
#         if root1.val != root2.val:
#             return False
            
#         if self.equalChildren(root1.left, root2.left, root1.right, root2.right):
#             res = self.flipEquiv(root1.left, root2.left)
#             return res and self.flipEquiv(root1.right, root2.right)
#         elif self.equalChildren(root1.left, root2.right, root1.right, root2.left):
#             res = self.flipEquiv(root1.left, root2.right)
#             return res and self.flipEquiv(root1.right, root2.left)
#         else:
#             return False
    
#     def equalChildren(self, l1, l2, r1, r2):
#         if l1:
#             if l2 is None or l1.val != l2.val:
#                 return False
#         else:
#             if l2 is not None:
#                 return False
#         if r1:
#             if r2 is None or r1.val != r2.val:
#                 return False
#         else:
#             if r2 is not None:
#                 return False
#         return True
            
class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))
            
```
