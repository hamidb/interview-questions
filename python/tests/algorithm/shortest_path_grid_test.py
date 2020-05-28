# Lint as: python3
"""Tests for shortest_path_grid."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from algorithm import shortest_path_grid
import unittest

class ShortestPathGridTest(unittest.TestCase):

  def test_shortes_path_00(self):

    grid = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]
    move, path = shortest_path_grid.shortest_path(grid, [0,4], [4, 4])
    self.assertEqual(move, 8)
    self.assertEqual(path, [[0, 4], [0, 3], [1, 3], [1, 2], [2, 2], [3, 2],
                            [4, 2], [4, 3], [4, 4]])
  
if __name__ == '__main__':
  unittest.main()
