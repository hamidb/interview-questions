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

[![Explanation](https://img.youtube.com/vi/vcv3REtIvEo/0.jpg)](https://youtu.be/vcv3REtIvEo)

```python
# O(N)
class Solution:
    # Maintain a monotonic increasing stack.
    # Every time we pop an element, we compute area by finding left and right limits.
    # left limit is simply the element on the top of stack.
    # the right limit is the current index we are iterating.
    # area = (i - stack[-1] - 1) * height of popped element. 
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
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        left, right = length*[None], length*[None]
        stack = deque([])

        # fill left limit
        for i in range(length):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]+1
            else:
                left[i] = 0
            stack.append(i)

        stack = deque([])
        
        # fill right limit
        for i in range(length-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]-1
            else:
                right[i] = length-1
            stack.append(i)

        max_area = 0
        for i in range(len(left)):
            max_area = max(max_area, heights[i]*(right[i]-left[i]+1))
        return max_area 
```

### Divide and conquer
```python
# T: O(n log n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calculateArea(heights: List[int], start: int, end: int) -> int:
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(
                heights[min_index] * (end - start + 1),
                calculateArea(heights, start, min_index - 1),
                calculateArea(heights, min_index + 1, end),
            )

        return calculateArea(heights, 0, len(heights) - 1)

```

C++

```c++
class Solution {
public:
    // We can observe that the max rectangle has at least one bar fully included in the rectangle
    // for each bar i: 1. if we know the first bar on the left which has h[left] < h[i] 
    //                 2. and we know the first bar on the right which has h[right] < h[i]
    //                 3. then max area = (right-left+1) * h[i]
    // Now we want to find a way to access left and right limits in O(1) using monotonic stack
    // monotonic increasing -> it always contains increasing values
    int largestRectangleArea(vector<int>& heights) {
        int L = heights.size();

        // Find the left limits for each bar i
        vector<int> left(L);  // index of left limit
        vector<int> right(L);  // index of right limit        
        vector<int> stack;
        for (int i=0; i < L; i++) {
            while (stack.size() > 0 && heights[stack.back()] >= heights[i]) {
                stack.pop_back();
            }
            if (stack.size() > 0) {
                left[i] = stack.back() + 1;                
            } else {
                left[i] = 0;
            }
            stack.push_back(i);
        }

        stack.clear();
        for (int i=L-1; i >= 0; i--) {
            while (stack.size() > 0 && heights[stack.back()] >= heights[i]) {
                stack.pop_back();
            }
            if (stack.size() > 0) {
                
                right[i] = stack.back() - 1;
            } else {
                right[i] = L-1;
            }
            stack.push_back(i);
        }

        int max_value = 0;
        for (int i=0; i < left.size(); i++) {
            max_value = max(max_value, (right[i] - left[i] + 1) * heights[i]);
        }
        return max_value;
    }
};
```
