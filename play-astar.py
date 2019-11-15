from app.helpers import calc_distance, pretty_print_state, calc_distance
from app.solver import AStar

def start_solving(start_state, goal_state, verbose=False):
  solver = AStar(start_state, goal_state, verbose)
  solution = solver.solve()
  if solution:
    print("Total movements: ", solution.cost)
    print("Steps:")
    ll = solution.get_path()
    for idx, x in enumerate(reversed(ll)):
      print("#{}".format(idx))
      pretty_print_state(x.state)

if __name__ == "__main__":
  print("*** A-star Search ***")
  start = input("Masukkan Start State: ")
  goal = input("Masukkan Goal State: ")
  try:
    start_solving(start, goal, verbose=False)
  except:
    print("Unsolvable")
