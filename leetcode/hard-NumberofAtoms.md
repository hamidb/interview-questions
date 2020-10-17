Number of Atoms (Leetcode #726)
===============================
### Hard

Given a chemical formula (given as a string), return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than `1`. If the count is `1`, no digits will follow. For example,
`H2O` and `H2O2` are possible, but `H1O2` is impossible.

Two formulas concatenated together to produce another formula. For example, `H2O2He3Mg4` is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, `(H2O2)` and `(H2O2)3` are formulas.

Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count
(if that count is more than `1`), followed by the second name (in sorted order), followed by its count (if that count is more than `1`), and so on.

### Example 1:
```
Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
```

### Example 2:
```
Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
```

### Example 3:
```
Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
```

### Example 4:
```
Input: formula = "Be32"
Output: "Be32"
```

### Constraints:
```
1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.
```

Solution
========

```python

# T: O(N^2)
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        ans = ''
        table = self.helper(formula)
        for k in sorted(table):
            ans += k + str(table[k]) if table[k] != 1 else k
        return ans

    def helper(self, formula: str) -> str:
        table = defaultdict(int)
        n, i = len(formula), 0
        while i < n:
            c = formula[i]
            cnt = 0
            if c.isupper():  # if it's start of a new Atom
                atom = c
                j = i+1
                while j < n and formula[j].islower():  # find lower c if any
                    atom += formula[j]
                    j += 1
                start_digit = j
                while j < n and formula[j].isdigit():  # find the following number
                    j += 1
                table[atom] += int(formula[start_digit:j] or 1)
            elif c == '(':  # if it's starting parenthesis
                j = self.matching_parenthesis(formula, i) + 1
                atoms = self.helper(formula[i+1:j-1])
                start_digit = j
                while j < n and formula[j].isdigit():  # find the following number
                    j += 1
                cnt = int(formula[start_digit:j] or 1)
                for k, v in atoms.items():
                    table[k] += v * cnt
            i = j
        return table
        
    def matching_parenthesis(self, formula, start):
        stack = deque(['('])
        i = start + 1
        while i < len(formula) and stack:
            if formula[i] == '(':
                stack.append(formula[i])
            elif formula[i] == ')':
                stack.pop()
            i += 1
        return i-1
        

```
