# Lint as: python3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class BinaryHeap:

  def __init__(self):
    self.heap = []

  def __repr__(self):
    return ' '.join(str(i) for i in self.heap)

  def compare(self, v1, v2):
    if v1 == v2:
      return 0
    if v1 < v2:
      return -1
    return 1

  @property
  def size(self):
    return len(self.heap)

  def empty(self):
    return len(self.heap) == 0

  def buildHeap(self, elements):
    assert self.size == 0
    for elem in elements:
      self.add(elem)

  def clean(self):
    self.heap = []

  def add(self, data):
    self.heap.append(data)
    self._trickleUp(self.size-1)

  def removeAt(self, pos):
    assert pos < self.size
    self._swap(pos, self.size-1)
    removed = self.heap.pop()
    if pos == self.size-1:
      return removed
    elem = self.heap[pos]
    self._trickleDown(pos)
    # trickleUp if no difference after trickleDown.
    if self.compare(elem, self.heap[pos]) == 0:
      self._trickleUp(pos)
    return removed

  def remove(self, key):
    index = self.find(key)
    if index == -1:
      return False
    self.removeAt(index)
    return True

  def find(self, key):
    for i in range(self.size):
      if self.compare(self.heap[i], key) == 0:
        return i
    return -1

  def contains(self, key):
    return self.find(key) != -1

  def isMinHeap(self, i):
    if i >= self.size:
      return True
    left = 2*i + 1
    right = 2*i + 1
    if left < self.size and self.compare(self.heap[left], self.heap[i]) < 0:
      return False
    if right < self.size  and self.compare(self.heap[right], self.heap[i]) < 0:
      return False
    return self.isMinHeap(left) and self.isMinHeap(right)

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def _trickleUp(self, pos):
    parent = (pos - 1) // 2
    if parent >= 0 and self.compare(self.heap[pos], self.heap[parent]) < 0:
      self._swap(pos, parent)
      self._trickleUp(parent)

  def _trickleDown(self, pos):
    left_child = 2*pos + 1
    right_child = 2*pos + 2
    if left_child >= self.size:
      return
    smallest = self._getMinChild(pos)
    if self.compare(self.heap[smallest], self.heap[pos]) < 0:
      self._swap(smallest, pos)
      self._trickleDown(self, smallest)

  def _getMinChild(self, pos):
    assert 2*pos + 1 < self.size
    left = 2*pos + 1
    right = 2*pos + 2
    smallest = left
    if right < self.size and self.compare(self.heap[left], self.heap[right]) > 0:
      smallest = right
    return smallest

if __name__ == '__main__':
  heap = BinaryHeap()
  heap.add(2)
  heap.add(3)
  heap.add(1)
  assert heap.heap == [1, 3, 2]
  heap.clean()
  assert heap.size == 0
  heap.buildHeap([1, 2, -3, 9, 0, -5])
  assert heap.heap == [-5, 0, -3, 9, 2, 1]
  assert heap.isMinHeap(0)
  assert heap.remove(-2) == False
  assert heap.remove(2)
  assert heap.isMinHeap(0)
  assert heap.heap == [-5, 0, -3, 9, 1]
  heap.add(2)
  assert heap.remove(1)
  assert heap.isMinHeap(0)
  assert heap.heap == [-5, 0, -3, 9, 2]
  heap.add(1)
  heap.remove(0)
  assert heap.isMinHeap(0)
  assert heap.heap == [-5, 1, -3, 9, 2]
  assert heap.contains(9)
  assert heap.contains(49) == False

#  lst.insertAt(3, 1)
#  lst.print()
#  lst.insertAt(4, 2)
#  lst.print()
#  assert 2 == lst.peek(0)
#  assert 1 == lst.peek(1)
#  assert 4 == lst.peek(3)
#  assert 2 == lst.pop(0)
#  assert 4 == lst.pop(2)
#  lst.print()
#  lst.append(1)
#  lst.append(5)
#  lst.append(7)
#  lst.print()
#  assert 4 == lst.find(7)
#  assert -1 == lst.find(-7)
#  assert not lst.contains(-7)
#  assert lst.contains(7)
#
