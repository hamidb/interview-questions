# Lint as: python3
"""Tests for binary_heap."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt.graph import Graph
from algorithm import dijkstra
import unittest

class TopSortTest(unittest.TestCase):

  def setUp(self):
    self.g = Graph(5)
    self.g.add_edge(0, 1, 4)
    self.g.add_edge(0, 2, 1)
    self.g.add_edge(2, 1, 2)
    self.g.add_edge(1, 3, 1)
    self.g.add_edge(2, 3, 5)
    self.g.add_edge(3, 4, 3)


  def test_dijkstra_00(self):
    dist, prev = dijkstra.dijkstra(self.g, 0, 4)
    self.assertEqual(dist, 7)
    self.assertEqual(prev, [None, 2, 0, 1, 3])

  def test_dijkstra_01(self):
    path = dijkstra.reconstruct_shortest_path(self.g, 0, 4)
    self.assertEqual(path, [0, 2, 1, 3, 4])


if __name__ == '__main__':
  unittest.main()
