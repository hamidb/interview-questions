LFU Cache (Leetcode #460)
===============================
### Hard

Design and implement a data structure for Least Frequently Used (LFU) cache.

Implement the `LFUCache` class:

`LFUCache(int capacity)` Initializes the object with the capacity of the data structure.
`int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.
`void put(int key, int value)` Sets or inserts the `value` if the key is not already present. When the cache reaches its capacity,
it should invalidate the least frequently used item before inserting a new item. For this problem, when there is a tie
(i.e., two or more keys with the same frequency), the least recently used key would be evicted.
Notice that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted.
This number is set to zero when the item is removed.

### Follow up:
Could you do both operations in O(1) time complexity?

 

### Example 1:
```
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
LFUCache lFUCache = new LFUCache(2);
lFUCache.put(1, 1);
lFUCache.put(2, 2);
lFUCache.get(1);      // return 1
lFUCache.put(3, 3);   // evicts key 2
lFUCache.get(2);      // return -1 (not found)
lFUCache.get(3);      // return 3
lFUCache.put(4, 4);   // evicts key 1.
lFUCache.get(1);      // return -1 (not found)
lFUCache.get(3);      // return 3
lFUCache.get(4);      // return 4
```
 

### Constraints:
```
0 <= capacity, key, value <= 104
At most 105 calls will be made to get and put.
```

Solution
========
Use a map (`key -> [value, freq])` and another map (`freq -> DList (OrderedDict)`) where DList stores keys in order.

```python
# put() and get(): O(1)

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 1
        self.key2pair = {}  # pair: (value, freq)
        # using OrderedDict as a Doubly Linked List
        self.freq2dlist = defaultdict(OrderedDict)  # DList: {items -> key}
        

    def get(self, key: int) -> int:
        if key not in self.key2pair:
            return -1
        v, f = self.key2pair[key]
        self.key2pair[key] = v, f+1
        self.freq2dlist[f].pop(key)
        # if no more item with f exists and f was min_freq, then update min_freq
        if len(self.freq2dlist[f]) == 0 and f == self.min_freq:
            self.min_freq += 1
        self.freq2dlist[f+1][key] = None  # create a dummy item
        return v
        

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.key2pair:
            self.key2pair[key] = value, self.key2pair[key][1]
            self.get(key)
            return
        
        if self.capacity <= len(self.key2pair):
            # evict in LFU order
            k, _ = self.freq2dlist[self.min_freq].popitem(last=False)  # FIFO order
            del self.key2pair[k]
        
        # Add a new item
        self.min_freq = 1
        self.freq2dlist[1][key] = None
        self.key2pair[key] = value, 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

C++
```c++
#include <unordered_map>
#include <map>
#include <list>
#include <utility>

class LFUCache {
private:
    int capacity;
    int minFreq;
    
    // Maps a key to its value and frequency
    std::unordered_map<int, std::pair<int, int>> key2pair;
    
    // Maps a frequency to a doubly linked list of keys
    std::unordered_map<int, std::list<int>> freq2list;
    
    // Maps a key to its position in the doubly linked list
    std::unordered_map<int, std::list<int>::iterator> key2iter;

    void updateFrequency(int key) {
        auto [value, freq] = key2pair[key];
        key2pair[key].second = freq + 1; // Increment frequency
        
        // Remove key from current frequency list
        freq2list[freq].erase(key2iter[key]);

        // If the current frequency was the minimum and its list is now empty, increment minFreq
        if (freq2list[freq].empty() && freq == minFreq) {
            minFreq++;
        }

        // Add key to the new frequency list
        freq2list[freq + 1].push_front(key);
        key2iter[key] = freq2list[freq + 1].begin();
    }

public:
    LFUCache(int capacity) : capacity(capacity), minFreq(0) {}

    int get(int key) {
        if (key2pair.find(key) == key2pair.end()) {
            return -1; // Key not found
        }
        
        // Update frequency
        updateFrequency(key);
        return key2pair[key].first;
    }

    void put(int key, int value) {
        if (capacity <= 0) return;

        if (key2pair.find(key) != key2pair.end()) {
            // Key exists, update its value and frequency
            key2pair[key].first = value;
            updateFrequency(key);
            return;
        }

        if (key2pair.size() >= capacity) {
            // Evict least frequently used key
            int evictKey = freq2list[minFreq].back(); // Get the oldest key in the minFreq list
            freq2list[minFreq].pop_back();
            key2pair.erase(evictKey);
            key2iter.erase(evictKey);
        }

        // Insert new key
        minFreq = 1;
        key2pair[key] = {value, 1};
        freq2list[1].push_front(key);
        key2iter[key] = freq2list[1].begin();
    }
};

```
