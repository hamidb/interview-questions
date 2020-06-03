# Lint as: python3
"""Tests for isomorphic trees."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt.graph import Graph
from algorithm.isomorphic_trees import IsomorphicTrees, TreeNode
import unittest

class IsomorphicTreesTest(unittest.TestCase):

  def test_isomorphic_trees_00(self):
    g = Graph(9)
    g.add_undirected_edge(0, 1, 0)
    g.add_undirected_edge(2, 1, 0)
    g.add_undirected_edge(2, 3, 0)
    g.add_undirected_edge(3, 4, 0)
    g.add_undirected_edge(5, 3, 0)
    g.add_undirected_edge(2, 6, 0)
    g.add_undirected_edge(6, 7, 0)
    g.add_undirected_edge(6, 8, 0)
    centers = IsomorphicTrees.get_tree_centers(g)
    self.assertCountEqual(centers, [2])

  def test_isomorphic_trees_01(self):
    g = Graph(2)
    g.add_undirected_edge(0, 1, 0)
    centers = IsomorphicTrees.get_tree_centers(g)
    self.assertCountEqual(centers, [0, 1])

  def test_isomorphic_trees_02(self):
    g = Graph(7)
    g.add_undirected_edge(0, 1, 0)
    g.add_undirected_edge(1, 2, 0)
    g.add_undirected_edge(2, 3, 0)
    g.add_undirected_edge(3, 4, 0)
    g.add_undirected_edge(4, 5, 0)
    g.add_undirected_edge(4, 6, 0)
    centers = IsomorphicTrees.get_tree_centers(g)
    self.assertCountEqual(centers, [2, 3])

  def test_isomorphic_trees_03(self):
    g = Graph(9)
    g.add_undirected_edge(0, 1, 0)
    g.add_undirected_edge(2, 1, 0)
    g.add_undirected_edge(2, 3, 0)
    g.add_undirected_edge(3, 4, 0)
    g.add_undirected_edge(5, 3, 0)
    g.add_undirected_edge(2, 6, 0)
    g.add_undirected_edge(6, 7, 0)
    g.add_undirected_edge(6, 8, 0)
    root_tree = IsomorphicTrees.root_tree(g, 6)
    keys = [c.key for c in root_tree.get_children()]
    self.assertEqual(root_tree.key, 6)
    self.assertIsNone(root_tree.parent)
    self.assertCountEqual(keys, [2, 7, 8])

  def test_isomorphic_trees_04(self):
    g1 = Graph(5)
    g2 = Graph(5)
    g1.add_undirected_edge(2, 0, 0)
    g1.add_undirected_edge(3, 4, 0)
    g1.add_undirected_edge(2, 1, 0)
    g1.add_undirected_edge(2, 3, 0)
    g2.add_undirected_edge(1, 0, 0)
    g2.add_undirected_edge(2, 4, 0)
    g2.add_undirected_edge(1, 3, 0)
    g2.add_undirected_edge(1, 2, 0)
    self.assertEqual(IsomorphicTrees.isomorphic_equal(g1, g2), True)

  def test_isomorphic_trees_05(self):
    g = Graph(10)
    g.add_undirected_edge(0, 2, 0)
    g.add_undirected_edge(0, 1, 0)
    g.add_undirected_edge(0, 3, 0)
    g.add_undirected_edge(2, 6, 0)
    g.add_undirected_edge(2, 7, 0)
    g.add_undirected_edge(1, 4, 0)
    g.add_undirected_edge(1, 5, 0)
    g.add_undirected_edge(5, 9, 0)
    g.add_undirected_edge(3, 8, 0)

    root0 = IsomorphicTrees.root_tree(g, 0)
    self.assertEqual(IsomorphicTrees._encode(root0), "(((())())(()())(()))")


if __name__ == '__main__':
  unittest.main()
