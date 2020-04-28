Course Schedule (Leetcode #207)
===============================
### Medium
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

### Example 1:

Input: `numCourses = 2, prerequisites = [[1,0]]`
Output: `true`
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
### Example 2:

Input: `numCourses = 2, prerequisites = [[1,0],[0,1]]`
Output: `false`
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


### Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
`1 <= numCourses <= 10^5`

Solution
========

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build a graph (Adjacency list representation).
        graph = {start:[] for start, end in prerequisites}
        for start, end in prerequisites:
            graph[start].append(end)

        visiting = []
        visited = []
        for v, _ in graph.items():  # iterate over all edges of the graph.
            if self.dfs_has_cycle(graph, v, visiting, visited):
                return False
        return True

    def dfs_has_cycle(self, graph, v, visiting, visited):
        visiting.append(v)  # move current node to visiting
        for neighbor in (graph.get(v) or []):  # iterate over its neighbors if it exist.
            if neighbor in visited:
                continue
            if neighbor in visiting:
                return True
            if self.dfs_has_cycle(graph, neighbor, visiting, visited):
                return True
        visiting.remove(v)  # move from visiting to visited.
        visited.append(v)
        return False
```
