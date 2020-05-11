LRU Cache (Leetcode #146)
===============================
### Medium
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

`put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:

Could you do both operations in O(1) time complexity?

#### Example:
```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

Solution
========
[![LRU Cache explanation](https://img.youtube.com/vi/S6IfqDXWa10/0.jpg)](https://www.youtube.com/watch?v=S6IfqDXWa10)

```python
class LRUCache:

    class Node:
        def __init__(self, key, data, prev, next):
            self.key = key  # keep track of key so we can delete from table
            self.data = data
            self.prev = prev
            self.next = next
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}  # key: node
        self.head = None
        self.tail = None
        self.size = 0
        
    def _empty(self):
        return self.size == 0
    
    def _popLast(self):
        node = self.tail
        self.tail = self.tail.prev
        self.size -= 1
        if self._empty():
            self.head = None
        else:
            self.tail.next = None
        return node
    
    def _popFirst(self):
        node = self.head
        self.head = self.head.next
        self.size -= 1
        if self._empty():
            self.tail = None
        else:
            self.head.prev = None
        return node
    
    def _prepend(self, key, value):
        if self._empty():
            node = self.Node(key, value, None, None)
            self.head = node
            self.tail = node
        else:
            node = self.Node(key, value, None, self.head)
            self.head.prev = node
            self.head = node
        self.table[key] = self.head
        self.size += 1

    def _remove(self, node):
        if node.prev == None:
            return self._popFirst()
        if node.next == None:
            return self._popLast()    
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node
        
    def get(self, key: int) -> int:
        if key in self.table:
            node = self._remove(self.table[key])
            self._prepend(key, node.data)
            return node.data
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self._remove(self.table[key])
            self._prepend(key, value)      
        else:
            if self.size < self.capacity:
                self._prepend(key, value)
            else:
                node = self._popLast()
                del self.table[node.key]
                self._prepend(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
