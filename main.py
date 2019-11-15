from app.helpers import calc_distance, pretty_print_state, calc_distance
from app.solver import AStar 

# def solvable():
#   start_state = "41325678#"
#   goal_state = "12345678#"
#   solver = AStar(start_state, goal_state)
#   print(solver.is_solvable())

def start_solving(start_state, goal_state):
  # start_state = input("Input start state: ")
  # goal_state = input("Input goal state: ")
  # start_state = "41325678#"
  # goal_state = "12345678#"
  solver = AStar(start_state, goal_state)
  solution = solver.solve()
  if solution:
    print("Minimum move: ", solution.cost)
    ll = solution.get_path()
    
    for x in reversed(ll):
      pretty_print_state(x.state)
  else:
    print("Unsolved")

if __name__ == "__main__":
  # start_state = input("Input start state: ")
  # goal_state = input("Input goal state: ")
  testcase = [
    ("41325678#","12345678#"),
    ("12345678#", "123456#78"),
  ]

  for start, goal in testcase:
    print("Start: ", start)
    print("Goal: ", goal)
    start_solving(start, goal)
  # start_solving()
  # solvable()

  # print(calc_distance("8134#2765", "12345678#"))
