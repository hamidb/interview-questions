The Most Similar Path in a Graph (Leetcode #1548)
===============================
### Hard

We have `n` cities and `m` bi-directional roads where `roads[i] = [ai, bi]` connects city `ai` with city `bi`. Each city has a name consisting of exactly `3`
upper-case English letters given in the string array `names`. Starting at any city `x`, you can reach any city `y` where `y != x` (i.e. the cities and the
roads are forming an undirected connected graph).

You will be given a string array `targetPath`. You should find a path in the graph of the same length and with the minimum edit distance to `targetPath`.

You need to return the order of the nodes in the path with the minimum edit distance, The path should be of the same length of `targetPath` and should be valid 
(i.e. there should be a direct road between `ans[i]` and `ans[i + 1]`). If there are multiple answers return any one of them.

The edit distance is defined as follows:

![img1](https://assets.leetcode.com/uploads/2020/08/08/edit.jpg)


Follow-up: If each node can be visited only once in the path, What should you change in your solution?

 

### Example 1:
![img2](https://assets.leetcode.com/uploads/2020/08/08/e1.jpg)
```
Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"],
targetPath = ["ATL","DXB","HND","LAX"]
Output: [0,2,4,2]
Explanation: [0,2,4,2], [0,3,0,2] and [0,3,1,2] are accepted answers.
[0,2,4,2] is equivalent to ["ATL","LAX","HND","LAX"] which has edit distance = 1 with targetPath.
[0,3,0,2] is equivalent to ["ATL","DXB","ATL","LAX"] which has edit distance = 1 with targetPath.
[0,3,1,2] is equivalent to ["ATL","DXB","PEK","LAX"] which has edit distance = 1 with targetPath.
```

### Example 2:
![img2](https://assets.leetcode.com/uploads/2020/08/08/e2.jpg)
```
Input: n = 4, roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], names = ["ATL","PEK","LAX","DXB"],
targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]
Output: [0,1,0,1,0,1,0,1]
Explanation: Any path in this graph has edit distance = 8 with targetPath.
```

### Example 3:
![img2](https://assets.leetcode.com/uploads/2020/08/09/e3.jpg)
```
Input: n = 6, roads = [[0,1],[1,2],[2,3],[3,4],[4,5]], names = ["ATL","PEK","LAX","ATL","DXB","HND"],
targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
Output: [3,4,5,4,3,2,1]
Explanation: [3,4,5,4,3,2,1] is the only path with edit distance = 0 with targetPath.
It's equivalent to ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
``` 

### Constraints:
```
2 <= n <= 100
m == roads.length
n - 1 <= m <= (n * (n - 1) / 2)
0 <= ai, bi <= n - 1
ai != bi 
The graph is guaranteed to be connected and each pair of nodes may have at most one direct road.
names.length == n
names[i].length == 3
names[i] consists of upper-case English letters.
There can be two cities with the same name.
1 <= targetPath.length <= 100
targetPath[i].length == 3
targetPath[i] consists of upper-case English letters.
```

Solution
========

```python
# T: O(E x M)
# M -> path length
# E -> Edges = N^2 in worst case.
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:        
        graph = defaultdict(set)
        for x, y in roads:
            graph[x].add(y)
            graph[y].add(x) 

        # We start from the city of newhere (-1) and visit all starting cities.
        graph[-1] = set(range(len(names)))
        prev_city = [len(targetPath)*[-1] for _ in names] 
        
        # start from city=-1 and path_id=-1
        q = deque([(-1, -1)])
        best_d = float('inf')
        while q:
            city, path_id = q.popleft()
            if path_id == len(targetPath) - 1:
                return self.reconstruct(city, prev_city)
            for neighbor in graph[city]:
                new_path_id= path_id + 1
                # if we have already visited "neighbor" in the same path location.
                if prev_city[neighbor][new_path_id] != -1:
                    continue
                prev_city[neighbor][new_path_id] = city
                if names[neighbor] != targetPath[new_path_id]:
                    q.append([neighbor, new_path_id])
                else:  # we give d=0 higher priority by appending left.
                    q.appendleft([neighbor, new_path_id])
        return []

    def reconstruct(self, start, prev_city):
        m = len(prev_city[0])
        path = m * [-1]
        for prev_id in range(m-1, -1, -1):
            path[prev_id] = start
            start = prev_city[start][prev_id]
        return path
    
# class Solution:
#     def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
#         graph = defaultdict(set)
#         for x, y in roads:
#             graph[x].add(y)
#             graph[y].add(x)    
#         # We start from the city of newhere (-1) and visit all starting cities.
#         graph[-1] = set(range(len(names)))
        
#         @lru_cache(maxsize=None)
#         def dfs(city, curr_i):
#             if curr_i == len(targetPath):
#                 return 0, []
#             min_d = float('inf')
#             best_path = []
#             for neighbor in graph[city]:
#                 d, path = dfs(neighbor, curr_i+1)
#                 d += (names[neighbor] != targetPath[curr_i])
#                 if d < min_d:
#                     min_d = d
#                     best_path = [neighbor] + path
#             return min_d, best_path
#         return dfs(-1, 0)[1]
```
