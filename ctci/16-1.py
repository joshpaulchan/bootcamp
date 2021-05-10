
import math
import random

# 16.1

# Number Swapper: Write a function to swap two numbers in place (that is, without temporary variables)

def swap(a, b):
  b = a - b
  a = a - b
  b = a + b
  return a, b

def test_swap():

  print((75, 25) == swap(25, 75))
  print((1000, 25) == swap(25, 1000))

test_swap()