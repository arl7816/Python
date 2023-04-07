# system imports
from time import perf_counter
from random import randint as ran
import sys
from math import e, log

sys.path.append("./SearchesAndSorts")
sys.path.append("./DataStructures")
sys.path.append("./DataTypes")
sys.path.append("./Algorithms")

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
from calc import integrate, ln, loga
from math import e

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

def f(x):
  return 3*pow(e, (-x/4))

def main():
  #mapset = HashSet()
  
  #mapset.assign(4)

  #print(mapset)

  x = 1
  a = 2

  n = 20
  print("Answer should be: 9")
  print("Right-point method with n =", n, ":", integrate(f, 1, 2, "right", n))
  print("Left-point method with n =", n, ":", integrate(f, 1, 2, "left", n))
  print("mid-point method with n =", n, ":", integrate(f, 0, 1, "mid", n))
  print("trapezoid method with n =", n, ":", integrate(f, 0, 9, "trapezoid", n))
  print("simp method with n =", n, ":", integrate(f, -3, 3, "simp", n))

  print("ln(" + str(x) + ") is:", log(x,e), " vs estimate: ", ln(x, 50))
  print("log(" + str(x) + ", " + str(a) + ") is:", log(x,a), " vs estimate: ", loga(a,x, 50))

  return None

if __name__ == "__main__":
  main()