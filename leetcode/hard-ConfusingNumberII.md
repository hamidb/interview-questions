Confusing Number II (Leetcode #1088)
===============================
### Hard

We can rotate digits by 180 degrees to form new digits. When `0, 1, 6, 8, 9` are rotated `180` degrees, they become `0, 1, 9, 8, 6` respectively.
When `2, 3, 4, 5` and `7` are rotated `180` degrees, they become invalid.

A confusing number is a number that when rotated `180` degrees becomes a different number with each digit valid.
(Note that the rotated number can be greater than the original number.)

Given a positive integer `N`, return the number of confusing numbers between `1` and `N` inclusive.

 

### Example 1:
```
Input: 20
Output: 6
Explanation: 
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
```

### Example 2:
```
Input: 100
Output: 19
Explanation: 
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
 ```

### Note:
```
1 <= N <= 10^9
```

#### Hint 1:
Which set of digits have the valid numbers?

#### Hint 2:
Only `0, 1, 6, 8, 9` are the valid set of digits, do a backtracking to generate all the numbers containing this digits and check they are valid.

Solution
========
```python
class Solution:
    def confusingNumberII(self, N: int) -> int:
        valid = [0, 1, 6, 8, 9]
        generated = [1, 6, 8, 9]
        i_first = 0
        n = 0
        cnt = 2
        while n <= N and i_first < len(generated):
            first = generated[i_first]
            for second in valid:
                n = first*10 + second
                if n > N:
                    break
                generated.append(n)
                if self.check(n):
                    cnt += 1
            i_first += 1
        return cnt

    def check(self, n):
        # return false if rotated == n
        original = n
        rotated = 0
        while n > 0:
            d = n % 10
            d = 6 if d==9 else (9 if d==6 else d) # replace 6 with 9 and vice versa.
            n = n // 10
            rotated = rotated*10 + d

        return rotated != original
```
