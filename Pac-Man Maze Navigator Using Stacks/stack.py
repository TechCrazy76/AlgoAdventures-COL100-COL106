class Stack:
  def __init__(self) -> None:
      self.list = []
      
  def is_empty(self):
      return len(self.list) == 0

  def push(self, item) -> None:
      self.list.append(item)

  def pop(self) -> None:
      if not self.is_empty():
          return self.list.pop()
      else:
          return None

  def top(self):
      if not self.is_empty():
          return self.list[-1]
      else:
          return None

  def size(self):
      return len(self.list)
