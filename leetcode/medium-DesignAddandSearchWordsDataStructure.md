Design Add and Search Words Data Structure (Leetcode #221)
===============================
### Medium

Design a data structure that supports adding new words and finding if a string matches any previously added string.

### Implement the WordDictionary class:

`WordDictionary()` Initializes the object.

`void addWord(word)` Adds word to the data structure, it can be matched later.
`bool search(word)` Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots `'.'` where dots can be matched
with any letter.
 

### Example:
```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
``` 

### Constraints:
```
1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
```

Solution
========

```python
# T Search without dot: O(M)
# T Search with dot: O(N x 26^M) 
# S Search: O(1)

# T Add: O(M)
# S Add: O(M)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False;
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True

    def search(self, word: str) -> bool:
        return self.search_(word, 0, len(word)-1, self.root)
    
    def search_(self, word: str, start, end, root) -> bool:
        p = root
        for i in range(start, end+1):
            c = word[i]
            if c not in p.children:
                if c == '.':
                    for child in (p.children):
                        if self.search_(word, i+1, end, p.children[child]):
                            return True
                        
                # it was not '.' and not found. So return False.
                return False
            p = p.children[c]
        return p.isEnd


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
