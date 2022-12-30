from LinkedList import LinkedList

class HashSet:
  CAPACITY = 60 # percentage

  def __init__(self) -> None:
    self.size = 0
    self.total_size = 100
    self.map = [LinkedList()]*self.total_size

  def assign(self, key: object) -> None:
    index = self.compress(hash(key))
    exist = self.map[index].get_value(key)
    if exist == -1:
      # the object is new
      self.map[index].append(key, 0)
    else:
      self.map[index].replace(exist, key)

  def contains(self, key: object) -> bool:
    index = self.compress(hash(key))
    return self.map[index].get_value(key) != -1

  def rehash(self):
    pass

  def compress(self, index: int) -> int:
    return index % self.total_size

  def __str__(self) -> str:
    print_statement = ""
    for lst in self.map:
      if lst.size == 0:
        continue
      print_statement += "("
      node = lst.root
      while node != None:
        print_statement += str(node.value) + ','
        node = node.get_link()
      print_statement += ")"
    return print_statement
