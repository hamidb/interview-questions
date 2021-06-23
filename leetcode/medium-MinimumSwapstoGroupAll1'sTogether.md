Minimum Swaps to Group All 1's Together (Leetcode #1151)
===============================
### Medium

Given a binary array `data`, return the minimum number of swaps required to group all `1`’s present in the array together in any place in the array.

### Example 1:
```
Input: data = [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
```

### Example 2:
```
Input: data = [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps needed.
```

### Example 3:
```
Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
```

### Example 4:
```
Input: data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
Output: 8
 ```

### Constraints:
```
1 <= data.length <= 105
data[i] is 0 or 1.
```

Solution
========

```python
# Assuming that there are ones 1's in the input array data, we need to find a subarray, or a window,
# of length ones and put all 1's in it by swapping 0's out. Therefore, among all windows of length ones,
# to find the minimum number of swaps required, we need to find the maximum number of 1's in the window
# so that we can make the smallest number of swaps to achieve the goal.

# T: O(N)
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)  # desired length of group
        max_ones = 0  # min swap is ones - max_ones
        cnt_ones = 0
        left = right = 0
        while right < len(data):
            cnt_ones += data[right]
            right += 1
            if right - left > ones:
                cnt_ones -= data[left]
                left += 1
            max_ones = max(max_ones, cnt_ones)
        return ones - max_ones
```
