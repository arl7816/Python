from data_types import Node, DoubleNode

class Queue:
  def __init__(self, obj = None) -> None:
    self.size = 0
    self.front = None
    self.back = None

    if obj != None:
      self.front = DoubleNode(obj, None, None)
      self.size = 1

  def peek(self) -> object:
    if self.size > 0:
      return None
    return self.front.get_value()

  def add(self, obj: object) -> None:
    if self.back == None:
      self.back = DoubleNode(obj, None, self.front)
      self.front.left = self.back
    else:
      new_back = DoubleNode(obj, None, self.back)
      self.back.left = new_back
      self.back = new_back
    self.size += 1

  def pop(self) -> object:
    if self.size == 0:
      raise IndexError("Cannot pop an empty stack")
    
    self.size -= 1

    removed = self.front
    if self.size == 0:
      self.front = None
    elif self.size == 1:
      self.front = DoubleNode(self.back.get_value(), None, None)
      self.back = None
    else:
      self.front = self.front.left
      self.front.right = None

    return removed

  def __str__(self) -> str:
    print_statement = ""
    temp_node = self.back
  
    if self.size == 0:
      return ""
    elif self.size == 1:
      return str(self.front.value)

    print_statement += str(temp_node.get_value())

    while temp_node.right != None:
      temp_node = temp_node.right
      print_statement += " <- " + str(temp_node.get_value())
    
    return print_statement