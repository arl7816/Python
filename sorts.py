from random import randint as ran

def compare(obj1: object, obj2: object, greater=False) -> bool:
  """
  [summary]
  Compares two objects to see if one object is greater than the other

  Args:
      obj1 (object): the first object
      obj2 (object): the second object
      greater (bool, optional): True if object one should be greater than object two. Defaults to False.

  Returns:
      bool: true is object 1 is greater/less than object 2
  """
  if greater:
    return obj1 > obj2
  else:
    return obj1 < obj2

def selection_sort(arr: list[object], reverse = False) -> list[object]:
  """[summary] Gets the sorted list of a array of objects using the selection sort method
  \nO(n) = n^2
  \nθ(n) = n^2  
  \nΩ(n) = n^2
  \n\t where n is the amount of elements in the array

  Args:
      arr (list[object]): Array of objects
      reverse (bool, optional): If true, list will be sorted in reverse. Defaults to False.

  Returns:
      list[object]: a sorted version of the list
  """
  sorted = []

  l = len(arr)
  for _ in range(l):
    maxi = 0
    for y in range(len(arr)):
      if arr[maxi] == None: maxi = y
      
      if arr[maxi] == None or arr[y] == None:
        continue
    
      if compare(arr[y], arr[maxi], reverse):
        maxi = y
      
    sorted.append(arr[maxi])
    arr[maxi] = None


  return sorted

def insertion_sort(arr: list[object], reverse=False) -> list[object]:
  """[summary] Gets the sorted list of a array of objects using the insertion sort method
  \nO(n) = n^2
  \nθ(n) = n  
  \nΩ(n) = n^2
  \n\t where n is the amount of elements in the array

  Args:
      arr (list[object]): Array of objects
      reverse (bool, optional): If true, list will be sorted in reverse. Defaults to False.

  Returns:
      list[object]: a sorted version of the list
  """
  def swap(i1: int, i2: int) -> None:
    temp = sorted[i1]
    sorted[i1] = sorted[i2]
    sorted[i2] = temp
    return None

  sorted = []

  for element in arr:
    sorted.append(element)

    index = len(sorted) - 1
    while index != 0:
      if compare(sorted[index - 1], sorted[index], not(reverse)):
        swap(index, index-1)
        index -= 1
      else:
        break

  return sorted


def merge(arr1: list[object], arr2: list[object], reverse=False) -> list[object]:
  """[summary]
  Merges two sorted lists together so that the whole thing altogether is sorted
  \nO(n) = n
  \nθ(n) = n  
  \nΩ(n) = n
  \n\tWhere n is the total number of elements in the two arrays

  Args:
      arr1 (list[object]): the first array of objects
      arr2 (list[object]): the secons array of the objects
      reverse (bool, optional): Are the pre-sorted arrays in a reversed order. Defaults to False.

  Returns:
      list[object]: a combined list of the two arrays, in a sorted condition
  """
  sorted = []
  left, right = 0,0

  while len(arr1) != left and len(arr2) != right:
    if compare(arr1[left], arr2[right], reverse):
      sorted.append(arr1[left])
      left += 1
    else:
      sorted.append(arr2[right])
      right += 1

  if left == len(arr1): sorted += arr2[right:]
  else: sorted += arr1[left:]

  return sorted


def merge_sort(arr: list[object], reverse=False) -> list[object]:
  """
  [summary] Gets the sorted list of a array of objects using the merge sort method
  
    Args:
      arr (list[object]): Array of objects
      reverse (bool, optional): If true, list will be sorted in reverse. Defaults to False.

    Returns:
      list[object]: a sorted version of the list

  \nComplexity:
  \nO(n) = n^2
  \nθ(n) = n  
  \nΩ(n) = n^2
  \n\t where n is the amount of elements in the array

  \nMerge Sort works by spliting the array into sub arrays until they reach their base cases of being
  one, element. Upon which it merges each of the sorted sub arrays until the entire array is sorted

  \nSample Run:
  \n[7,5,2,4,1,6,3,0]
  \n[7,5,2,4]\t[1,6,3,0]
  \n[7,5][2,4]\t[1,6][3,0]
  \n[7][5]\t[2][4]\t[1][6]\t[3][0]
  \n[5,7][2,4]\t[1,6][0,3]
  \n[2,4,5,7]\t[0,1,3,6]
  \n[0,1,2,3,4,5,6,7]

  """
  center_index = len(arr) // 2
  left = arr[:center_index]
  right = arr[center_index:]

  if len(left) > 1:
    left = merge_sort(left, reverse)
  if len(right) > 1:
    right = merge_sort(right, reverse)

  return merge(left, right, reverse)


def quicksort(arr: list[object], reverse=False) -> list[object]:
  if len(arr) <= 1:
    return arr

  center_index = ran(0,len(arr))
  left = []
  pivot = [arr[center_index]]
  right = []

  for i in range(len(arr)):
    if i == center_index:
      continue
    
    if arr[i] == pivot[0]:
      pivot.append(arr[i])
    elif compare(arr[i], pivot[0], reverse):
      left.append(arr[i])
    else:
      right.append(arr[i])
  

  return quicksort(left, reverse) + pivot + quicksort(right, reverse)
