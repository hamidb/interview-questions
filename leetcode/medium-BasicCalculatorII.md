Basic Calculator II (Leetcode #227)
===============================
### Medium

Given a string `s` which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

 

### Example 1:
```
Input: s = "3+2*2"
Output: 7
```

### Example 2:
```
Input: s = " 3/2 "
Output: 1
```

### Example 3:
```
Input: s = " 3+5 / 2 "
Output: 5
 ```

### Constraints:
```
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
```

Solution
========

```python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        last_op = '+'
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in '+-*/' or i == len(s)-1:  # or end of the loop
                if last_op == '+':
                    stack.append(num)    
                elif last_op == '-':
                    stack.append(-num)
                elif last_op == '*':
                    num = num * stack.pop()
                    stack.append(num)
                elif last_op == '/':
                    if stack[-1] >= 0:
                        num = stack.pop() // num
                    else:
                        num = -(-stack.pop() // num)
                    stack.append(num)
                last_op = c
                num = 0
        return sum(stack)
                
```
