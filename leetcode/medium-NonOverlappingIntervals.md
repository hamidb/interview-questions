Non-Overlapping Intervals (Leetcode #435)
===============================
### Medium

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

### Example 1:

Input: `[[1,2],[2,3],[3,4],[1,3]]`

Output: `1`

Explanation: `[1,3]` can be removed and the rest of intervals are non-overlapping.

### Example 2:

Input: `[[1,2],[1,2],[1,2]]`

Output: `2`

Explanation: You need to remove two `[1,2]` to make the rest of intervals non-overlapping.

### Example 3:
Input: `[[1,2],[2,3]]`

Output: `0`

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

### Note:

1. You may assume the interval's end point is always bigger than its start point.
2. Intervals like `[1,2]` and `[2,3]` have borders "touching" but they don't overlap each other.

Solution
========

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # |-------||------||------|
        #           |-||-||-|

        # Sorting by start point
        # |-------|
        #          |------|
        #           |-|                x
        #              |-|             x
        #                 |-|
        #                  |------|    x

        # Sorting by end point is the solution:

        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[1])

        end = intervals[0][0]
        remove = 0
        for i in intervals:
            start = i[0]
            if start < end:
                remove += 1
            else:
                end = i[1]
        return remove
```
### **C++**
```c++
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() <= 1) return 0;
        std::sort(intervals.begin(), intervals.end(), [](const vector<int>& v1, const vector<int>& v2){return v1[1] < v2[1];});
        int remove = 0;
        int end = intervals[0][0];
        for (const auto &v: intervals) {
            if (v[0] < end)
                remove++;
            else
                end = v[1];
        }
        return remove;
    }
};
```
