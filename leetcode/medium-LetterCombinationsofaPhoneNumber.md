Letter Combinations of a Phone Number (Leetcode #17)
===============================
### Medium

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that `1` does not map to any letters.

![ex](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

### Example 1:
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Example 2:
```
Input: digits = ""
Output: []
```

### Example 3:
```
Input: digits = "2"
Output: ["a","b","c"]
``` 

### Constraints:
```
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
```

Solution
========

```python
# T: O(Nx4^N)   we have 4 letters for a key in worst case.
# S: O(N)  recursion depth
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        N = len(digits)
        ans = []
        alpha = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        def dfs(digits, prefix, ans):
            if len(digits) == 0:
                if len(prefix) > 0:
                    ans.append(prefix)
                return
            d = int(digits[0])
            for c in alpha[d-2]:
                dfs(digits[1:], prefix+c, ans)
        
        dfs(digits, '', ans)
        return ans    
```
