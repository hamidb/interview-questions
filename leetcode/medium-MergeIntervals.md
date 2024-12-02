Merge Intervals (Leetcode #56)
===============================
### Medium

Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all
the intervals in the input.

 

### Example 1:
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

### Example 2:
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
``` 

### Constraints:
```
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
```

Solution
========

```python
# T: O(N log N)
# S: O(1)
# sort by interval start.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        # ans[0][1] holds last end point.
        for s, e in intervals[1:]:
            if s <= ans[-1][1]:
                ans[-1][1] = max(e, ans[-1][1])
            else:
                ans.append([s, e])
        return ans
```

```c++
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int L = intervals.size();
        if (L == 0)
            return vector<vector<int>>();
        
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int> &a, const std::vector<int> &b) {
            return a[0] < b[0];
        });
        vector<vector<int>> ans = {intervals[0]};
        for (int i=1; i < L; i++) {
            auto se = intervals[i];
            if (se[0] <= ans[ans.size()-1][1]) {
                ans[ans.size()-1][1] = max(ans[ans.size()-1][1], se[1]);
            } else {
                ans.push_back(se);
            }
        }
        return ans;
        
    }
};
```
