"""Graph bfs"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from collections import deque

# grid = [[0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 0],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0]]

def construct_path(prev, start, end):
  if prev[end[0]][end[1]] is None:
    return []
  path = []
  at = end
  while at:
    path.insert(0, at)
    at = prev[at[0]][at[1]]
  if path[0] != start: return []
  return path

def shortest_path(grid, start, end):
  if start == end:
    return 0
  rows = len(grid)
  cols = len(grid[0]) if rows else 0
  if rows == 0 or cols == 0: return -1, []

  sr, sc = start
  q = deque()
  q.append(start)
  prev = [cols*[None] for _ in range(rows)]
  visited = [cols*[0] for _ in range(rows)]
  visited[sr][sc] = 1

  move_count = 0
  nodes_left_in_layer = 1
  nodes_in_next_layer = 0
  reached = False
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  while q:
    r, c = q.popleft()
    if [r, c] == end:
      reached = True
      break
    for i in range(4):
      y = r + dy[i]
      x = c + dx[i]
      if x < 0 or y < 0 or x >= cols or y >= rows:
        continue
      if visited[y][x] or grid[y][x] == 1:
        continue
      visited[y][x] = 1
      q.append([y, x])
      prev[y][x] = [r, c]
      nodes_in_next_layer += 1
    nodes_left_in_layer -= 1
    if nodes_left_in_layer == 0:
      move_count += 1
      nodes_left_in_layer = nodes_in_next_layer
      nodes_in_next_layer = 0
  if reached:
    return move_count, construct_path(prev, start, end)
  return -1, []

if __name__ == "__main__":
  grid = [[0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 0, 0, 0]]
  move, path = shortest_path(grid, [0,4], [4, 4])
  print('shortest path from [0, 4] to [4, 4] is ', move)
  print('path: ', path)
        
