from app.solver.solver import Solver, Solution
from app.model import StateNode
from app.helpers import is_goal, pretty_print_state

class AStar(Solver):
  def __init__(self, start_state, goal_state):
    super().__init__(start_state, goal_state)

  def solve(self):
    solved = False
    current_node = None
    i = 0
    while not self.queue.is_empty():
      print()
      print("Iteration: ", i)
      current_node = self.queue.pop()
      print("empty", self.queue.is_empty())
      print("Current state: ")
      pretty_print_state(current_node.state)
      print("Queue: ")
      self.queue.print()

      current_node.set_cost(current_node.distance + current_node.depth)
      self.visited_state.add(current_node.state)

      if is_goal(current_node.state, self.goal_state):
        solved = True
        print("Found: ", current_node.state)
        break

      expansion = []
      print("Expansion: ")

      for adj in current_node.expand():
        if adj in self.visited_state:
          continue

        expanding_node = StateNode(
            adj,
            self.goal_state,
            depth = current_node.depth + 1,
            parent = current_node
        )
        expanding_node.set_cost(expanding_node.distance + expanding_node.depth)
        expansion.append(expanding_node)
        self.queue.add(expanding_node)

      # min_cost = min(expansion, key= lambda x: x.cost)
      # self.queue.add(min_cost)
      i += 1

    if solved:
      return Solution(current_node)
    return None
