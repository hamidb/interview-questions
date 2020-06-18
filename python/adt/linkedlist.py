# Lint as: python3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
  
class Node:
  def __init__(self, data, prev=None, next=None):
    self.data = data
    self.prev = prev
    self.next = next

class DoublyLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def __repr__(self):
    return ' '.join(str(i) for i in self.heap)

  def empty(self):
    return self.size == 0

  def append(self, data):
    if self.empty():
      node = Node(data, None, None)
      self.head = node
      self.tail = node
    else:
      node = Node(data, self.tail, None)
      self.tail.next = node
      self.tail = node
    self.size += 1

  def prepend(self, data):
    if self.empty():
      node = Node(data, None, None)
      self.head = node
      self.tail = node
    else:
      node = Node(data, None, self.head)
      self.head.prev = node
      self.head = node
    self.size += 1

  def insertAt(self, data, index):
    assert index >= 0 and index < self.size
    if index == 0:
      self.prepend(data)
      return
    if index == self.size-1:
      self.append(data)
      return
    tmp = self.head
    for i in range(0, index):
      tmp = tmp.next
    node = Node(data, tmp, tmp.next)
    tmp.next.prev = node
    tmp.next = node
    self.siize += 1

  def peek(self, index):
    assert not self.empty()
    assert index >= 0 and index < self.size
    if index == 0:
      return self.head.data
    if index == self.size-1:
      return self.tail.data

    tmp = self.head
    for i in range(0, index):
      tmp = tmp.next
    return tmp.data

  def popFirst(self):
    assert not self.empty()
    data = self.head.data
    self.head = self.head.next
    self.size -= 1
    if self.empty():
      self.tail = None
    else:
      self.head.prev = None
    return data

  def popLast(self):
    assert not self.empty()
    data = self.tail.data
    self.tail = self.tail.prev
    self.size -= 1
    if self.empty():
      self.head = None
    else:
      self.tail.next = None
    return data

  def remove(self, node):
    if node.prev == None:
      return self.popFirst()
    if node.next == None:
      return self.popLast()
    data = node.data
    node.prev.next = data.next
    node.next.prev = data.prev
    node.prev = node.next = None
    self.size -= 1
    return data

  def pop(self, index):
    assert not self.empty()
    assert index >= 0 and index < self.size
    tmp = self.tail
    if index > self.size / 2:
      i = self.size-1
      while i != index:
        tmp = tmp.prev
        i -= 1
    else:
      tmp = self.head
      i = 0
      while i != index:
        tmp = tmp.next
        i += 1
    return self.remove(tmp)

  def reverse(self):
    head = self.head
    if head is None or head.next is None:
      return head
    ptr0, ptr1, ptr2 = None, head, None
    while ptr1:
      ptr2 = ptr1.next
      ptr1.next = ptr0
      # next iter
      ptr0 = ptr1
      ptr1 = ptr2
    self.head = ptr0

  def traverse(self):
    trav = self.head
    output = []
    while trav != None:
      output.append(trav.data)
      trav = trav.next
    return output

  def print(self):
    string = '['
    trav = self.head
    while trav != None:
      string += str(trav.data) + ', '
      trav = trav.next
    print(string + ']')

  def find(self, data):
    if self.empty():
      return -1
    index = 0
    tmp = self.head
    while index < self.size:
      if tmp.data == data:
        return index
      tmp = tmp.next
      index += 1
    return -1

  def contains(self, data):
    return self.find(data) != -1

