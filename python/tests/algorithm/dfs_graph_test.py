# Lint as: python3
"""Tests for binary_heap."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt.graph import Graph
from algorithm import dfs_graph
import unittest

class DFSGraphTest(unittest.TestCase):

  def setUp(self):
    self.g = Graph(5)
    self.g.add_edge(0, 1, 4)
    self.g.add_edge(0, 2, 1)
    self.g.add_edge(2, 1, 2)
    self.g.add_edge(1, 3, 1)
    self.g.add_edge(2, 3, 5)
    self.g.add_edge(3, 4, 3)

  def test_dfs_00(self):
    self.assertEqual(dfs_graph.dfs_recursive(self.g), self.g.size)

  def test_dfs_01(self):
    self.assertEqual(dfs_graph.dfs_iterative(self.g), self.g.size)


if __name__ == '__main__':
  unittest.main()
