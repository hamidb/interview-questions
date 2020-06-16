Reverse Words in a String (Leetcode #151)
===============================
### Medium
Given an input string, reverse the string word by word.

### Example 1:
```
Input: "the sky is blue"
Output: "blue is sky the"
```
### Example 2:
```
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```
### Example 3:
```
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

### Note:

A word is defined as a sequence of non-space characters.

Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.

You need to reduce multiple spaces between two words to a single space in the reversed string.
 

### Follow up:
For C programmers, try to solve it in-place in O(1) extra space.

Solution
========

```python
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         if s == '': return ''
#         tmp = s.split(' ')
#         tmp = tmp[::-1]
#         if len(tmp) == 1:
#             return tmp[0]
#         res = ''
#         for i in tmp[:-1]:
#             res += (i + ' ') if i else ''
#         if tmp[-1]:
#             return res + tmp[-1]
#         return res[:-1]
    
class Solution:
    def reverseWords(self, s: str) -> str:
        if s == '': return ''
        tmp = s.split()
        return ' '.join(tmp[::-1])
        

```
