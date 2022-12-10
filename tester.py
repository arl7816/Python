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
  linked.append(6, key="B")
  linked.append(7, key="D", index=1)
  linked.append(7, key="E", index=1)
  linked.append(4)
  linked.append(1, 0)
  linked.set_root(5, "TITy")

  print(linked)
  print("Index =", linked.get_key("TITy"))

  linked.pop()
  print(linked)

  linked2 = LinkedList(5)
  linked2.append(6)
  linked2.pop(0)
  print(linked2)

  return None

if __name__ == "__main__":
  main()