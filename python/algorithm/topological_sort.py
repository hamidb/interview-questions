"""Topological sort for a DAG"""

class Edge:

  def __init__(self, origin, to, w):
    self.from_ = origin
    self.to = to
    self.w = w

def dfs_topsort(at, i, graph, visited, ordering):
  visited.add(at)
  for child in (graph.get(at) or []):
    if child.to not in visited:
      i = dfs_topsort(child.to, i, graph, visited, ordering)
  ordering[i] = at
  return i-1

def topological_sort(graph):  # graph: Dict[int, List[Edge]]
  N = len(graph)  # number of nodes
  visited = set()
  ordering = N * [None]
  i = N-1
  for at, _ in graph.items():
    if at not in visited:
      i = dfs_topsort(at, i, graph, visited, ordering)
  return ordering

# returns shortest path distance from start node to other nodes.
# This only works for DAG.
def dag_shortest_path(graph, start):
  if len(graph) == 0:
    return []
  assert start in graph

  top_sort = topological_sort(graph)
  dist = len(graph) * [None]
  dist[start] = 0  # distance from itself
  for i in range(len(graph)):
    node = top_sort[i]
    if dist[node] is None: continue  # start form 'start' node.
    for edge in (graph.get(node) or []):
      new_dist = dist[node] + edge.w
      if dist[edge.to] is None:
        dist[edge.to] = new_dist
      else:
        dist[edge.to] = min(new_dist, dist[edge.to])
  return dist

