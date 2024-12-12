Maximum Number of Visible Points (Leetcode #1610)
===============================
### Hard

You are given an array `points`, an integer angle, and your location, where `location = [posx, posy]` and `points[i] = [xi, yi]` both denote integral coordinates
on the `X-Y` plane.

Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed.
Your field of view in degrees is represented by `angle`, determining how wide you can see from any given view direction. Let `d` be the amount in degrees that you rotate
counterclockwise. Then, your field of view is the inclusive range of angles `[d - angle/2, d + angle/2]`.


You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east direction from your position is in your field of 
view.

There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation.
Points do not obstruct your vision to other points.

Return the maximum number of points you can see.

 

### Example 1:
![ex1](https://assets.leetcode.com/uploads/2020/09/30/89a07e9b-00ab-4967-976a-c723b2aa8656.png)

```
Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3
Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.
```

### Example 2:
```
Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
Output: 4
Explanation: All points can be made visible in your field of view, including the one at your location.
```

### Example 3:
![ex2](https://assets.leetcode.com/uploads/2020/09/30/5010bfd3-86e6-465f-ac64-e9df941d2e49.png)

```
Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
Output: 1
Explanation: You can only see one of the two points, as shown above.
 ```

### Constraints:
```
1 <= points.length <= 105
points[i].length == 2
location.length == 2
0 <= angle < 360
0 <= posx, posy, xi, yi <= 100
```

Solution
========
Why Wraparound is Necessary
Without duplication, angles near 
360∘ (e.g., 350∘) and 0∘ (e.g., 10∘) would not be adjacent in the sorted list. Adding 
360∘ allows us to treat them as continuous, enabling the sliding window to work seamlessly.
  
```python
# T:O(nlogn)
# S: O(n)
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        itself = 0
        polar = list()
        for point in points:
            if point == location:
                itself += 1
                continue
            polar.append(math.atan2(point[1]-location[1], point[0]-location[0]))
        
        polar.sort()
        L = len(polar)
        pi_2 = math.pi * 2
        for i in range(L):
            polar.append(polar[i] + pi_2)
        
        angle *= math.pi / 180
        i = j = 0
        res = 0
        L = len(polar)
        while i < L:
            while j < L and polar[j] - polar[i] <= angle:
                res = max(res, j - i + 1)
                j += 1
            i += 1
        return res + itself
```
