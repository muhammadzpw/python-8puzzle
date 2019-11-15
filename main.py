from app.helpers import calc_distance, pretty_print_state, calc_distance
from app.solver import AStar, BestFirst

def start_solving(start_state, goal_state, verbose=False):
  # solver = AStar(start_state, goal_state, verbose)
  solver = BestFirst(start_state, goal_state, verbose)
  solution = solver.solve()
  if solution:
    print("Total movements: ", solution.cost)
    print("Steps:")
    ll = solution.get_path()
    for idx, x in enumerate(reversed(ll)):
      print("#{}".format(idx))
      pretty_print_state(x.state)

if __name__ == "__main__":
  testcase = [
    ("41325678#","12345678#"),
    ("12345678#", "123456#78"),
    ("12345678#", "123456#87"),
  ]

  for start, goal in testcase:
    print("********************")
    print("Start: ", start)
    print("Goal: ", goal)
    try:
      start_solving(start, goal, verbose=False)
    except:
      print("Unsolvable")
