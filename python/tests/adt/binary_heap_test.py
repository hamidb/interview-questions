# Lint as: python3
"""Tests for binary_heap."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt import binary_heap
import unittest

class BinaryHeapTest(unittest.TestCase):

  def test_binary_heap_00(self):
    heap = binary_heap.BinaryHeap()
    heap.add(2)
    heap.add(3)
    heap.add(1)
    self.assertEqual(heap.heap, [1, 3, 2])

  def test_binary_heap_01(self):
    heap = binary_heap.BinaryHeap()
    heap.buildHeap([1, 2, -3, 9, 0, -5])
    heap.clean()
    self.assertEqual(heap.heap, [])
    self.assertEqual(heap.size, 0)

  def test_binary_heap_02(self):
    heap = binary_heap.BinaryHeap()
    heap.buildHeap([1, 2, -3, 9, 0, -5])
    self.assertEqual(heap.heap, [-5, 0, -3, 9, 2, 1])
    self.assertTrue(heap.isMinHeap(0))

  def test_binary_heap_03(self):
    heap = binary_heap.BinaryHeap()
    heap.buildHeap([1, 2, -3, 9, 0, -5])
    self.assertFalse(heap.remove(-2))
    self.assertTrue(heap.remove(2))
    self.assertTrue(heap.isMinHeap(0))
    self.assertEqual(heap.heap, [-5, 0, -3, 9, 1])

  def test_binary_heap_04(self):
    heap = binary_heap.BinaryHeap()
    heap.buildHeap([1, 2, -3, 9, 0, -5])
    self.assertTrue(heap.remove(1))
    self.assertTrue(heap.isMinHeap(0))
    self.assertEqual(heap.heap, [-5, 0, -3, 9, 2])

  def test_binary_heap_05(self):
    heap = binary_heap.BinaryHeap()
    heap.buildHeap([1, 2, -3, 9, 0, -5])
    self.assertTrue(heap.remove(0))
    self.assertTrue(heap.isMinHeap(0))
    self.assertEqual(heap.heap, [-5, 1, -3, 9, 2])

  def test_binary_heap_06(self):
    heap = binary_heap.BinaryHeap()
    heap.buildHeap([1, 2, -3, 9, 0, -5])
    self.assertTrue(heap.contains(9))
    self.assertFalse(heap.contains(49))


if __name__ == '__main__':
  unittest.main()
