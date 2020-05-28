"""Cycle in Undirected Graphs."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt.graph import Graph

def dfs(graph, i, visited, parent):
  visited[i] = 1  # mark it.
  for edge in (graph.get_edges(i) or []):
    if not visited[edge]:  # recurse if not visited.
      if dfs(graph, edge.to, visited, i):
        return True
    # cyclic if visited and not parent.
    elif edge != parent:
      return True
  return False

def is_cyclic(graph):
  assert isinstance(graph, Graph)
  assert graph.size > 0

  visited = graph.size*[0]
  # iterate over all nodes.
  for node in graph.get_nodes():
    if visited[node]:  # skip if already visited.
      continue
    if dfs(graph, node, visited, None):
      return True
  return False
