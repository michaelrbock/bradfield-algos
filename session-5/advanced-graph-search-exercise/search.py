from collections import deque
from constants import *
import heapq
import itertools


# UP, LEFT, DOWN, RIGHT
_DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def _neighbors(grid, row, col):
  for r_offset, c_offset in _DIRECTIONS:
    next_row, next_col = row + r_offset, col + c_offset
    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
      if grid[next_row][next_col] != M:
        yield (next_row, next_col), COSTS[grid[next_row][next_col]]


def graph_search(grid, start, goal, cost_fxn):
  explored = {}  # { (row, col) : previous (row, col) }
  to_visit = [(0, start, None)]  # (priority, node, previous)
  while to_visit:
    cost_so_far, (row, col), prev = heapq.heappop(to_visit)
    if (row, col) in explored:
      continue
    explored[(row, col)] = prev
    if (row, col) == goal:
      break
    for (next_row, next_col), cost in _neighbors(grid, row, col):
      if (next_row, next_col) not in explored:
        heapq.heappush(
          to_visit,
          (cost_fxn(explored, cost_so_far + cost, (next_row, next_col), goal),
            (next_row, next_col), (row, col)))
  return explored


def bfs(grid, start, goal):
  return graph_search(grid, start, goal, lambda e, *args: len(e))


def bfs1(grid, start, goal):
  explored = {}  # { (row, col) : previous (row, col) }
  to_visit = deque([(start, None)])  # (node, previous)
  while to_visit:
    (row, col), prev = to_visit.popleft()
    explored[(row, col)] = prev
    if (row, col) == goal:
      break
    for (next_row, next_col), _ in _neighbors(grid, row, col):
      if (next_row, next_col) not in explored:
        to_visit.append(((next_row, next_col), (row, col)))
  return explored


def dfs(grid, start, goal):
  return graph_search(grid, start, goal, lambda *args: 0)


def dfs1(grid, start, goal):
  explored = {}  # { (row, col) : previous (row, col) }
  to_visit = deque([(start, None)])  # (node, previous)
  while to_visit:
    (row, col), prev = to_visit.pop()
    explored[(row, col)] = prev
    if (row, col) == goal:
      break
    for (next_row, next_col), _ in _neighbors(grid, row, col):
      if (next_row, next_col) not in explored:
        to_visit.append(((next_row, next_col), (row, col)))
  return explored


def ucs(grid, start, goal):
  return graph_search(grid, start, goal, lambda _, c, *args: c)


def ucs1(grid, start, goal):
  explored = {}  # { (row, col) : previous (row, col) }
  to_visit = [(0, start, None)]  # (priority, node, previous)
  while to_visit:
    cost_so_far, (row, col), prev = heapq.heappop(to_visit)
    explored[(row, col)] = prev
    if (row, col) == goal:
      break
    for (next_row, next_col), cost in _neighbors(grid, row, col):
      if (next_row, next_col) not in explored:
        heapq.heappush(to_visit,
          (cost_so_far + cost, (next_row, next_col), (row, col)))
  return explored


def _heuristic(start, goal):
  return abs(goal[0] - start[0]) + abs(goal[1] - start[1])


def a_star(grid, start, goal):
  return graph_search(grid, start, goal,
    lambda _, c, s, g: c + _heuristic(s, g))


def a_star1(grid, start, goal):
  explored = {}  # { (row, col) : previous (row, col) }
  to_visit = [(0, start, None)]  # (priority, node, previous)
  while to_visit:
    cost_so_far, (row, col), prev = heapq.heappop(to_visit)
    if (row, col) in explored:
      continue

    explored[(row, col)] = prev

    if (row, col) == goal:
      break
    for (next_row, next_col), cost in _neighbors(grid, row, col):
      new_cost = cost_so_far + cost
      if (next_row, next_col) not in explored:
        heapq.heappush(to_visit,
          (new_cost + _heuristic((next_row, next_col), goal),
            (next_row, next_col), (row, col)))
  return explored
