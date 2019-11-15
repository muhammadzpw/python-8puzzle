from typing import List
from app.helpers import (
  calc_distance,
  is_possible_down,
  is_possible_left,
  is_possible_right,
  is_possible_up,
  move_up,
  move_right,
  move_left,
  move_down
)

class StateNode(object):
  state = ""
  depth = 0
  distance = 0
  cost = 0
  parent = None

  def __init__(self, state: str, goal_state: str, depth: int, parent):
    self.state = state
    self.goal_state = goal_state
    self.depth = depth
    self.parent = parent
    self.distance = calc_distance(self.state, self.goal_state)
  
  def set_cost(self, cost):
    self.cost = cost

  def expand(self) -> List[str]:
    adjacent = []
    if is_possible_left(self.state):
      adjacent.append(move_left(self.state))
    if is_possible_up(self.state):
      adjacent.append(move_up(self.state))
    if is_possible_right(self.state):
      adjacent.append(move_right(self.state))
    if is_possible_down(self.state):
      adjacent.append(move_down(self.state))
    return adjacent

class PriorityQueue(object):
  queue = []

  def add(self, node: StateNode):
    self.queue.append(node)
    self.queue = sorted(self.queue, key = lambda x: x.cost)

  def pop(self) -> StateNode:
    return self.queue.pop(0)

  def clear(self):
    self.queue.clear()

  def is_empty(self) -> bool:
    return len(self.queue) == 0
  
  def print(self):
    print(self.queue)
