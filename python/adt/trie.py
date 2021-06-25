class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Search:
        
    def __init__(self, sentences: List[str]):
        self.root = TrieNode()
        for sentence in sentences:
            self.add(sentence)
    
    def add(self, sentence):
        if sentence is None:
            return
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True
        
    def search(self, word):
        if word == '':
            return []
        p = self.root
        prefix = ''
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
            prefix += c
        return p.isEnd
