# Lint as: python3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt import linkedlist
import unittest

class LinkedListTest(unittest.TestCase):

  def test_linkedlist_00(self):
    lst = linkedlist.DoublyLinkedList()
    lst.append(1)
    lst.prepend(2)
    lst.insertAt(3, 1)
    lst.insertAt(4, 2)
    self.assertEqual(lst.traverse(), [2, 1, 3, 4])

  def test_linkedlist_01(self):
    lst = linkedlist.DoublyLinkedList()
    lst.append(1)
    lst.prepend(2)
    lst.insertAt(3, 1)
    lst.insertAt(4, 2)
    self.assertEqual(2, lst.peek(0))
    self.assertEqual(1, lst.peek(1))
    self.assertEqual(4, lst.peek(3))
    self.assertEqual(2, lst.pop(0))
    self.assertEqual(4, lst.pop(2))

  def test_linkedlist_02(self):
    lst = linkedlist.DoublyLinkedList()
    lst.append(1)
    lst.prepend(2)
    lst.insertAt(3, 1)
    lst.insertAt(4, 2)
    self.assertEqual(3, lst.find(4))
    self.assertEqual(-1, lst.find(7))
    self.assertFalse(lst.contains(-7))

  def test_linkedlist_03(self):
    lst = linkedlist.DoublyLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)
    lst.reverse()
    self.assertEqual(lst.traverse(), [5, 4, 3, 2, 1])


if __name__ == '__main__':
  unittest.main()
