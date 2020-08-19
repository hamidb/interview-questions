 24 Game (Leetcode #679)
===============================
### Hard
You have `4` cards each containing a number from `1 to 9`. You need to judge whether they could operated through `*, /, +, -, (, )` to get the value of `24`.

### Example 1:
```
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
```

### Example 2:
```
Input: [1, 2, 1, 2]
Output: False
```

### Note:

The division operator `/` represents real division, not integer division. For example, `4 / (1 - 2/3) = 12`.

Every operation done is between two numbers. In particular, we cannot use `-` as a unary operator. For example, with `[1, 1, 1, 1]` as input,
the expression `-1 - 1 - 1 - 1` is not allowed.

You cannot concatenate numbers together. For example, if the input is `[1, 2, 1, 2]`, we cannot write this as `12 + 12`.


Solution
========
Say we have numbers `a, b, c, d`. We choose two of them (with order) in `12` ways and perform one of `4` operations.
This is where `12 * 4` comes from. Then, with `3` remaining numbers, we choose `2` of them and perform one of `4` operations.
This is where `6 * 4` comes from.
Finally we have two numbers left and make a final choice of `2 * 4` possibilities.

```python
# O(1)
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return (abs(nums[0]-24.0) < 1e-6)
        
        for i in range(n):
            for j in range(i+1, n):
                remaining = []
                for k in range(n):
                    if k not in [i, j]:
                        remaining.append(nums[k])
                for r in self.calc_six_results(nums[i], nums[j]):
                    remaining.append(r)
                    if self.judgePoint24(remaining):
                        return True
                    remaining.pop()
        return False
    
    def calc_six_results(self, a, b):
        results = [a-b, b-a, a+b, a*b]
        if abs(a) > 1e-6: results.append(b/a)
        if abs(b) > 1e-6: results.append(a/b)
        return results

```
