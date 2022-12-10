from dataclasses import dataclass

def linear_search(arr: list[object], element: object) -> int:
  """
  [Summary] Finds an element in the array and returns the index of its location using a linear search
  \n O(n) = n      
  \nθ(n) = 1      
  \nΩ(n) = n
  \n\t where n is the amount of elements in the array

  Args:
      arr (list(object)): array of elements
      element (object): the element your searching for

  Returns:
      int: Index of the found item, returns -1 if not found
  """
  index = -1
  for item in arr:
    index += 1
    if item == element:
      return index
  return -1

# not finished yet
def pointed_search(arr: list[object], element: object, c=100) -> int:
  @dataclass
  class Pointer:
    index: int
    dir: int

  def add_pointers(temp_arr: list[object]):
    if len(temp_arr) > c:
      center_index = len(temp_arr) // 2
      leftPointer = Pointer(center_index, -1)
      rightPointer = Pointer(center_index, 1)
      pointers.append(leftPointer)
      pointers.append(rightPointer)
      add_pointers(temp_arr[:center_index])
      add_pointers(temp_arr[center_index:])


  if len(arr) == 1:
    if arr[0] == element:
      return 0
  elif len(arr) == 0:
    return -1

  start = Pointer(0,1)
  end = Pointer(len(arr)-1, -1)
  pointers = [start, end]

  add_pointers(arr, c)

  return -1

def binary_search(arr: list[object], element: object) -> int:
  """
  [Summary] Finds an element in the array and returns the index of its location using a linear search
  \n*Assumes the array to be ordered*
  \n O(n) = logn      
  \nθ(n) = 1      
  \nΩ(n) = logn
  \n\t where n is the amount of elements in the array

  Args:
      arr (list(object)): array of elements
      element (object): the element your searching for

  Returns:
      int: Index of the found item, returns -1 if not found
  """

  start = 0
  end = len(arr)

  while (start != end):
    index = (end - start) // 2

    if (arr[index] == (element)):
      return index
    
    if (arr[index] > element):
      end = index
    else:
      start = index

  return -1

def main():
  array = [0,1,2,3,4,5,6,7,8,9]

  print(linear_search(array, 6))

  return None


if __name__ == "__main__":
  main()