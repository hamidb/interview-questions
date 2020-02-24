"""A Binary Tree Node"""

from queue import Queue

class Node:

  # Constructor to create a new node
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BST(object):

  def __init__(self, root=None):
    self._root = root

  def _add(self, node, data):
    if data > node.data:
      if node.right:
        self._add(node.right, data)
      else:
        node.right = Node(data)
    else:
      if node.left:
        self._add(node.left, data)
      else:
        node.left = Node(data)

  @property
  def root(self):
    return self._root

  @root.setter
  def root(self, root):
    self._root = root

  def add(self, data):
    if self.root:
      self._add(self.root, data)
    else:
      self.root = Node(data)

  @staticmethod
  def bft(node, callback):
    if not callback:
      return
    if node:
      queue = Queue()
      queue.put(node)
      while not queue.empty():
        front = queue.get()
        callback(front.data)
        if front.left:
          queue.put(front.left)
        if front.right:
          queue.put(front.right)

  @staticmethod
  def pre_order_traverse(node, callback):
    if not callback:
      return
    if node:
      callback(node.data)
      BST.pre_order_traverse(node.left, callback)
      BST.pre_order_traverse(node.right, callback)

  @staticmethod
  def in_order_traverse(node, callback):
    if not callback:
      return
    if node:
      BST.pre_order_traverse(node.left, callback)
      callback(node.data)
      BST.pre_order_traverse(node.right, callback)

  @staticmethod
  def post_order_traverse(node, callback):
    if not callback:
      return
    if node:
      BST.pre_order_traverse(node.left, callback)
      BST.pre_order_traverse(node.right, callback)
      callback(node.data)

  @staticmethod
  def contains(node, data):
    if node:
      if data == node.data:
        return True
      if data > node.data:
        return BST.contains(node.right, data)
      return BST.contains(node.left, data)
    return False

  @staticmethod
  def find_minimum(node):
    if not node:
      return node
    return BST.find_minimum(node.left)

  @staticmethod
  def get_maximum_depth(node):
    max_depth = 0
    if not node:
      return max_depth
    left_depth = BST.get_maximum_depth(node.left)
    right_depth = BST.get_maximum_depth(node.right)
    return max(left_depth, right_depth) + 1

  @staticmethod
  def get_inorder_successor(node):
    if not node or not node.right:
      return None
    ptr = node.right
    while not ptr.left:
      ptr = ptr.left
    return ptr

  @staticmethod
  def get_inorder_predecessor(node):
    if not node or not node.left:
      return None
    ptr = node.left
    while not ptr.right:
      ptr = ptr.right
    return ptr

  def delete(self, node, data):
    if not node:
      return node
    if node.data > data:
      node.left = self.delete(node.left, data)
    elif node.data < data:
      node.right = self.delete(node.right, data)
    else:
      if node.left is None:
        # has right child only
        tmp = node.right
        node = None
        return tmp
      if node.right is None:
        # has left child only
        tmp = node.left
        node = None
        return tmp
      # has both children. Then replace its content with its in-order
      # successor and delete the successor node.
      succ = BST.get_inorder_successor(node)
      node.data = succ.data
      node.right = self.delete(node, succ.data)
    return node


if __name__ == '__main__':
  print('Binary Search TREE')

  bst_tree = BST()
  bst_tree.add(3)
  bst_tree.add(1)
  bst_tree.add(2)
  bst_tree.add(4)
  bst_tree.add(5)
  print('Pre Order Traversal')
  BST.pre_order_traverse(bst_tree.root, callback=print)
  print('Post Order Traversal')
  BST.post_order_traverse(bst_tree.root, callback=print)
  print('In Order Traversal')
  BST.in_order_traverse(bst_tree.root, callback=print)

  print('Max Depth >> ', BST.get_maximum_depth(bst_tree.root))

  print('Search a node')
  print('11 in tree: ', BST.contains(bst_tree.root, 11))
  print('4 in tree: ', BST.contains(bst_tree.root, 4))

  print('Level Order Traversal')
  BST.bft(bst_tree.root, print)

  bst_tree.delete(bst_tree.root, 2)
  print('2 in tree: ', BST.contains(bst_tree.root, 2))
