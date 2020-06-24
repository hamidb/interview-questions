Capacity To Ship Packages Within D Days (Leetcode #1011)
===============================
### Medium
A conveyor belt has packages that must be shipped from one port to another within `D` days.

The `i`-th package on the conveyor belt has a weight of `weights[i]`.  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `D` days.

### Example 1:

```
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
```

Note that the cargo must be shipped in the order given, so using a ship of capacity `14` and splitting the packages into parts like `(2, 3, 4, 5), (1, 6, 7), (8), (9), (10)` is not allowed. 

### Example 2:

```
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
```

### Example 3:

```
Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation: 
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
``` 

### Constraints:

```
1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500
```

Solution
========
Search on the capacity space and check if all packages can be ship within `D` days.

### Python
```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        len_w = len(weights)
        if len_w == 0: return 0
        if len_w == 1: return weights[0]
        
        lo, hi = float('-inf'), 0
        for w in weights:
            hi += w
            lo = max(lo, w)
            
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if self.days_needed(weights, mid) < D:
                hi = mid - 1  # decrease capacity
            else:
                lo = mid + 1  # increase capacity
        return lo
        
    def days_needed(self, weights, capacity):
        d = 0
        tmp_sum = 0
        for w in weights:
            tmp_sum += w
            if capacity < tmp_sum:
                d += 1
                tmp_sum = w
        return d
```

### C++
```c++
class Solution {
public:
    int shipWithinDays(vector<int>& weights, int D) {
        int lo = -0xffffffff;
        int hi = 0;
        for (const auto &w: weights) {
            lo = lo > w ? lo : w;
            hi += w;
        }
        while (lo <= hi) {
            int mid = lo + (hi-lo) / 2;
            if (daysNeeded(weights, mid) < D) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
    
    int daysNeeded(vector<int>&weights, int capacity) {
        int tmp_sum = 0;
        int d = 0;
        for (const auto &w : weights) {
            tmp_sum += w;
            if (tmp_sum > capacity) {
                tmp_sum = w;
                d++;
            }
        }
        return d;
    }
};
```
