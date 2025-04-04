Time Based Key-Value Store (Leetcode #981)
===============================
### Medium
Create a timebased key-value store class TimeMap, that supports two operations.

1. `set(string key, string value, int timestamp)`

Stores the key and value, along with the given timestamp.

2. `get(string key, int timestamp)`

Returns a value such that `set(key, value, timestamp_prev)` was called previously, with `timestamp_prev <= timestamp`.

If there are multiple such values, it returns the one with the largest `timestamp_prev`.

If there are no values, it returns the empty string `("")`.
 

### Example 1:
```
Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   
```
### Example 2:
```
Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
 ```

### Note:
All key/value strings are lowercase.

All key/value strings have length in the range [1, 100]

The timestamps for all TimeMap.set operations are strictly increasing.

`1 <= timestamp <= 10^7`

`TimeMap.set` and `TimeMap.get` functions will be called a total of 120000 times (combined) per test case.

Solution
========
```python
class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)
        self.vmap = defaultdict(list)    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append(timestamp)
        self.vmap[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        t = self.tmap[key]
        v = self.vmap[key]
        if len(t) == 0:
            return ""
        i = bisect.bisect_right(t, timestamp)
        if i-1 < len(t) and i-1 >= 0:
            return v[i-1]
        return ""
```

```python
class TimeMap:            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table: 
            self.table[key] = ([value], [timestamp])
            return
        values, times = self.table[key]
        values.append(value)
        times.append(timestamp)
        # index = bisect.bisect(times, timestamp)
        # values.insert(index, value)
        # times.insert(index, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ''
        values, times = self.table[key]
        index = bisect.bisect(times, timestamp)
        if index == 0:
            return ''
        return values[index-1]
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

```c++
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class TimeMap {
public:
    TimeMap() {}

    void set(string key, string value, int timestamp) {
        tmap[key].push_back(timestamp);
        vmap[key].push_back(value);
    }

    string get(string key, int timestamp) {
        // Retrieve the timestamps and values for the key
        auto &timestamps = tmap[key];
        auto &values = vmap[key];

        if (timestamps.empty()) {
            return ""; // No entries for the given key
        }

        // Find the position of the first timestamp greater than the given timestamp
        auto it = upper_bound(timestamps.begin(), timestamps.end(), timestamp);
        
        // If there is no valid timestamp <= the given timestamp
        if (it == timestamps.begin()) {
            return "";
        }

        // Otherwise, return the value at the last valid timestamp
        int index = it - timestamps.begin() - 1;
        return values[index];
    }

private:
    unordered_map<string, vector<int>> tmap;  // Maps key to a list of timestamps
    unordered_map<string, vector<string>> vmap;  // Maps key to a list of values
};

```
