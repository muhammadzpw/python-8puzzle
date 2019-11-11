from app.helpers import calc_distance
from app.astar import AStar 

if __name__ == "__main__":
  start_state = input("Input start state: ")
  goal_state = input("Input goal state: ")

  solver = AStar(start_state, goal_state)
  solution = solver.solve()
  print(solution.cost)
  ll = solution.get_path()
  
  for x in ll:
    print(x.state)