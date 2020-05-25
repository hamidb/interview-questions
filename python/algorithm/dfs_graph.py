"""Graph dfs"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt.graph import Graph

def dfs_recursive(graph):
  assert isinstance(graph, Graph)
  assert graph.size > 0

  def dfs(graph, i, visited):
    if visited[i]:
      return 0
    visited[i] = 1
    count = 1
    for edge in (graph.get_edges(i) or []):
      count += dfs(graph, edge.to, visited)
    return count

  visited = graph.size*[0]
  return dfs(graph, 0, visited)

def dfs_iterative(graph):
  assert isinstance(graph, Graph)
  assert graph.size > 0

  visited = graph.size*[0]
  visited[0] = 1
  stack = [0]
  count = 0

  while stack:
    node = stack.pop(len(stack)-1)
    count += 1
    for edge in (graph.get_edges(node) or []):
      if visited[edge.to]:
        continue
      visited[edge.to] = 1
      stack.append(edge.to)
  return count
