# system imports
from time import perf_counter
from random import randint as ran
import sys

sys.path.append("./SearchesAndSorts")
sys.path.append("./DataStructures")
sys.path.append("./DataTypes")

# custom imports (if an import is not working, make sure to change the
# json file in .vscode so the code knows where to look)
import sorts
import searches
from data_types import *
from LinkedList import LinkedList
from Stack import Stack
from Queue import Queue

def random_array(size: int, low:int, high:int) -> list[object]:
  arr = []
  for _ in range(size):
    arr.append(ran(low, high))
  return arr

def main():
  
  q = Queue("A")

  print("Popped", q.pop())

  print(q)

  return None

if __name__ == "__main__":
  main()