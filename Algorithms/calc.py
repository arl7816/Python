import math

def diff(f: function, x: int, h=0.000000001) -> int:
  return (f(x+h)-f(x))/h


def integrate(f: function, a: int, b: int, n=10000) -> int:
  total = 0
  deltaX = (b-a)/n

  index = 1

  for _ in range(n):
    total += f(a+index*deltaX)*deltaX
    index += 1
  return total

def mean_value(f: function, a: int, b: int) -> int:
  return (f(b) - f(a)) / (b-a)


class Matrix:
  pass


class Vector:
  pass