Remove Invalid Parentheses (Leetcode #301)
===============================
### Hard

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

### Example 1:
```
Input: s = "()())()"
Output: ["(())()","()()()"]
```

### Example 2:
```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
```

### Example 3:
```
Input: s = ")("
Output: [""]
``` 

### Constraints:
```
1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
```

Solution
========

```python
# T: O(2^N)
# S: O(N) depth of recursion.
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        N = len(s)
        rm_left, rm_right = 0, 0
        for c in s:
            if c == '(':
                rm_left += 1
            elif c == ')':
                if rm_left > 0:
                    rm_left -= 1
                else:
                    rm_right += 1
        
        ans = set()
        def recurse(idx, left, right, rm_left, rm_right, result):
            if idx == len(s):
                if rm_left == 0 and rm_right == 0:
                    ans.add(result)
                return
                
            curr = s[idx]
            if curr == '(':
                # case1: discard curr only if we have remaining left braces to remove.
                if rm_left > 0:
                    recurse(idx+1, left, right, rm_left-1, rm_right, result)
                # case2: keep it
                recurse(idx+1, left+1, right, rm_left, rm_right, result+curr)
            elif curr == ')':
                # case1: discard curr if we have remaining right brace to remove.
                if rm_right > 0:
                    recurse(idx+1, left, right, rm_left, rm_right-1, result)
                # case2: keep it if it's valid to keep. valid means that there're more '(' in the result than ')'
                if left > right:  # keep it
                    recurse(idx+1, left, right+1, rm_left, rm_right, result+curr)
            else:
                # keep if alphabet
                recurse(idx+1, left, right, rm_left, rm_right, result+curr)
                         
        recurse(0, 0, 0, rm_left, rm_right, '')
        return ans

# # T: O(2^N)
# # S: O(N) depth of recursion.
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         def mincost(s):
#             if len(s) == 0:
#                 return 0
#             stack=["."]
#             for c in s:
#                 if c == "(":
#                     stack.append(c)
#                 elif c == ")":
#                     if stack[-1] == "(":
#                         stack.pop()
#                     else:
#                         stack.append(c)
#             return len(stack) - 1
        
#         #initialization 
#         q = deque([(s, mincost(s))])
#         ans = []
#         v = set()
#         while q:
#             string, cost = q.popleft()
#             if string in v:
#                 continue 
#             v.add(string)  # visit
#             if cost == 0:
#                 ans.append(string)  # we found the string
#             # finding all possible paths 
#             for i in range(len(string)):
#                 if string[i] not in "()":
#                     continue  # alphabet 
#                 curr = string[:i] + string[i+1:]
#                 k = mincost(curr)  # finding mincost to transform 
#                 if k <= cost:  # only if better potential solution
#                     q.append((curr, k)) 
#         return ans
```
