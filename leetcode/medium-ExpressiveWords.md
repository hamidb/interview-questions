Expressive Words (Leetcode #809)
===============================
### Medium

Sometimes people repeat letters to represent extra feeling, such as `"hello" -> "heeellooo", "hi" -> "hiiii"`.
In these strings like `"heeellooo"`, we have groups of adjacent letters that are all the same:  `"h", "eee", "ll", "ooo"`.

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation:
choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is `3` or more.

For example, starting with `"hello"`, we could do an extension on the group `"o"` to get `"hellooo"`, but we cannot get `"helloo"`
since the group `"oo"` has size less than `3`.  Also, we could do another extension like `"ll" -> "lllll"` to get `"helllllooo"`.  If `S = "helllllooo"`,
then the query word `"hello"` would be stretchy because of these two extension operations: `query = "hello" -> "hellooo" -> "helllllooo" = S`.

Given a list of query words, return the number of words that are stretchy. 

 

### Example:
```
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
``` 

### Constraints:
```
0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
```

Solution
========

```python
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        table = defaultdict(list)
        for word in words:
            w, code = self.encode(word)
            table[w].append(code)
        s, c = self.encode(S)
        cnt = 0
        for code in (table.get(s) or []):
            if self.isStretchOf(c, code):
                cnt += 1
        return cnt
    
    def isStretchOf(self, c, code):
        stretchOf = False
        for i in range(len(code)):
            if code[i] == c[i]:
                continue
            if c[i] > code[i] and c[i] >= 3:
                stretchOf = True
            else:
                return False
        return stretchOf
    
    def encode(self, word):
        if word == '':
            return '', []
        return zip(*[(k, len(list(grp)))
                     for k, grp in itertools.groupby(word)])
```
