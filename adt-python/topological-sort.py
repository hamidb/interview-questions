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

  dists = dag_shortest_path(graph, 0);
  # Find the shortest path from 0 to 4 which is 8.0
  assert dists[4] == 8.0
  # Find the shortest path from 0 to 6 which is None since 6 is not reachable.
  assert dists[6] is None
