Cheapest Flights Within K Stops (Leetcode #787)
===============================
### Medium

There are `n` cities connected by some number of flights. You are given an array flights where `flights[i] = [fromi, toi, pricei]` indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers `src`, `dst`, and `k`, return the cheapest price from src to dst with at most `k` stops. If there is no such route, return `-1`.

### Example 1:
```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
```

### Example 2:
```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
```

### Example 3:
```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
```

### Constraints:
```
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
```

Solution
========

```python
# This is a dijkstra with a modification to store current stops too
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:                
#         graph = defaultdict(list)
#         for u, v, price in flights:
#             graph[u].append((v, price))

#         # (cost, current node, stops remaining)
#         pq = [(0, src, k + 1)]

#         # Distance dictionary to track the cheapest price with a given number of stops
#         # The key is to store distances in a dict with key->(node, stops)
#         distances = defaultdict(lambda: float('inf'))
#         distances[(src, k + 1)] = 0

#         while pq:
#             cost, node, stops = heapq.heappop(pq)
#             if node == dst:
#                 return cost

#             # If we have stops left, explore the neighbors
#             if stops > 0:
#                 for neighbor, price in graph[node]:
#                     new_cost = cost + price
#                     # Only proceed if it's cheaper or we have more stops available
#                     if new_cost < distances[(neighbor, stops - 1)]:
#                         distances[(neighbor, stops - 1)] = new_cost
#                         heapq.heappush(pq, (new_cost, neighbor, stops - 1))
#         return -1
                
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:                    
        graph = defaultdict(list)
        for u, v, price in flights:
             graph[u].append((v, price))

        dists = [float('inf')] * n 
        pq = [(0,src,0)] # [stops, node, cost]
        
        while pq:
            steps, node, cost = heappop(pq)
            #we're only going to add more nodes to the queue if they've
            #taken less than k+1 steps, and their children are present
            #in the adjacency list
            if steps <= k:
                # go through the current nodes neighbours
                for nextNode, weight in graph[node]:
                    #the path to this node is less than the smallest we've
                    #every seen at nextNode then relax the edge
                    if weight + cost < dists[nextNode]:
                        dists[nextNode] = weight + cost
                        heappush(pq, (steps+1, nextNode, weight+cost))

        return dists[dst] if dists[dst] != float('inf') else -1
```
