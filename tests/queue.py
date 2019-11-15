import unittest
from app.model import PriorityQueue, StateNode

class TestingPriorityQueue(unittest.TestCase):

  def init_queue(self):
    return PriorityQueue()

  def test_exist(self):
    q = PriorityQueue()
    print(len(q.queue))
    self.assertTrue(q.is_empty())

  def test_add(self):
    qu = PriorityQueue()
    print(qu)
    x = StateNode(
      "12345678#",
      goal_state = "12345678#",
      depth = "0",
      parent = None
    )
    qu.add(x)
    self.assertFalse(qu.is_empty())


if __name__ == '__main__':
  unittest.main()
