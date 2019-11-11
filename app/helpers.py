def calc_distance(stateA: str, stateB: str) -> int: 
  if len(stateA) != len(stateB):
    raise Exception("The size of input a and b should be equal.")
  if len(stateA) != 9:
    raise Exception("The size of input must be exactly 9")
  distance = 0
  for i in range(len(stateA)):
    if stateA[i] != stateB[i]:
      distance += 1
  return distance

def find_space_position(input: str) -> int:
  return input.index('#')

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

# print(move_up("123#45678"))
# print(move_right("123#45678"))
# print(move_down("123#45678"))
# print(move_left("123#45678"))
