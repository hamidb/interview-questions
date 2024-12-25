Pow(x, n) (Leetcode #50)
===============================
### Medium

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

 

### Example 1:
```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

### Example 2:
```
Input: x = 2.10000, n = 3
Output: 9.26100
```

### Example 3:
```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 ```


### Constraints:
```
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= xn <= 10^4
```

### Solution
```python
# T: O(log n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if x == -1:
            return -1 if n%2 else 1
        
        x = x if n > 0 else 1/x
        ans = x
        n = abs(n)
        p = 1
        while p*p < n:
            p *= 2
            ans = ans*ans
            if ans < 1e-6:
                return 0

        for _ in range(p, n):
            ans = ans*x
        return ans

## recursive solution
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if abs(x) < 1e-9:
#             return 0            
#         if n == 0 or x == 1:
#             return 1
        
#         if n < 0:
#             return self.myPow(1/x, -n)
        
#         level = self.myPow(x, n//2)
#         if n % 2:
#             return level*level*x
#         else:
#             return level*level

```

C++
```c++
class Solution {
public:
    double myPow(double x, int n) {        
        if (abs(x) < 1e-9)
            return 0;
        if (n==0 || x==1)
            return 1.;

        if (n < 0) {
            if (n == INT_MIN)
                return myPow(1/x, -(n+1))/x;
            else
                return myPow(1/x, -n);
        }
        double level = myPow(x, floor(n/2));
        if (n % 2)
            return level*level*x;
        else
            return level*level;
    }
};
```
