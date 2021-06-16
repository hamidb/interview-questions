Validate Stack Sequences (Leetcode #946)
===============================
### Medium

Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

### Example 1:

```
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

### Example 2:

```
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
```

### Note:

```
0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
```

Solution
========

```python
# Greedy 
# T: O(N) 
# S: O(N)
# N: length of popped and pushed.

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(popped) == 0:
            return True
        if len(popped) > len(pushed):
            return False
        
        pop_i = 0
        stack = []
        for p in pushed:
            stack.append(p)
            while stack and pop_i < len(popped) and popped[pop_i] == stack[-1]:
                stack.pop()
                pop_i += 1        
        return pop_i == len(popped)


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_size = len(popped)
        push_size = len(pushed)
        if pop_size == 0:
            return True
        if pop_size > push_size:
            return False
        
        stack = []
        while popped:
            pop = popped.pop(0)
            not_at_top = self.peek_stack(stack) != pop
            while not_at_top and pushed:
                stack.append(pushed.pop(0))
                not_at_top = self.peek_stack(stack) != pop
            if not_at_top:
                return False
            stack.pop()
        return True
    
    def peek_stack(self, stack):
        if stack:
            return stack[-1]
        return None
```
