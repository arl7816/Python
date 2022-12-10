from dataclasses import dataclass

class Node:
  def __init__(self, value: any, link = None) -> None:
    self.value = value
    self.link = link

  def get_link(self) -> object:
    return self.link

  def get_value(self) -> any:
    return self.value

  def set_value(self, value: int) -> None:
    self.value = value
  
  def set_link(self, link: object) -> None:
    self.link = link

  def __eq__(self, node: object) -> bool:
    result = False
    if type(node) == type(self):
      result = node.value == self.value and node.link == self.link
    return result

  def __ge__(self, obj: object): # greater than or equal
    result = False
    if type(obj) == type(self):
      result = self.value >= obj.value
    return result
  
  def __gt__(self, obj: object): # greater than
    result = False
    if type(obj) == type(self):
      result = self.value > obj.value
    return result

  def __lt__(self, obj: object): # less than
    result = False
    if type(obj) == type(self):
      result = self.value < obj.value
    return result

  def __le__(self, obj: object): #less than or equal to
    result = False
    if type(obj) == type(self):
      result = self.value <= obj.value
    return result

  def __ne__(self, obj: object): # not equal to
    result = True
    if type(obj) == type(self):
      result = obj.value != self.value and obj.link == self.link
    return result

  def __str__(self) -> str:
    return "Node: (value=" + str(self.value) + ")"
  
class EntryNode(Node):
  def __init__(self, key: any , value: any, link=None) -> None:
    super().__init__(value, link)
    self.key = key
  
  def get_key(self):
    return self.key

  def __setattr__(self, name: any, value: any) -> None:
    if hasattr(self, "key") and name == "key":
      raise Exception("Cannot change the value of a key")

    return super().__setattr__(name, value)

@dataclass (frozen=True)
class Entry:
  key: any
  value: any