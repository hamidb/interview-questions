"""Kruskal's Greedy Algorithm."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools

from adt.union_find import UnionFind
from adt.graph import Graph

def _edge_cmp_(e1, e2):
  assert isinstance(e1, Graph.Edge)
  assert isinstance(e2, Graph.Edge)
  return e1.w - e2.w

# returns MST cost if there's any.
def kruskal(edges):
  assert isinstance(edges, list(Graph.Edge))
  assert len(edges) >= 0

  if len(edges) == 0: return None
  cost = 0
  uf = UnionFind(len(edges))
  sorted_list = sorted(
    edges,
    key=functools.cmp_to_key(_edge_cmp_))
  for edge in sorted_list:
    if uf.is_connected(edge.origin, edge.to):
      continue
    uf.unify(edge.origin, edge.to)
    cost += edge.w
    if uf.component_size() == len(edges):
      break
  if uf.component_size() != len(edges):
    return None
  return cost

