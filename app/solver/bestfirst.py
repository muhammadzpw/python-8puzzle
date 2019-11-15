from app.solver.solver import Solver, Solution
from app.model import StateNode
from app.helpers import is_goal

class BestFirst(Solver):
  def __init__(self, start_state, goal_state):
    super().__init__(start_state, goal_state)
  
  def solve(self):
    solved = False
    current_node = None
    while not self.queue.is_empty():
      current_node = self.queue.pop()
      current_node.set_cost(current_node.distance + current_node.depth)

      if current_node.state in self.visited_state:
        continue

      expansion = []
      for adj in current_node.expand():
        expanding_node = StateNode(
            adj,
            self.goal_state,
            depth=current_node.depth + 1,
            parent=current_node
        )
        expanding_node.set_cost(expanding_node.distance)
        expansion.append(expanding_node)

        if is_goal(adj, self.goal_state):
          solved = True
          current_node = expanding_node
          break

      if not solved:
        min_cost = min(expansion, key= lambda x: x.cost)
        self.queue.add(min_cost)
        self.visited_state.add(current_node.state)
      else:
        break

    if solved:
      return Solution(current_node)
    return None
