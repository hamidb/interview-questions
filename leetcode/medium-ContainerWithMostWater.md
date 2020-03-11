Container with Most Water (Leetcode #11)
===============================
### Medium
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
![containers](images/image0004.png)
### Example:
```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

Solution
========
Brute force solution is trivial.

We can Optimize it with two pointer solution. Once pointer start from the begining and the other one from the end. We only increment the first or decrement the second pointer only if it's smaller one.

```python
class Solution:
    # Brute Force
    # def maxArea(self, height: List[int]) -> int:
    #     max_area = 0
    #     for i in range(len(height)-1):
    #         for j in range(i+1, len(height)):
    #             w = j - i
    #             h = min(height[i], height[j])
    #             if w*h > max_area:
    #                 max_area = w*h
    #     return max_area


    # Two pointers
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height)-1
        while i < j:
            area = (j-i)*min(height[i], height[j])
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_area
```
