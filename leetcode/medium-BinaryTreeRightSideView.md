Binary Tree Right Side View (Leetcode #199)
===============================
### Medium

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

### Example 1:
![ex1](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

### Example 2:
```
Input: root = [1,null,3]
Output: [1,3]
```

### Example 3:
```
Input: root = []
Output: []
 ```

### Constraints:
```
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
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

# Do bfs by adding left first and then right.
# At each level add the curr (holds rightmost element) to ans.
# T: O(N)
# S: O(N)
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        ans = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(curr.val)
        return ans
```
