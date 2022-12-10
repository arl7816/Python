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

  def __ne__(self, obj: object): # not equal to
    result = True
    if type(obj) == type(self):
      result = obj.value != self.value and obj.link == self.link
    return result

  def __str__(self) -> str:
    return "Node: V=" + str(self.value)
  
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

  def __str__(self) -> str:
    return "EntryNode: K=" + str(self.key)

@dataclass (frozen=True)
class Entry:
  key: any
  value: any