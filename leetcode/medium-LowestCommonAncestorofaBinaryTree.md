Lowest Common Ancestor of a Binary Tree (Leetcode #236)
===============================
### Medium
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  `root = [3,5,1,6,2,0,8,null,null,7,4]`


 

### Example 1:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```
### Example 2:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 ```

### Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

Solution
========
Keep searching until we find both nodes while keeping all searched nodes parent in a dictionary.
Then we can build p's ancestor and search q or q's ancestors in p's ancestor.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(N), Space: O(N)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p is None or q is None:
            return None
        prev = {root: None}
        self.bfs(root, p, q, prev)
        ancestor = set()
        while p:
            ancestor.add(p)
            p = prev[p]
        while q not in ancestor:
            q = prev[q]
        return q
        
    def bfs(self, root, p, q, prev):
        queue = deque()
        queue.append(root)
        found = 0
        while queue and found < 2:
            node = queue.popleft()
            if node.val == p.val:
                found += 1
            if node.val == q.val:
                found += 1
            if node.left:
                queue.append(node.left)
                prev[node.left] = node
            if node.right:
                queue.append(node.right)
                prev[node.right] = node
                
# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#        result = []
#         def recurse(curr):
#             if curr is None: 
#                 return False
#             if curr.val == p.val or curr.val == q.val:
#                 mid = True
#             else:
#                 mid = False
#             left = recurse(curr.left)
#             right = recurse(curr.right)
#             if left+right+mid >= 2:
#                 result.append(curr)
#             return left or right or mid
        
#         recurse(root)
#         return result[-1]

```
