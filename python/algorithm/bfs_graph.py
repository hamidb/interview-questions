"""Graph bfs"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from collections import deque

from adt.graph import Graph

def bfs_iterative(graph, start):
  assert isinstance(graph, Graph)
  assert graph.size > 0

  visited = graph.size*[0]
  prev = graph.size*[None]
  q = deque()
  visited[start] = 1
  q.append(start)
  while q:
    node = q.popleft()
    for edge in (graph.get_edges(node) or []):
      if visited[edge.to]:
        continue
      visited[edge.to] = 1
      q.append(edge.to)
      prev[edge.to] = node
  return prev

def bfs_path(graph, start, end):
  prev = bfs_iterative(graph, start)
  path = []
  at = end
  while at is not None:  # at can be 0
    path.insert(0, at)
    at = prev[at]
  if path[0] == start:
    return path
  return []
