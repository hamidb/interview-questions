"""Dijkstra shortest path."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import heapq

from adt.graph import Graph

# returns shortest distance from start node to end node.
# This only works for graphs with non negative edges.
def dijkstra(graph, start, end):
  """
    graph: adt.graph.Graph
    start: int
    end: int

    returns (distance, prev) in which prev is an array to parent nodes.
  """
  assert isinstance(graph, Graph)
  assert graph.size > 0
  assert start < graph.size and end < graph.size

  N = graph.size
  visited = N*[0]
  prev = N*[None]
  dist = N*[float('inf')]
  dist[start] = 0
  pq = []

  if start == end:
    return 0, prev

  heapq.heappush(pq, (0, start))
  while pq:
    curr_dist, node = heapq.heappop(pq)
    visited[node] = 1
    if dist[node] < curr_dist:
      continue
    for edge in graph.get_edges(node):
      if visited[edge.to]:
        continue
      new_dist = dist[edge.origin] + edge.w
      if new_dist < dist[edge.to]:
        dist[edge.to] = new_dist
        prev[edge.to] = edge.origin
        heapq.heappush(pq, (dist[edge.to], edge.to))
    if end == node:
      return dist[end], prev
  return -1, []  # not reachable

def reconstruct_shortest_path(graph, start, end):
  assert isinstance(graph, Graph)
  assert start < graph.size and end < graph.size
  assert start >= 0 and end >= 0
  assert start <= end

  path = []
  dist, prev = dijkstra(graph, start, end)
  if dist == -1:
    return path
  at = end
  while at != None:
    path.insert(0, at)
    at = prev[at]
  return path

