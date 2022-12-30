from data_types import Node, DoubleNode

class Queue:
  """
  [summary]
  A Queue is a type of linked list based on the first-in, first-out paradigm. In which, each node is appened to the
  end of the list and each node that is accessed, is taken from the front of the list, similar to line.
  """
  def __init__(self, *values) -> None:
    """
    [Summary]
    The constructor for the Queue

    Args:
        obj (object, optional): The starting value for the Queue. Defaults to None.
    """
    self.size = 0
    self.front = None
    self.back = None

    for value in values:
      self.add(value)

  def peek(self) -> object:
    """
    Grabs the front node without removing it
    \nO(n) = 1

    Returns:
        object: the front node
    """
    if self.size > 0:
      return None
    return self.front.get_value()

  def add(self, obj: object) -> None:
    """Adds a value to the back of the queue
    \nO(n) = 1

    Args:
        obj (object): the value to added to the queue
    """
    if self.front == None:
      self.front = DoubleNode(obj, None, None)
    elif self.back == None:
      self.back = DoubleNode(obj, None, self.front)
      self.front.left = self.back
    else:
      new_back = DoubleNode(obj, None, self.back)
      self.back.left = new_back
      self.back = new_back
    self.size += 1

  def pop(self) -> object:
    """Removes the element at the front of the queue
    O(n) = 1

    Raises:
        IndexError: If no values exist, an index error will occur

    Returns:
        object: the removed value
    """
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

  def __len__(self) -> int:
    """Gets the total size of the Queue

    Returns:
        int: the size of the queue
    """
    return self.size

  def __str__(self) -> str:
    """Grabs a string representation of the queue in the form
    \n D <- C <- B <- A...
    \n where D is back of the queue and A is the front of the queue

    Returns:
        str: A string representation of the queue
    """
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