# Lint as: python3
"""Tests for union_find."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt import union_find
import unittest

class UnionFindTest(unittest.TestCase):

  def test_union_find_00(self):
    uf = union_find.UnionFind(5)
    self.assertEqual(uf.component_nums(), 5);
    uf.unify(0, 1)
    self.assertEqual(uf.component_nums(), 4)
    uf.unify(1, 0)
    self.assertEqual(uf.component_nums(), 4)
    uf.unify(1, 2)
    self.assertEqual(uf.component_nums(), 3)
    uf.unify(0, 2)
    self.assertEqual(uf.component_nums(), 3)
    uf.unify(2, 1)
    self.assertEqual(uf.component_nums(), 3)
    uf.unify(3, 4)
    self.assertEqual(uf.component_nums(), 2)
    uf.unify(4, 3)
    self.assertEqual(uf.component_nums(), 2)
    uf.unify(1, 3)
    self.assertEqual(uf.component_nums(), 1)
    uf.unify(4, 0)
    self.assertEqual(uf.component_nums(), 1)

  def test_union_find_01(self):
    uf = union_find.UnionFind(5)
    self.assertEqual(uf.component_size(0), 1)
    self.assertEqual(uf.component_size(1), 1)
    self.assertEqual(uf.component_size(2), 1)
    self.assertEqual(uf.component_size(3), 1)
    self.assertEqual(uf.component_size(4), 1)

    uf.unify(0, 1)
    self.assertEqual(uf.component_size(0), 2)
    self.assertEqual(uf.component_size(1), 2)
    self.assertEqual(uf.component_size(2), 1)
    self.assertEqual(uf.component_size(3), 1)
    self.assertEqual(uf.component_size(4), 1)

    uf.unify(1, 0)
    self.assertEqual(uf.component_size(0), 2)
    self.assertEqual(uf.component_size(1), 2)
    self.assertEqual(uf.component_size(2), 1)
    self.assertEqual(uf.component_size(3), 1)
    self.assertEqual(uf.component_size(4), 1)

    uf.unify(1, 2)
    self.assertEqual(uf.component_size(0), 3)
    self.assertEqual(uf.component_size(1), 3)
    self.assertEqual(uf.component_size(2), 3)
    self.assertEqual(uf.component_size(3), 1)
    self.assertEqual(uf.component_size(4), 1)

    uf.unify(0, 2)
    self.assertEqual(uf.component_size(0), 3)
    self.assertEqual(uf.component_size(1), 3)
    self.assertEqual(uf.component_size(2), 3)
    self.assertEqual(uf.component_size(3), 1)
    self.assertEqual(uf.component_size(4), 1)

    uf.unify(2, 1)
    self.assertEqual(uf.component_size(0), 3)
    self.assertEqual(uf.component_size(1), 3)
    self.assertEqual(uf.component_size(2), 3)
    self.assertEqual(uf.component_size(3), 1)
    self.assertEqual(uf.component_size(4), 1)

    uf.unify(3, 4)
    self.assertEqual(uf.component_size(0), 3)
    self.assertEqual(uf.component_size(1), 3)
    self.assertEqual(uf.component_size(2), 3)
    self.assertEqual(uf.component_size(3), 2)
    self.assertEqual(uf.component_size(4), 2)

    uf.unify(4, 3)
    self.assertEqual(uf.component_size(0), 3)
    self.assertEqual(uf.component_size(1), 3)
    self.assertEqual(uf.component_size(2), 3)
    self.assertEqual(uf.component_size(3), 2)
    self.assertEqual(uf.component_size(4), 2)

    uf.unify(1, 3)
    self.assertEqual(uf.component_size(0), 5)
    self.assertEqual(uf.component_size(1), 5)
    self.assertEqual(uf.component_size(2), 5)
    self.assertEqual(uf.component_size(3), 5)
    self.assertEqual(uf.component_size(4), 5)

    uf.unify(4, 0)
    self.assertEqual(uf.component_size(0), 5)
    self.assertEqual(uf.component_size(1), 5)
    self.assertEqual(uf.component_size(2), 5)
    self.assertEqual(uf.component_size(3), 5)
    self.assertEqual(uf.component_size(4), 5)

  def test_union_find_02(self):
    sz = 7
    uf = union_find.UnionFind(sz);
    for i in range(sz):
      self.assertTrue(uf.is_connected(i, i))

    uf.unify(0, 2)
    self.assertTrue(uf.is_connected(0, 2))
    self.assertTrue(uf.is_connected(2, 0))
    self.assertFalse(uf.is_connected(0, 1))
    self.assertFalse(uf.is_connected(3, 1))
    self.assertFalse(uf.is_connected(6, 4))
    self.assertFalse(uf.is_connected(5, 0))

    for i in range(sz):
      self.assertTrue(uf.is_connected(i, i))
    uf.unify(3, 1)
    self.assertTrue(uf.is_connected(0, 2))
    self.assertTrue(uf.is_connected(2, 0))
    self.assertTrue(uf.is_connected(1, 3))
    self.assertTrue(uf.is_connected(3, 1))
    self.assertFalse(uf.is_connected(0, 1))
    self.assertFalse(uf.is_connected(1, 2))
    self.assertFalse(uf.is_connected(2, 3))
    self.assertFalse(uf.is_connected(1, 0))
    self.assertFalse(uf.is_connected(2, 1))
    self.assertFalse(uf.is_connected(3, 2))
    self.assertFalse(uf.is_connected(1, 4))
    self.assertFalse(uf.is_connected(2, 5))
    self.assertFalse(uf.is_connected(3, 6))

    for i in range(sz):
      self.assertTrue(uf.is_connected(i, i))
    uf.unify(2, 5)
    self.assertTrue(uf.is_connected(0, 2))
    self.assertTrue(uf.is_connected(2, 0))
    self.assertTrue(uf.is_connected(1, 3))
    self.assertTrue(uf.is_connected(3, 1))
    self.assertTrue(uf.is_connected(0, 5))
    self.assertTrue(uf.is_connected(5, 0))
    self.assertTrue(uf.is_connected(5, 2))
    self.assertTrue(uf.is_connected(2, 5))
    self.assertFalse(uf.is_connected(0, 1))
    self.assertFalse(uf.is_connected(1, 2))
    self.assertFalse(uf.is_connected(2, 3))
    self.assertFalse(uf.is_connected(1, 0))
    self.assertFalse(uf.is_connected(2, 1))
    self.assertFalse(uf.is_connected(3, 2))
    self.assertFalse(uf.is_connected(4, 6))
    self.assertFalse(uf.is_connected(4, 5))
    self.assertFalse(uf.is_connected(1, 6))

    for i in range(sz):
      self.assertTrue(uf.is_connected(i, i))
    uf.unify(1, 2)
    uf.unify(3, 4)
    uf.unify(4, 6)

    for i in range(sz):
      for j in range(sz):
        self.assertTrue(uf.is_connected(i, j))


if __name__ == '__main__':
  unittest.main()
