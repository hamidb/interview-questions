Delete Nodes And Return Forest (Leetcode #1110)
===============================
### Medium
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

### Example 1:

![example1](https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png)
```
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
```

### Constraints:
```
The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
```

Solution
========
```python
# O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None or len(to_delete) == 0: return root
        forest = []
        deletes = set(to_delete)
        root = self.dfs_post_order(root, deletes, forest)
        if root: forest.append(root)
        return forest
    
    def dfs_post_order(self, root, deletes, forest):
        if root is None:
            return None
        
        root.left = self.dfs_post_order(root.left, deletes, forest)
        root.right = self.dfs_post_order(root.right, deletes, forest)
        
        if root.val in deletes:
            if root.left:
                forest.append(root.left)
            if root.right:
                forest.append(root.right)
            return None  # deleted
        return root
```
tags: DFS, Post Order Traversal, Binary Tree, Disjoint set, Union
