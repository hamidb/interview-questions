Largest Rectangle in Histogram (Leetcode #84)
===============================
### Hard

Given `n` non-negative integers representing the histogram's bar height where the width of each bar is `1`, find the area of largest rectangle in the histogram.

![example1](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)

Above is a histogram where width of each bar is `1`, given `height = [2,1,5,6,2,3]`.

![example2](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)
 
The largest rectangle is shown in the shaded area, which has `area = 10` unit.

### Example:
```
Input: [2,1,5,6,2,3]
Output: 10
```

Solution
========
### Approach 5: Using Stack
#### Algorithm

In this approach, we maintain a stack. Initially, we push a `-1` onto the stack to mark the end.

We start with the leftmost bar and keep pushing the current bar's index onto the stack until we get two successive numbers in descending order,
i.e. until we get `a[i] < a[i-1]`. 

Now, we start popping the numbers from the stack until we hit a number `stack[j]` on the stack such that `height[stack[j]] <= height[i]`.
Every time we pop, we find out the area of rectangle formed using the current element as the height of the rectangle and the difference between the the current element's
index pointed to in the original array and the element `stack[top-1] -1` as the width i.e. if we pop an element `stack[top]` and `i` is the current index to which we are
pointing in the original array, the current area of the rectangle will be considered as:

`(i−stack[top−1]−1)×height[stack[top]]`.

Further, if we reach the end of the array, we pop all the elements of the stack and at every pop, this time we use the following equation to find the area:
`(stack[top]−stack[top−1])×height[stack[top]]`, where `stack[top]` refers to the element just popped. 
Thus, we can get the area of the of the largest rectangle by comparing the new area found everytime.

```python
# O(N)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque([-1])
        length = len(heights)
        max_area = 0
        for i in range(length):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()]*(length-stack[-1]-1))
        return max_area
```
