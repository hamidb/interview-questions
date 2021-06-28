Trie Pattern matching with Wildcard * and ? (Facebook)
===============================
### Facebook

Implement trie match for a whole word, and also support if the whole word contains:
* `?` (match any one character) or
* `*` (any zero or more characters).

### Example 1:
```
    root = Matching()
    root.insert('abc')
    root.insert('acd')
    root.insert('bcd')
    print(root.search('acd')) # True
    print(root.search('acdd')) # False
    print(root.search('aaa')) # False
    print(root.search('a?d')) # True
    print(root.search('a*d')) # True
    print(root.search('ad*')) # False
    print(root.search('*c*')) # True
    print(root.search('*c?')) # True
    print(root.search('*a?')) # False
```

Solution
========

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Matching:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, source):
        if not source:
            return
        node = self.root
        for s in source:
            if s not in node.children:
                node.children[s] = TrieNode()
            node = node.children[s]
        node.isEnd = True

    def search(self, source):
        return self._search(self.root, source)
    
    def _search(self, root, source):
        p = root
        for i, c in enumerate(source):
            if c not in p.children:
                if c == '?':
                    for child in p.children:
                        if self._search(p.children[child], source[i+1:]):
                            return True
                elif c == '*':
                    for child in p.children:
                        node = p.children[child]
                        if self._search(node, source[i+1:]) or self._search(node, source):
                            return True
                # Either not '?' and c not in p.children or
                # it was '?' but the rest did not match or
                # it was '*' but the rest did not match.
                return False
            p = p.children[c]
        return p.isEnd
    
```
