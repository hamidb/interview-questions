Validate Binary Search Tree (Leetcode #98)
===============================
### Medium

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.
 

### Example 1:
```
    2
   / \
  1   3

Input: [2,1,3]
Output: true
```

### Example 2:
```
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
```
Explanation: The root node's value is 5 but its right child's value is 4.

Solution
========
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True   
        left = root.left
        right = root.right
        if left == None and right == None:
            return True
        if left and left.val >= root.val:
            return False
        if right and right.val <= root.val:
            return False
        pred = self.inOrderPredecessor(root)
        if pred and pred.val >= root.val:
            return False
        succ = self.inOrderSuccessor(root)
        if succ and succ.val <= root.val:
            return False
        return self.isValidBST(left) and self.isValidBST(right)
    
    def inOrderPredecessor(self, root):
        if root == None or root.left == None:
            return None
        node = root.left
        while node.right:
            node = node.right
        return node
    
    def inOrderSuccessor(self, root):
        if root == None or root.right == None:
            return None
        node = root.right
        while node.left:
            node = node.left
        return node        
```
