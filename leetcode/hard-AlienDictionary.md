Alien Dictionary(Leetcode #269)
===============================
### Hard

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules.
If there is no solution, return `""`. If there are multiple solutions, return any of them.

A string `s` is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language.
If the first `min(s.length, t.length)` letters are the same, then `s` is smaller if and only if `s.length < t.length`.


### Example 1:
```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

### Example 2:
```
Input: words = ["z","x"]
Output: "zx"
```

### Example 3:
```
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
``` 

### Constraints:
```
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
```
### Complexity

Total Time Complexity:

Combining graph construction and topological sorting:

O(N⋅L+C+E)

N⋅L: For comparing adjacent words to build edges.

C+E: For topological sorting.

In the worst case:

C≤26 (number of lowercase English letters).

E≤C^2 (a complete graph).

Thus, the complexity simplifies to:

O(N⋅L+C^2)
 
Solution
========
```python

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        in_degree = {c: 0 for w in words for c in w}
        W = len(words)
        for i in range(W):
            wi = words[i]
            for j in range(i+1, W):
                wj = words[j]
                p, q = 0, 0
                while p < len(wi) and q < len(wj):
                    if wi[p] != wj[q]:
                        if wj[q] not in graph[wi[p]]:
                            graph[wi[p]].add(wj[q])
                            in_degree[wj[q]] += 1
                        break
                    p += 1
                    q += 1
                else:
                    if len(wj) < len(wi):
                        return ""  # invalid (e.g. ['abc', 'ab'])
        
        q = deque([node for node in in_degree if in_degree[node] == 0])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for child in (graph[node] or {}):
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)
        
        if len(order) < len(in_degree):
            return ""  # cycle found
        
        return "".join(order)
```
