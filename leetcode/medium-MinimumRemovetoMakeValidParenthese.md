Minimum Remove to Make Valid Parenthese (Leetcode #1249)
===============================
### Medium

Given a string `s` of `'('` , `')'` and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting parentheses string is valid and return any
valid string.

Formally, a parentheses string is valid if and only if:

+ It is the empty string, contains only lowercase characters, or

+ It can be written as `AB` (`A` concatenated with `B`), where `A` and B are valid strings, or

+ It can be written as `(A)`, where A is a valid string.
 

### Example 1:
```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

### Example 2:
```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

### Example 3:
```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

### Example 4:
```
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
``` 

### Constraints:
```
1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
```

Solution
========

```python
# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         def delete_invalid_close(s, open, close):
#             balance = 0
#             text = ''
#             for c in s:
#                 if c == open:
#                     balance += 1
#                 if c == close:
#                     balance -= 1
#                 if balance >= 0:
#                     text += c
#                 else:
#                     balance += 1
#             return text
        
#         text = delete_invalid_close(s, '(', ')')
#         text = delete_invalid_close(text[::-1], ')', '(')  # same in reverse
                
#         return text[::-1]
        
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque([])
        remove = set()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')' and stack:
                stack.pop()
            elif s[i] == ')':
                remove.add(i)
        text = '' 
        un = remove.union(set(stack))
        for i in range(len(s)):
            if i not in un:
                text += s[i]
            
        return text
        
```
