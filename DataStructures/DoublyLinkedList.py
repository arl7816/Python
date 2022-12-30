import sys
sys.path.append("./DataTypes")

from data_types import DoubleNode

class DoublyLinkedList:
  def __init__(self, *values) -> None:
    self.size = 0
    self.root = None
    self.end = None

    for value in values:
      self.append(value)

  def find_node(self, index) -> DoubleNode:
    replaced = None
    if index > self.size // 2:
      # start at the end of the list
      temp_index = self.size - 1
      temp_node = self.end
      while temp_index != index:
        temp_node = temp_node.left
        temp_index -= 1
      replaced = temp_node
    else:
      # start at the root of the list
      temp_node = self.root
      temp_index = 0
      while temp_index != index:
        temp_node = temp_node.right
        temp_index += 1
      replaced = temp_node
    return replaced

  def append(self, obj: object, index=None) -> None:
    if index == 0 or self.size == 0:
      self.add_front(obj)
      return

    if (index == None or index == self.size): 
      self.add_back(obj)
      return

    if index > self.size:
      raise IndexError("Index out of bounds")

    replaced = self.find_node(index)

    new_node = DoubleNode(obj, replaced.left, replaced)
    replaced.left.right = new_node
    replaced.left = new_node

    self.size += 1
    return

  def add_front(self, obj: object) -> None:
    self.size += 1
    if self.root == None:
      self.root = DoubleNode(obj, None, None)
    else:
      new_node = DoubleNode(obj, None, self.root)
      self.root.left = new_node
      self.root = new_node
    return

  def add_back(self, obj: object) -> None:
    self.size += 1
    if self.end == None:
      self.end = DoubleNode(obj, self.root, None)
      self.root.right = self.end
    else:
      new_node = DoubleNode(obj, self.end, None)
      self.end.right = new_node
      self.end = new_node
    return

  def pop(self, index=0) -> object:
    if index == 0:
      return self.pop_front()
    if index == self.size - 1:
      return self.pop_end()

    if index >= self.size:
      raise IndexError("Index " + str(index) + " out of bounds for list of size " +  str(self.size))

    remove = self.find_node(index)
    return self.pop_middle(remove)

  def pop_front(self) -> object:
    if self.size == 0:
      raise Exception("Can't remove item from an empty list")

    removed = self.root.value
    if self.size == 1:
      self.root = None
    else:
      self.root.right.left = None
      self.root = self.root.right
    self.size -= 1

    return removed

  def pop_middle(self, node: DoubleNode) -> object:
    self.size -= 1
    node.left.right = node.right
    node.right.left = node.left
    return node

  def pop_end(self) -> object:
    if self.size <= 1:
      raise Exception("Can't remove an end point that doesnt exist")

    removed = self.end
    if self.size == 2:
      self.end = None
      self.root.right = None
    else:
      prev_node = self.end.left
      prev_node.right = None
      self.end = prev_node

    self.size -= 1

    return removed

  def pop_value(self, value: object, all=False) -> None:
    if self.root == None:
      return

    current_node = self.root

    while current_node != None:
      if current_node.value == value:
        if current_node == self.root:
          self.pop_front()
        elif current_node == self.end:
          self.pop_end()
        else:
          self.pop_middle(current_node)
        
        if not all:
          return

      current_node = current_node.get_right()

    return 

  def get(self, index=0) -> object:
    if index >= self.size:
      raise IndexError("Index " + str(index) + " out of bounds for list of size " +  str(self.size))

    return self.find_node(index).value

  def get_value(self, value: object) -> int:
    current_node = self.root
    index = 0

    while current_node != None:
      if current_node.value == value:
        return index
      index += 1
      current_node = current_node.get_right()

    return -1

  def replace(self, index: int, value: object) -> None:
    self.pop(index)
    self.append(value, index)

  def __len__(self) -> int:
    return self.size

  def __str__(self) -> str:
    print_statement = ""
    temp_node = self.root
  
    if temp_node == None:
      return ""

    print_statement += str(temp_node.get_value())

    while temp_node.get_right() != None:
      temp_node = temp_node.get_right()
      print_statement += " <-> " + str(temp_node.get_value())
    
    return print_statement