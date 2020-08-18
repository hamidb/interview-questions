Sequence Reconstruction (Leetcode #444)
===============================
### Medium

Check whether the original sequence `org` can be uniquely reconstructed from the sequences in `seqs`.
The `org` sequence is a permutation of the integers from `1 to n`, with `1 ≤ n ≤ 10^4`.
Reconstruction means building a shortest common supersequence of the sequences in `seqs` (i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
Determine whether there is only one sequence that can be reconstructed from `seqs` and it is the `org` sequence.

 

### Example 1:
```
Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
```

### Example 2:
```
Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation: The reconstructed sequence can only be [1,2].
```

### Example 3:
```
Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
```

### Example 4:
```
Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output: true
``` 

### Constraints:
```
1 <= n <= 10^4
org is a permutation of {1,2,...,n}.
1 <= segs[i].length <= 10^5
seqs[i][j] fits in a 32-bit signed integer.
```

Solution
========
### Thought process
* First, construct the dependency graph using `seqs`.
* try topological sorting on the dependency graph.
  * during each step, check whether there is only one option to select the node. if there is more than one options, return `False` directly.
* after getting the topological sorted node list, check whether its length is the same with number of distinct values and whether it's the same with `org`.

```python
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        values = set([x for seq in seqs for x in seq])
        # build adjacency list
        graph = collections.defaultdict(list)
        indegree = {x:0 for x in values}
        for seq in seqs:
            for i in range(1, len(seq)):
                src, desc = seq[i-1], seq[i]
                graph[src].append(desc)
                indegree[desc] += 1

        # create queue with indegree == 0
        q = deque()
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
                
        top_sort = []
        while q:
            if len(q) != 1:  # if we have more than one choice.
                return False
            node = q.popleft()
            top_sort.append(node)
            for c in graph[node]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        
        return len(top_sort) == len(values) and org == top_sort
```
