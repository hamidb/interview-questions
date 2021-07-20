Basic Calculator (Leetcode #224)
===============================
### Hard

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

 

### Example 1:
```
Input: s = "1 + 1"
Output: 2
```

### Example 2:
```
Input: s = " 2-1 + 2 "
Output: 3
```

### Example 3:
```
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
``` 

### Constraints:
```
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation.
'-' could be used as a unary operation but it has to be followed by parentheses.
Every number and running calculation will fit in a signed 32-bit integer.
```

Solution
========

```python
# T: O(N)
# S: O(N)
# keep the sign and left side of the results in stack.
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        op = 0
        ans = 0
        for c in s:
            if c.isdigit():
                op = op * 10 + int(c)
            elif c in '+-':
                ans += sign * op
                sign = -1 if c == '-' else 1
                op = 0
            elif c == '(':
                stack.append(ans)  # save result so far. eg. ans-(...)
                stack.append(sign)  # save sign before opening brace.
                ans = 0  # reset
                sign = 1  # reset
            elif c == ')':
                ans += sign * op 
                # eg. ans-(op) stack=[ans, -1]
                ans *= stack.pop()  # -1*op
                ans += stack.pop()  # ans - op
                op = 0  # reset
        return ans + op * sign
                

# # TLE
# class Solution:
#     def calculate(self, s: str) -> int:
#         s = ''.join([c for c in s if c not in ' '])
#         def eval_(s):
#             if len(s) == 0:
#                 return 0
#             if len(s) == 1:
#                 return int(s)
#             ans = 0
#             i = 0
#             while i < len(s):
#                 c = s[i]
#                 if c in '+-':
#                     if s[i+1] == '(':
#                         j = self.findClosing(s, i+1)
#                         ans += eval_(s[i+2:j]) if c == '+' else -eval_(s[i+2:j])
#                         i = j + 1
#                     else:
#                         j = i + 1
#                         while j < len(s) and s[j] in '0123456789':
#                             j += 1
#                         ans += int(s[i+1:j]) if c == '+' else -int(s[i+1:j])
#                         i = j
#                 else:
#                     if c == '(': 
#                         j = self.findClosing(s, i)
#                         ans += eval_(s[i+1:j])
#                         i = j + 1
#                     else:
#                         j = i+1
#                         while j < len(s) and s[j] in '0123456789':
#                             j += 1
#                         ans += int(s[i:j])
#                         i = j
#             return ans
#         return eval_(s)

        
#     def findClosing(self, s, start):
#         stack = [s[start]]
#         i = start + 1
#         while i < len(s):
#             if s[i] == '(':
#                 stack.append('(')
#             elif s[i] == ')':
#                 stack.pop()
#             if len(stack) == 0:
#                 return i
#             i += 1
#         return i
            
```
