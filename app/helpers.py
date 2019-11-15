from app.config import SPACE_SYMBOL

def calc_distance(state: str, goal_state: str) -> int: 
  '''
  Manhattan Distance
  '''
  distance = 0
  for idx, val in enumerate(state):
    if val == SPACE_SYMBOL:
      continue
    goal_idx = goal_state.index(val)
    d = abs(idx % 3 - goal_idx % 3) + abs(idx // 3 - goal_idx // 3)
    distance += d 
  return distance

def find_space_position(input: str) -> int:
  return input.index(SPACE_SYMBOL)

def is_possible_up(input: str) -> bool:
  space_position = find_space_position(input)
  if space_position in [0, 1, 2]:
    return False
  return True

def is_possible_left(input: str) -> bool:
  space_position = find_space_position(input)
  if space_position in [0, 3, 6]:
    return False
  return True

def is_possible_right(input: str) -> bool:
  space_position = find_space_position(input)
  if space_position in [2, 5, 8]:
    return False
  return True

def is_possible_down(input: str) -> bool:
  space_position = find_space_position(input)
  if space_position in [6, 7, 8]:
    return False
  return True

def is_move_possible(move, input) -> bool:
  if move == "up":
    return is_possible_up(input)
  elif move == "left":
    return is_possible_left(input)
  elif move == "right":
    return is_possible_right(input)
  elif move == "down":
    return is_possible_down(input)
  else:
    raise Exception("Unknown move")

def move_up(input: str) -> str:
  if not is_possible_up(input):
    return None
  space_position = find_space_position(input)
  switch_space_position = space_position - 3
  return switch_position(input, space_position, switch_space_position)

def move_down(input:str) -> str:
  if not is_possible_down(input):
    return None
  space_position = find_space_position(input)
  switch_space_position = space_position + 3
  return switch_position(input, space_position, switch_space_position)

def move_left(input: str) -> str:
  if not is_possible_left(input):
    return None
  space_position = find_space_position(input)
  switch_space_position = space_position - 1
  return switch_position(input, space_position, switch_space_position)

def move_right(input: str) -> str:
  if not is_possible_right(input):
    return None
  space_position = find_space_position(input)
  switch_space_position = space_position + 1
  return switch_position(input, space_position, switch_space_position)

def switch_position(input: str, idx: int, switch_idx: int) -> str:
  output = list(input)
  tmp = output[switch_idx]
  output[switch_idx] = output[idx]
  output[idx] = tmp
  return list_to_str(output)

def list_to_str(lst: list):
  out = ""
  for x in lst:
    out += x
  return out

def is_goal(current, goal) -> bool:
  return current == goal

def pretty_print_state(state: str):
  print(state[0:3])
  print(state[3:6])
  print(state[6:9])
  print()

# print(move_up("123#45678"))
# print(move_right("123#45678"))
# print(move_down("123#45678"))
# print(move_left("123#45678"))
413
256
78#

41325678#