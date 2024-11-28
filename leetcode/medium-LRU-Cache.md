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
simpler version
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map: key -> node
        # Dummy head and tail to simplify adding/removing nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the doubly linked list."""
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def _add(self, node: Node):
        """Add a node to the end of the doubly linked list (most recently used)."""
        prev, next = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move node to the end to mark it as recently used
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])  # Remove the old node
        node = Node(key, value)
        self._add(node)  # Add the new node
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # Remove the least recently used node
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
```

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

### **C++**
```c++
class Node {
public:
    Node(int key, int data, Node* prev=NULL, Node* next=NULL) {
        _key = key;
        _data = data;
        _prev = prev;
        _next = next;
    }
    int _data;
    int _key;
    Node* _next;
    Node* _prev;
};
class LRUCache {
public:
    LRUCache(int capacity) {
        _capacity = capacity;
        _size = 0;
        _head = NULL;
        _tail = NULL;
    }
    
    int get(int key) {
        if (_table.count(key) == 0) {
            return -1;
        }
        auto node = _remove(_table[key]);
        _preppend(key, node->_data);
        return node->_data;
    }
    
    void put(int key, int value) {
        if (_table.count(key) != 0) {
            auto node = _remove(_table[key]);
            delete node;
            _preppend(key, value);
        } else {
            if (_size < _capacity) {
                _preppend(key, value);
            } else {
                auto node = _popLast();
                _table.erase(node->_key);
                delete node;
                _preppend(key, value);
            }
        }
        
    }
    
    bool _empty() {
        return (_size == 0);
    }
    
    Node* _popFirst() {
        Node* node = _head;
        _head = node->_next;
        _size--;
        if (_empty()) {
            _tail = NULL;    
        } else {
            _head->_prev = NULL;
        }
        return node;
    }
    
    Node* _popLast() {
        Node* node = _tail;
        _tail = node->_prev;
        _size--;
        if (_empty()) {
            _head = NULL;
        } else {
            _tail->_next = NULL;   
        }
        return node;
    }
    
    void _preppend(int key, int value) {
        if (_empty()) {
            Node* node = new Node(key, value);
            _head = node;
            _tail = node;
        } else {
            Node* node = new Node(key, value, NULL, _head);
            _head->_prev = node;
            _head = node;
        }
        _table[key] = _head;
        _size++;
    }
    
    Node* _remove(Node* node) {
        if (node->_prev == NULL) {
            return _popFirst();
        }
        if (node->_next == NULL) {
            return _popLast();
        }
        node->_prev->_next = node->_next;
        node->_next->_prev = node->_prev;
        _size--;
        return node;
    }
    
    std::unordered_map<int, Node*> _table;
    int _capacity;
    int _size;
    Node* _head;
    Node* _tail;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```
