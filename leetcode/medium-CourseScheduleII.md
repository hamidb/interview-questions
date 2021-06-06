Course Schedule II (Leetcode #210)
===============================
### Medium
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

### Example 1:
```
Input: 2, [[1,0]] 
Output: [0,1]
```
Explanation:
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is `[0,1]`.

### Example 2:
```
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
```
Explanation:
There are a total of 4 courses to take. To take course 3 you should have finished both     
courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is `[0,1,2,3]`. Another correct ordering is `[0,2,1,3]`.

### Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

Solution
========
using "In degree".

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        graph = {k: [] for k in range(numCourses)}
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        if self.isCyclic(graph):
            return []
        
        in_degree = numCourses * [0]
        for node in range(numCourses):
            for k in graph[node]:
                in_degree[k] += 1
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        order = []
        while q:
            node = q.popleft()
            order.insert(0, node)
            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)
        return order
    
    def isCyclic(self, graph):
        def dfs(graph, node, visiting, visited):
            visiting.add(node)
            for v in (graph.get(node) or []):
                if v in visiting:
                    return True
                if v in visited:
                    continue
                if dfs(graph, v, visiting, visited):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False
        visited = set()
        visiting = set()
        for node, _ in (graph.items() or {}):
            if dfs(graph, node, visiting, visited):
                return True
        return False
```
```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        
        graph = {i: [] for i in range(numCourses)}
        for node in prerequisites:
            graph[node[0]].append(node[1])
        if self.isCyclic(graph):
            return []
        return self.topSort(graph)

    def isCyclic(self, graph):
        visited = set()
        visiting = set()
        for at, _ in (graph.items() or {}):
            if self.dfsIsCyclic(graph, at, visiting, visited):
                return True 
        return False
        
    def dfsIsCyclic(self, graph, at, visiting, visited):
        visiting.add(at)
        for child in (graph.get(at) or []):
            if child in visited:
                continue
            if child in visiting:
                return True
            if self.dfsIsCyclic(graph, child, visiting, visited):
                return True
        visiting.remove(at)
        visited.add(at)
        return False
    
    def topSort(self, graph):
        N = len(graph)
        ordering = N * [None]
        visited = set()
        i = 0
        for at, _ in graph.items():
            if at not in visited:
                i = self.dfs(i, at, graph, visited, ordering)
        return ordering
    
    def dfs(self, i, at, graph, visited, ordering):
        visited.add(at)
        for child in (graph.get(at) or []):
            if child not in visited:
                i = self.dfs(i, child, graph, visited, ordering)
        ordering[i] = at
        return i+1
```
