Swap For Longest Repeated Character Substring (Leetcode #1156)
===============================
### Medium

Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

### Example 1:
```
Input: text = "ababa"
Output: 3
```
#### Explanation:
We can swap the first `b` with the last `a`, or the last `b` with the first `a`. Then, the longest repeated character substring is `aaa`, which its length is `3`.
### Example 2:
```
Input: text = "aaabaaa"
Output: 6
```
#### Explanation:
Swap `b` with the last `a` (or the first `a`), and we get longest repeated character substring `aaaaaa`, which its length is `6`.
### Example 3:
```
Input: text = "aaabbaaa"
Output: 4
```
### Example 4:
```
Input: text = "aaaaa"
Output: 5
```
#### Explanation:
No need to swap, longest repeated character substring is `aaaaa`, length is `5`.
### Example 5:
```
Input: text = "abcdef"
Output: 1
```
 

### Constraints:
```
1 <= text.length <= 20000
text consist of lowercase English characters only.
```
Solution
========

```python
# T: O(n)
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        chars, count, table = self.encode(text)
        max_value = 0
        for i in range(len(chars)):
            # why min?
            # if table[c] < count+1, it means there's no more c in text
            # so we can swap with the middle character.
            max_value = max(max_value, min(count[i]+1, table[chars[i]]))
        
        for i in range(1, len(chars)-1):
            if count[i] == 1 and chars[i-1] == chars[i+1]:
                cnt = count[i-1] + count[i+1] + 1
                max_value = max(max_value, min(cnt, table[chars[i+1]]))
        return max_value
    
    def encode(self, text: str):
        i, count, chars, table = 0, [], [], {}
        while i < len(text):
            c = text[i]
            cnt = 0
            while i < len(text) and text[i] == c:
                i += 1
                cnt += 1
            count.append(cnt)
            chars.append(c)
            table[c] = table.get(c, 0) + cnt
        return chars, count, table
```
