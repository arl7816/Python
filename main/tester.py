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
from HashSet import HashSet
from DoublyLinkedList import DoublyLinkedList

def random_array(size: int, low:int, high:int) -> list[int]:
  """
  [summary]
  Creates an array with each index having a random number

  Args:
      size (int): the size of the entire array
      low (int): the lowest possible integer value
      high (int): the highest possible integer value

  Returns:
      list[int]: an array of integers that are random
  """

  return [ran(low, high) for _ in range(size)]

def main():
  mapset = HashSet()
  
  mapset.assign(4)

  print(mapset)

  return None

if __name__ == "__main__":
  main()