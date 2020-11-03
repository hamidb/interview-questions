Range Module (Leetcode #715)
===============================
### Hard

A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

`addRange(int left, int right)` Adds the half-open interval `[left, right)`, tracking every real number in that interval.
Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval `[left, right)` that are not already tracked.
`queryRange(int left, int right)` Returns true if and only if every real number in the interval `[left, right)` is currently being tracked.
`removeRange(int left, int right)` Stops tracking every real number currently being tracked in the interval `[left, right)`.

### Example 1:
```
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
```

### Note:
```
A half open interval [left, right) denotes all real numbers left <= x < right.
0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
The total number of calls to addRange in a single test case is at most 1000.
The total number of calls to queryRange in a single test case is at most 5000.
The total number of calls to removeRange in a single test case is at most 1000.
```

Solution
========
TreeMap, Segment Tree, Ordered List

```python
# add/remove -> O(N) because of collapsing the range (list slicing)
# query -> O(logN)
class RangeModule:

    def __init__(self):
        # stores ordered list
        # even index -> start of interval
        # odd index -> end of interval
        self.arr = []
        
    def addRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.arr, left)  # first smaller or equal
        j = bisect.bisect_right(self.arr, right)  # last larger or equal
        # i is even -> left is a new start point
        # j is even -> right is a new end point
        self.arr[i:j] = [left] * (i%2 == 0) + [right] * (j%2 == 0)  # O(N)

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.arr, left)
        j = bisect.bisect_left(self.arr, right)
        # returns true if and only if (i,j) lie within an existing range
        return i==j and (i%2 == 1)

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.arr, left)  # first smaller or equal
        j = bisect.bisect_right(self.arr, right)  # last larger or equal
        # i is odd -> left is a new start point
        # j is odd -> right is a new end point
        self.arr[i:j] = [left] * (i%2 == 1) + [right] * (j%2 == 1)  # O(N)
          
            
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
```
