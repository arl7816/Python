import math

def diff(f, x: int, h=0.000000001) -> int:
  return (f(x+h)-f(x))/h

def base_integrate(f, a: int, b: int, n: int, k: int) -> float:
  total = 0
  deltaX = (b-a)/n

  for _ in range(n):
    total += (f(a+k*deltaX)*deltaX)
    k += 1
  return total

def trapezoid_integration(f, a: int, b: int, n: int) -> float:
  deltaX = (b-a)/n

  fo = f(a)
  fn = f(a + n*deltaX)

  total = 0
  for k in range(1,n):
    total += (2*f(a + k*deltaX))

  total = (deltaX/2)*(fo + fn + total)
  return total

def simp_integrate(f, a: int, b: int, n: int) -> float:
  deltaX = (b-a)/n

  fo = f(a)
  fn = f(a + n*deltaX)

  total = 0
  for k in range(1,n):
    total += (2*(1+(k % 2)) * f(a + k*deltaX))
  
  total = (deltaX/3) * (fo+fn+total)
  return total

def integrate(f, a: int, b: int, method: str, n=100) -> float:
  total = None

  if method == "left":
    total = base_integrate(f, a, b, n, 0)
  elif method == "mid":
    total = base_integrate(f, a, b, n, 0.5)
  elif method == "trapezoid":
    total = trapezoid_integration(f, a, b, n)
  elif method == "simp":
    total = simp_integrate(f, a, b, n)
  else: 
    # right hand method --> most common
    total = base_integrate(f, a, b, b, 1)
  
  return total

def mean_value(f, a: int, b: int) -> int:
  return (f(b) - f(a)) / (b-a)


def ln(x: int, n=100) -> float:
  def f(x: int) -> float:
    return 1/x

  return integrate(f, 1, x, "simp", n)

def loga(a: int, b: int, n=100) -> float:
  lna = ln(a, n)

  def f(x: int) -> float:
    return 1/(x*lna)

  return integrate(f, 1, b, "simp", n)

class Matrix:
  pass


class Vector:
  pass