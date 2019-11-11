from app.helpers import calc_distance

class StateNode(object):
  value = "" 
  def __init__(self, value, goal, parent):
    self.value = value
    self.parent = parent
    self.distance = calc_distance(value, goal)
