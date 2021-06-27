Divide Two Integers (Leetcode #29)
===============================
### Medium
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, `truncate(8.345) = 8` and `truncate(-2.7335) = -2`.

Note: Assume we are dealing with an environment that could only store integers within the `32`-bit signed integer range: `[−2^31, 2^31 − 1]`.
For this problem, assume that your function returns `2^31 − 1` when the division result overflows.

 
 
### Example 1:
```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
```

### Example 2:
```
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
```

### Example 3:
```
Input: dividend = 0, divisor = 1
Output: 0
```

### Example 4:
```
Input: dividend = 1, divisor = 1
Output: 1
 ```

### Constraints:
```
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
```

Solution
========
```python
# # O(N): TLE
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         if dividend == -2147483648 and divisor == -1:
#             return 2147483647
#         neg = 0
#         if dividend > 0:
#             neg += 1
#             dividend = -dividend
#         if divisor > 0:
#             neg += 1
#             divisor = -divisor
        
#         # we work with negative numbers to avoid dividend-divisor exceeds min_int.
#         ans = 0
#         while dividend-divisor <= 0:
#             dividend -= divisor
#             ans += 1
#         return ans if neg != 1 else -ans

# O((logN)^2)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        neg = 0
        if dividend > 0:
            neg += 1
            dividend = -dividend
        if divisor > 0:
            neg += 1
            divisor = -divisor

        HALF_MIN_INT = -1073741824  # MIN_INT // 2
        ans = 0
        # we work with negative numbers to avoid dividend-divisor exceeds min_int.
        while dividend-divisor <= 0:
            pow2 = -1  # normal 1, 1+1, 2+2, ... (-1, -2, -4)
            val = divisor
            while val >= HALF_MIN_INT and dividend <= (val+val):  # dividend - (val+val) <= 0
                val <<= 1
                pow2 <<= 1
            ans += pow2
            dividend -= val

        return -ans if neg != 1 else ans

# # T: O(logN)
# # S: O(logN)  with memo
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         # Constants.
#         MAX_INT = 2147483647        # 2**31 - 1
#         MIN_INT = -2147483648       # -2**31
#         HALF_MIN_INT = -1073741824  # MIN_INT // 2

#         # Special case: overflow.
#         if dividend == MIN_INT and divisor == -1:
#             return MAX_INT

#         # We need to convert both numbers to negatives.
#         # Also, we count the number of negatives signs.
#         negatives = 2
#         if dividend > 0:
#             negatives -= 1
#             dividend = -dividend
#         if divisor > 0:
#             negatives -= 1
#             divisor = -divisor

#         doubles = []
#         powersOfTwo = []

#         # Nothing too exciting here, we're just making a list of doubles of 1 and
#         # the divisor. This is pretty much the same as Approach 2, except we're
#         # actually storing the values this time. */
#         powerOfTwo = 1
#         while divisor >= dividend:
#             doubles.append(divisor)
#             powersOfTwo.append(powerOfTwo)
#             # Prevent needless overflows from occurring...
#             if divisor < HALF_MIN_INT:
#                 break
#             divisor += divisor # Double divisor
#             powerOfTwo += powerOfTwo

#         # Go from largest double to smallest, checking if the current double fits.
#         # into the remainder of the dividend.
#         quotient = 0
#         for i in reversed(range(len(doubles))):
#             if doubles[i] >= dividend:
#                 # If it does fit, add the current powerOfTwo to the quotient.
#                 quotient += powersOfTwo[i]
#                 # Update dividend to take into account the bit we've now removed.
#                 dividend -= doubles[i]

#         # If there was originally one negative sign, then
#         # the quotient remains negative. Otherwise, switch
#         # it to positive.
#         return quotient if negatives != 1 else -quotient
```
