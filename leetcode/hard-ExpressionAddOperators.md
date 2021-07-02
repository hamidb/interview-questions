Expression Add Operators (Leetcode #282)
===============================
### Hard

Given a string `num` that contains only digits and an integer `target`, return all possibilities to add the binary operators `'+', '-'`, or `'*'` between the digits of
`num` so that the resultant expression evaluates to the target value.

 

### Example 1:
```
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
```

### Example 2:
```
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
```

### Example 3:
```
Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
```

### Example 4:
```
Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
```

### Example 5:
```
Input: num = "3456237490", target = 9191
Output: []
 ```

### Constraints:
```
1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1
```

Solution
========

```python
# T: O(N x 3^N) = O(3^N)
# S: O(N) depth of recursion
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        exprs = []
        
        def recurse(idx, value, delta, exp):
            # base case here
            if idx == len(num):
                if value == target:
                    exprs.append(exp)
                    return
            
            # the loop will create the current operand and recursively call
            # the next set of actions to be executed
            for i in range(idx, len(num)):
                # this is to avoid cases where the operand starts with a 0
                # we need to have a case with just the 0 but not something like
                # 05, so the condition will return early if we find such cases
                if num[idx] == '0' and i > idx:
                    return
                
                curr = int(num[idx:i+1])
                curr_str = num[idx:i+1]
                
                # when we start the problem we dont have a preceding operator or operand
                if idx == 0:
                    recurse(i+1, curr, curr, exp + curr_str)
                else:
                    # We need to do 3 different recursions for each operator
                    # value stores the running value of the expression evaluated so far
                    # the crux of the logic lies in how we use and pass delta
                    # when the operation is '+' or '-' we don't care much about it and can just
                    # add or subtract it from the value 
                    # when '*' is involved, we need to follow the precedence relation,
                    # but we have already evaluated the previous operator. We know the
                    # previous operation that was performed and how much it contributed to the value i.e., delta
                    # so, we can revert that operation by subtracting delta from value and reapplying the multiplication
                    recurse(i+1, value+curr, curr, exp + '+' + curr_str)
                    recurse(i+1, value-curr, -curr, exp + '-' + curr_str)
                    recurse(i+1, (value-delta)+curr*delta, curr*delta, exp + '*' + curr_str)
                            
        recurse(0, 0, 0, '')
        return exprs
                      
```
