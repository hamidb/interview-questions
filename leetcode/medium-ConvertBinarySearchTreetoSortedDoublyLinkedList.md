Convert Binary Search Tree to Sorted Doubly Linked List (Leetcode #426)
===============================
### Medium

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list.
For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor,
and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

 

### Example 1:
![Example](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)

```
Input: root = [4,2,5,1,3]
```
![Example](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png)
```
Output: [1,2,3,4,5]
```
```
Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
```

### Example 2:
```
Input: root = [2,1,3]
Output: [1,2,3]
```

### Example 3:
```
Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.
```

### Example 4:
```
Input: root = [1]
Output: [1]
```

### Constraints:
```
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
All the values of the tree are unique.
```

Solution
========

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# T: O(N)
# S: O(N) -> recursion depth is O(N) in worst case and O(log n) in best case

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        def inOrderDfs(node, first, last):
            if node is None:
                return first, last
            
            # left
            first, last = inOrderDfs(node.left, first, last)
            
            # link curr and last
            if last:
                node.left = last
                last.right = node
            else:
                first = node
                
            # root
            last = node

            # right
            first, last = inOrderDfs(node.right, first, last)
            return first, last
        
        if root is None:
            return None

        first, last = inOrderDfs(root, None, None)
        
        # close circle
        first.left = last
        last.right = first
        
        return first
```
