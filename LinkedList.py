from data_types import Node, EntryNode

class LinkedList:
  def __init__(self, value: any, key=None) -> None:
    self.size = 1

    if key == None:
      self.root = Node(value, None)
    else:
      self.root = EntryNode(key, value, None)

  def create_node(self, value, link=None, key=None):
    self.size += 1
    if key == None:
      return Node(value, link=link)
    else:
        return EntryNode(key, value, link)

  def get_root(self) -> Node:
    return self.root

  def get(self, index=0) -> Node:
    if index >= self.size:
      raise IndexError("Index", index, "is out of bounds for a linked list of size ", self.size)

    if index == 0:
      return self.root

    temp_node = self.root
    for i in range(1, index):
      temp_node = temp_node.get_link()
    return temp_node

  def get_value(self, value: any) -> int:
    index = 0
    temp_node = self.root
    while temp_node != None:
      if temp_node.get_value() == value:
        return index
      temp_node = temp_node.get_link()
      index += 1
    return -1

  def get_key(self, key: any) -> int:
    index = 0
    temp_node = self.root

    while temp_node != None:
      if hasattr(temp_node, "key"):
        if temp_node.get_key() == key:
          return index
      temp_node = temp_node.get_link()
      index += 1

    return -1

  def append(self, value: any, index=None, key=None) -> None: # will add it to the start and anywhere else
    if index == None: index=self.size
      
    if index > self.size:
      raise IndexError("Index", index, "is out of bounds for a linked list of size ", self.size)

    if index == 0:
      return self.set_root(value, key)

    temp_node = self.root
    prev_node = self.root
    for _ in range(1, index+1):
      prev_node = temp_node
      temp_node = temp_node.get_link()
    # we now have the node we want
    
    if temp_node == None: # were at the tail node
      prev_node.set_link(self.create_node(value, key=key))
      return
    
    # were in the middle nodes
    new_node = self.create_node(value, key=key, link=temp_node)
    prev_node.set_link(new_node)

  def set_root(self, value: any, key=None) -> None:
    temp_node = self.create_node(value, key=key, link=self.root)
    self.root = temp_node

  def pop(self, index = None) -> Node:
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
      return prev_node
    
    # were in the middle nodes
    self.size -= 1
    prev_node.set_link(temp_node.get_link())
    return temp_node

  def pop_root(self) -> Node:
    removed = self.root
    self.root = self.root.get_link()
    self.size -= 1
    return removed

  def __str__(self) -> str:
    print_statement = ""
    temp_node = self.root
  
    if temp_node == None:
      return ""

    print_statement += temp_node.__str__()

    while temp_node.get_link() != None:
      temp_node = temp_node.get_link()
      print_statement += " -> " + temp_node.__str__()
    
    return print_statement