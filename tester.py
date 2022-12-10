import sorts
import searches
from time import perf_counter
from random import randint as ran
from data_types import *

def random_array(size: int, low:int, high:int) -> list[object]:
  arr = []
  for _ in range(size):
    arr.append(ran(low, high))
  return arr

def main():
  a = Node(5,None)
  b = Node(5,a)
  a.set_link(b)

  print(a < b)
  print(a)

  dic = dict()
  c = EntryNode("Hello", "world")
  c.value = "take"
  dic[c.key] = "Hello"

  return None

if __name__ == "__main__":
  main()