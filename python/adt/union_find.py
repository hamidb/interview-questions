"""A Union Find Data Structure"""

class UnionFind:
  def __init__(self, size):
    self.size = size
    self.parents = list(range(size))
    self.c_size = size * [1]  # size of each component.
    self.num_component = size

  def find(self, p):
    # returns component root.
    root = p
    while root != self.parents[root]:
      root = self.parents[root]
    # compress
    while p != root:
      tmp = self.parents[p]
      self.parents[p] = root
      p = tmp
    return root

  def is_connected(self, p, q):
    return self.find(p) == self.find(q)

  def component_size(self, p):
    return self.c_size[self.find(p)]

  def component_nums(self):
    return self.num_component

  def unify(self, p, q):
    if self.is_connected(p, q):
      return
    root1 = self.find(p)
    root2 = self.find(q)
    size1 = self.c_size[root1]
    size2 = self.c_size[root2]
    if size2 > size1:
      self.parents[root1] = root2
      self.c_size[root2] += size1
    else:
      self.parents[root2] = root1
      self.c_size[root1] += size2
    self.num_component -= 1
