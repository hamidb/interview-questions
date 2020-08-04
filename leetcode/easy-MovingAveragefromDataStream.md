Moving Average from Data Stream (Leetcode #346)
===============================
### Easy

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

### Example:
```
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
```

Solution
========
```python
# Space: O(K)
# Time: O(K)
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.buffer = []
        self.size = size
        self.idx = 0

    def next(self, val: int) -> float:
        if len(self.buffer) < self.size:
            self.buffer.append(val)
        else:
            self.buffer[self.idx] = val
            self.idx = (self.idx + 1) % self.size
        return sum(self.buffer)/len(self.buffer)
    
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```
