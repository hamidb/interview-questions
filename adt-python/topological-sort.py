"""Topological sort for a DAG"""

class Edge:

  def __init__(self, origin, to, w):
    self._from = origin
    self._to = to
    self._w = w

def dfs_topsort(at, i, graph, visited, ordering):
  visited.add(at)
  for child in (graph.get(at) or []):
    if child._to not in visited:
      i = dfs_topsort(child._to, i, graph, visited, ordering)
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

if __name__ == '__main__':
  # Graph setup
  graph = {i: [] for i in range(7)}
  graph.get(0).append(Edge(0, 1, 3));
  graph.get(0).append(Edge(0, 2, 2));
  graph.get(0).append(Edge(0, 5, 3));
  graph.get(1).append(Edge(1, 3, 1));
  graph.get(1).append(Edge(1, 2, 6));
  graph.get(2).append(Edge(2, 3, 1));
  graph.get(2).append(Edge(2, 4, 10));
  graph.get(3).append(Edge(3, 4, 5));
  graph.get(5).append(Edge(5, 4, 7));

  assert topological_sort(graph) == [6, 0, 5, 1, 2, 3, 4]
