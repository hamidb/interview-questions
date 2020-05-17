# Lint as: python3
"""Tests for binary_heap."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from algorithm import topological_sort as topsort
import unittest

class TopSortTest(unittest.TestCase):

  def test_top_sort_00(self):
    graph = {i: [] for i in range(7)}
    graph.get(0).append(topsort.Edge(0, 1, 3));
    graph.get(0).append(topsort.Edge(0, 2, 2));
    graph.get(0).append(topsort.Edge(0, 5, 3));
    graph.get(1).append(topsort.Edge(1, 3, 1));
    graph.get(1).append(topsort.Edge(1, 2, 6));
    graph.get(2).append(topsort.Edge(2, 3, 1));
    graph.get(2).append(topsort.Edge(2, 4, 10));
    graph.get(3).append(topsort.Edge(3, 4, 5));
    graph.get(5).append(topsort.Edge(5, 4, 7));

    self.assertEqual(topsort.topological_sort(graph), [6, 0, 5, 1, 2, 3, 4])

    dists = topsort.dag_shortest_path(graph, 0);
    self.assertEqual(dists[4], 8.0)
    self.assertIsNone(dists[6] )


if __name__ == '__main__':
  unittest.main()
