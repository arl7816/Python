from data_types import Node, EntryNode

class Stack:
  def __init__(self, obj = None) -> None:
    self.size = 0
    self.head = None

    if obj != None:
      self.size = 1
      self.head = Node(obj, None)

  def peek(self) -> object:
    if self.size > 0:
      return None

    return self.head.get_value()

  def is_empty(self) -> bool:
    return self.size == 0

  def get_size(self) -> int:
    return self.size

  def pop(self) -> object:
    if self.head == None:
      raise IndexError("Cannot remove element from an empty stack")

    temp_head = self.head
    self.head = self.head.get_link()
    self.size -= 1
    return temp_head.get_value()

  def add(self, obj: object) -> None:
    self.head = Node(obj, self.head)
    self.size += 1
    return

  def __str__(self) -> str:
    print_statement = ""
    temp_node = self.head

    while temp_node != None:
      print_statement += temp_node.value

      if temp_node.get_link() != None:
        print_statement += "\n|\nV\n"

      temp_node = temp_node.get_link()
    return print_statement