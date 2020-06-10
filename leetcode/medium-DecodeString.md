Decode String (Leetcode #394)
===============================
### Medium

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there won't be input like `3a` or `2[4]`.

### Example 1:
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```
### Example 2:
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```
### Example 3:
```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```
### Example 4:
```
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
```

Solution
========

```python
# T: O(n)
# S: O(kn)
class Solution:
    def decodeString(self, s: str) -> str:
        result = ''
        i = 0
        while i < len(s):
            c = s[i]
            if ord(c) >= 49 and ord(c) <= 57:
                # e.g. 32[a]
                # i -> points to the 1st digit. (i = 0)
                # d -> points to the first [. (d = 2)
                d = s.find('[', i)
                closing_brace = self.findMatchingBrace(s, d+1)
                new_s = s[d+1:closing_brace]                
                number = int(s[i:d])
                for j in range(number):
                    result += self.decodeString(new_s)
                i = closing_brace+1
            else:
                result += c
                i += 1
        return result

    def findMatchingBrace(self, s, start):
        stack = []
        for i in range(start, len(s)):
            if s[i] == ']':
                if len(stack) == 0:
                    return i
                stack.pop()
            elif s[i] == '[':
                stack.append('[')
``` 
