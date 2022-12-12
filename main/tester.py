import sorts
import searches
from time import perf_counter
from random import randint as ran
from data_types import *
from LinkedList import LinkedList

def random_array(size: int, low:int, high:int) -> list[object]:
  arr = []
  for _ in range(size):
    arr.append(ran(low, high))
  return arr

def main():
  linked = LinkedList(5, "A")
  linked.append_key("B", 5)
  linked.append_key("D", 7, index=1)
  linked.append_key("E", 7, index=1)
  linked.append(4)
  linked.append(1, 0)
  linked.set_root(5, "TITy")
  linked.set_root(7)
  linked.append(7)
  linked.append_key("E", 0)

  print(linked)

  linked.pop_value(7, True)
  print(linked)
  print(linked.size)

  return None

if __name__ == "__main__":
  main()