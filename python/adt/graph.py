"""A Graph Class"""

class Graph:

  class Edge:
    def __init__(self, origin, to, w):
      self.origin = origin
      self.to = to
      self.w = w

  def __init__(self,  n):
    self.graph = {i:[] for i in range(n)}
    self.size = n

  def add_edge(self, origin, to, w):
    assert self.size > 0
    assert origin < self.size and to < self.size
    self.graph[origin].append(self.Edge(origin, to, w))

  def get_edges(self, origin):
    assert self.size > 0
    assert origin < self.size
    return self.graph.get(origin)
