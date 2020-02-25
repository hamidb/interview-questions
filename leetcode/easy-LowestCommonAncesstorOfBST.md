Lowest Common Ancesstor of Binray Search Tree (Leetcode #235)
===============================
### Easy
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

### Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

### Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


### Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

Solution
========
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == root.val or q.val == root.val:
            # if one of them is equal to root -> root is LCA
            return root
        if p.val > root.val:
            if q.val < root.val:
                # if q on the left and p on the right subtree -> root is LCA
                return root
            # otherwise, LCA is somewhere in the right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        if q.val > root.val:
            # if q on the right and p on the left subtree -> root is LCA
            return root
        # otherwise, LCA is somewhere in the left subtree
        return self.lowestCommonAncestor(root.left, p, q)



```
