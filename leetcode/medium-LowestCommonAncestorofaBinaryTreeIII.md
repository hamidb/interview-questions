Lowest Common Ancestor of a Binary Tree III (Leetcode #1650)
===============================
### Medium

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

```
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
```
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes `p` and `q` in a tree `T` is the lowest node that has both `p` and `q`
as descendants (where we allow a node to be a descendant of itself)."

### Example 1:
![ex1](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

### Example 2:
![ex2](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
```

### Example 3:
```
Input: root = [1,2], p = 1, q = 2
Output: 1
``` 

### Constraints:
```
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.
```

Solution
========

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# T: O(H) -> H is height of tree
# S: O(1)
class Solution(object):
    def lowestCommonAncestor(self, p, q):
        def findDepth(node):
            depth = 0
            while node:
                depth += 1
                node = node.parent
            return depth
        
        # find depth of p and q
        p_depth, q_depth = findDepth(p), findDepth(q)
        
        # level up depth by visiting their parents
        while p_depth != q_depth:
            if p_depth > q_depth:
                p_depth -= 1
                p = p.parent
            else:
                q_depth -= 1
                q = q.parent
                
        # find where they meet
        while p != q:
            p = p.parent
            q = q.parent
        return p
    
# # T: O(H) -> H is height of tree
# # S: O(N)
# class Solution(object):
#     def lowestCommonAncestor(self, p, q):
#         """
#         :type node: Node
#         :rtype: Node
#         """
#         p_anc = set()
        
#         while p:
#             p_anc.add(p)
#             p = p.parent
        
#         while q:
#             if q in p_anc:
#                 return q
#             q = q.parent
#         return None

```
