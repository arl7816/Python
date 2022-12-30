from data_types import Node

class LinkedList:
  def __init__(self, *values) -> None:
    self.size = 0
    self.root = None

    for value in values:
      self.append(value)

  def create_node(self, value, link=None):
    self.size += 1
    return Node(value, link=link)

  def get_root(self) -> object:
    return self.root.get_value()

  def get(self, index=0) -> object:
    if index >= self.size:
      raise IndexError("Index", index, "is out of bounds for a linked list of size ", self.size)

    if index == 0:
      return self.root.get_value()

    temp_node = self.root
    for _ in range(1, index):
      temp_node = temp_node.get_link()
    return temp_node.get_value()

  def get_value(self, value: any) -> int:
    index = 0
    temp_node = self.root
    while temp_node != None:
      if temp_node.get_value() == value:
        return index
      temp_node = temp_node.get_link()
      index += 1
    return -1

  def append(self, obj: object, index=None) -> None: # will add it to the start and anywhere else
    if index == None: index=self.size
      
    if index > self.size:
      raise IndexError("Index", index, "is out of bounds for a linked list of size ", self.size)

    if index == 0:
      return self.set_root(obj)

    temp_node = self.root
    prev_node = self.root
    for _ in range(1, index+1):
      prev_node = temp_node
      temp_node = temp_node.get_link()
    # we now have the node we want
    
    if temp_node == None: # were at the tail node
      prev_node.set_link(self.create_node(obj))
      return
    
    # were in the middle nodes
    new_node = self.create_node(obj, link=temp_node)
    prev_node.set_link(new_node)

  def set_root(self, obj: object) -> None:
    temp_node = self.create_node(obj, link=self.root)
    self.root = temp_node

  def pop(self, index = None) -> object:
    if index != None and index >= self.size:
      raise IndexError("Index", index, "is out of bounds for a linked list of size ", self.size)

    if index == None: index=self.size - 1

    if index == 0:
      return self.pop_root()

    temp_node = self.root
    prev_node = self.root
    for _ in range(1, index+1):
      prev_node = temp_node
      temp_node = temp_node.get_link()
    # we now have the node we want
    
    if temp_node == None: # were at the tail node
      prev_node.set_link = None
      self.size -= 1
      return prev_node.get_value()
    
    # were in the middle nodes
    self.size -= 1
    prev_node.set_link(temp_node.get_link())
    return temp_node.get_value()

  def pop_root(self) -> object:
    removed = self.root
    self.root = self.root.get_link()
    self.size -= 1
    return removed.get_value()

  def pop_value(self, checker: any, all = False) -> None:
    def check_element(element: object) -> bool:
      return element.value == checker

    stop_change = False
    if self.root == None:
      return

    temp_node = self.root
    prev_node = None

    if check_element(temp_node): # remove the first node
      self.pop_root()
      if not all: return

    while temp_node.get_link() != None:
      if not stop_change:
        prev_node = temp_node
      else:
        stop_change = False
      temp_node = temp_node.get_link()

      if check_element(temp_node):
        if temp_node == None: # this is the final node
          prev_node.set_link = None
        else: # this is a middle node
          prev_node.set_link(temp_node.get_link())
          stop_change = True
        self.size -= 1
        if not(all): return

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

    while temp_node.get_link() != None:
      temp_node = temp_node.get_link()
      print_statement += " -> " + str(temp_node.get_value())
    
    return print_statement