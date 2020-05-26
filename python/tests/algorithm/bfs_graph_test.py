# Lint as: python3
"""Tests for bfs_graph."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt.graph import Graph
from algorithm import bfs_graph
import unittest

class BFSGraphTest(unittest.TestCase):

  def setUp(self):
    self.g = Graph(13)
    self.g.add_undirected_edge(0, 7, 1)
    self.g.add_undirected_edge(0, 9, 1)
    self.g.add_undirected_edge(0, 11, 1)
    self.g.add_undirected_edge(7, 11, 1)
    self.g.add_undirected_edge(7, 6, 1)
    self.g.add_undirected_edge(7, 3, 1)
    self.g.add_undirected_edge(6, 5, 1)
    self.g.add_undirected_edge(3, 4, 1)
    self.g.add_undirected_edge(2, 3, 1)
    self.g.add_undirected_edge(2, 12, 1)
    self.g.add_undirected_edge(12, 8, 1)
    self.g.add_undirected_edge(8, 1, 1)
    self.g.add_undirected_edge(1, 10, 1)
    self.g.add_undirected_edge(10, 9, 1)
    self.g.add_undirected_edge(9, 8, 1)

  def test_bfs_00(self):
    path = bfs_graph.bfs_path(self.g, start=10, end=5)
    self.assertEqual(path, [10, 9, 0, 7, 6, 5])


if __name__ == '__main__':
  unittest.main()
