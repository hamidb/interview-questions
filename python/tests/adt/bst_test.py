# Lint as: python3
"""Tests for binary_heap."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt import bst
import unittest

class BSTTest(unittest.TestCase):

  def test_bst_00(self):
    bst_tree = bst.BST()
    bst_tree.add(3)
    bst_tree.add(1)
    bst_tree.add(2)
    bst_tree.add(4)
    bst_tree.add(5)
    output = []
    callback = lambda x: output.append(x)
    bst.BST.pre_order_traverse(bst_tree.root, callback=callback)
    self.assertEqual(output, [3, 1, 2, 4, 5])

  def test_bst_01(self):
    bst_tree = bst.BST()
    bst_tree.add(3)
    bst_tree.add(1)
    bst_tree.add(2)
    bst_tree.add(4)
    bst_tree.add(5)
    output = []
    callback = lambda x: output.append(x)
    bst.BST.post_order_traverse(bst_tree.root, callback=callback)
    self.assertEqual(output, [1, 2, 4, 5, 3])

  def test_bst_02(self):
    bst_tree = bst.BST()
    bst_tree.add(3)
    bst_tree.add(1)
    bst_tree.add(2)
    bst_tree.add(4)
    bst_tree.add(5)
    output = []
    callback = lambda x: output.append(x)
    bst.BST.in_order_traverse(bst_tree.root, callback=callback)
    self.assertEqual(output, [1, 2, 3, 4, 5])

  def test_bst_03(self):
    bst_tree = bst.BST()
    bst_tree.add(3)
    bst_tree.add(1)
    bst_tree.add(2)
    bst_tree.add(4)
    bst_tree.add(5)
    self.assertEqual(3, bst.BST.get_maximum_depth(bst_tree.root))

  def test_bst_04(self):
    bst_tree = bst.BST()
    bst_tree.add(3)
    bst_tree.add(1)
    bst_tree.add(2)
    bst_tree.add(4)
    bst_tree.add(5)
    self.assertFalse(bst.BST.contains(bst_tree.root, 11))
    self.assertTrue(bst.BST.contains(bst_tree.root, 4))

  def test_bst_05(self):
    bst_tree = bst.BST()
    bst_tree.add(3)
    bst_tree.add(1)
    bst_tree.add(2)
    bst_tree.add(4)
    bst_tree.add(5)
    output = []
    callback = lambda x: output.append(x)
    bst.BST.bft(bst_tree.root, callback=callback)
    self.assertEqual(output, [3, 1, 4, 2, 5])

  def test_bst_06(self):
    bst_tree = bst.BST()
    bst_tree.add(3)
    bst_tree.add(1)
    bst_tree.add(2)
    bst_tree.add(4)
    bst_tree.add(5)
    bst_tree.delete(bst_tree.root, 2)
    self.assertFalse(bst.BST.contains(bst_tree.root, 2))


if __name__ == '__main__':
  unittest.main()
