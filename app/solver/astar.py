from app.solver.solver import Solver, Solution
from app.model import StateNode, PriorityQueue
from app.helpers import is_goal, pretty_print_state

class AStar(Solver):
  def __init__(self, start_state, goal_state, verbose = False):
    super().__init__(start_state, goal_state, verbose)
    self.queue = PriorityQueue()
    root_node = StateNode(start_state, goal_state, depth=0, parent=None)
    self.queue.add(root_node)

  def solve(self):
    super().solve()
    solved = False
    current_node = None
    i = 0
    while not self.queue.is_empty():
      current_node = self.queue.pop()
      current_node.set_cost(current_node.distance + current_node.depth)

      if self.verbose:
        print()
        print("Iteration: ", i)
        print("empty", self.queue.is_empty())
        print("Current state: ")
        pretty_print_state(current_node.state)
        print("Visited: ", self.visited_state)
        print("Queue: ")
        self.queue.print()

      self.visited_state.add(current_node.state)

      if is_goal(current_node.state, self.goal_state):
        solved = True
        if self.verbose:
          print("Found: ", current_node.state)
        break

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
        self.queue.add(expanding_node)
      i += 1

    if solved:
      return Solution(current_node)
    raise Exception("Error can not solve the puzzle")
