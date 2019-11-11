from typing import List
from app.model import PriorityQueue, StateNode

class Solution(object):
  cost = 0
  path = []

  def __init__(self, goal_node: StateNode):
    self.traceback(goal_node)

  def set_cost(self, cost):
    self.cost = cost

  def set_path(self, path):
    self.path = path
  
  def get_path(self) -> List[StateNode]:
    return self.path

  def traceback(self, goal_node: StateNode):
    current_node = goal_node
    self.path.append(current_node)
    while True:
      if current_node.parent is None:
        break
      else:
        current_node = current_node.parent
        self.path.append(current_node)

    self.cost = len(self.path)
      

class Solver(object):
  goal_state = ""
  start_state  = ""
  visited_state = set()
  queue = PriorityQueue()

  def __init__(self, start_state, goal_state):
    self.start_state = start_state
    self.goal_state = goal_state
    root_node = StateNode(start_state, goal_state, depth=0, parent=None)
    self.queue.add(root_node)
    
  def solve(self):
    raise NotImplementedError
