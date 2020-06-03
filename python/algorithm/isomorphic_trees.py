"""Isomorphism"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from adt.graph import Graph

class TreeNode:
  def __init__(self, key, parent=None):
    self.key = key
    self.parent = parent
    self.children = []

  def add_child(self, child):
    assert isinstance(child, TreeNode)
    self.children.append(child)

  def get_children(self):
    return self.children


class IsomorphicTrees:
  @staticmethod
  def get_tree_centers(graph):
    assert isinstance(graph, Graph)
    if graph.size == 0:
      return []
    leaves = []
    degree = graph.size * [0]
    for node in graph.get_nodes():
      degree[node] = len(graph.get_edges(node))
      if degree[node] <= 1:
        leaves.append(node)

    leaves_count = len(leaves)
    while leaves_count < graph.size:
      new_leaves = []
      for leaf in leaves:
        for edge in graph.get_edges(leaf):
          degree[edge.to] -= 1
          if degree[edge.to] == 1:
            new_leaves.append(edge.to)
      leaves_count += len(new_leaves)
      leaves = new_leaves
    return leaves

  @staticmethod
  def root_tree(graph, root_key=0):
    assert isinstance(graph, Graph)
    assert graph.size > 0
    root = TreeNode(root_key, None)
    return IsomorphicTrees._build_rooted(graph, root, None)

  @staticmethod
  def _build_rooted(graph, node, parent):
    for edge in graph.get_edges(node.key):
      if parent is not None and edge.to == parent.key:
        continue
      child = TreeNode(edge.to, node)
      node.add_child(child)
      IsomorphicTrees._build_rooted(graph, child, node)
    return node

  @staticmethod
  def isomorphic_equal(g1, g2):
    assert isinstance(g1, Graph)
    assert isinstance(g2, Graph)
    assert g1.size > 0
    assert g2.size > 0
    centers_1 = IsomorphicTrees.get_tree_centers(g1)
    centers_2 = IsomorphicTrees.get_tree_centers(g2)
    root_tree1 = IsomorphicTrees.root_tree(g1, centers_1[0])
    encoded_1 = IsomorphicTrees._encode(root_tree1)
    for center in centers_2:
      root_tree2 = IsomorphicTrees.root_tree(g2, center)
      encoded_2 = IsomorphicTrees._encode(root_tree2)
      if encoded_2 == encoded_1:
        return True
    return False

  @staticmethod
  def _encode(root):
    if root is None:
      return ""
    assert isinstance(root, TreeNode)
    labels = [IsomorphicTrees._encode(c) for c in root.get_children()]
    return "(" + ''.join(sorted(labels)) + ")"
