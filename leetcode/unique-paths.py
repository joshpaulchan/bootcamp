"""
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

1    
1 
1 
 

0,0 - top left
m,n - bottom right

"""

import dataclasses
import functools

@dataclasses.dataclass(frozen=True)
class Location:
  x: int
  y: int
  
  def above(self):
    return Location(self.x, self.y - 1)
  
  def left(self):
    return Location(self.x - 1, self.y)


@functools.lru_cache
def _unique_paths(location: Location) -> int:
  if location.x == 0 or location.y == 0:
    return 1

  return _unique_paths(location.above()) + _unique_paths(location.left())


def unique_paths(num_rows, num_cols):
  return _unique_paths(Location(num_rows - 1, num_cols - 1))

@functools.lru_cache
def _unique_paths2(x, y) -> int:
  if x == 0 or y == 0:
    return 1

  return _unique_paths2(x - 1, y) + _unique_paths2(x, y - 1)


def unique_paths2(num_rows, num_cols):
  return _unique_paths2(num_rows - 1, num_cols - 1)

def test_unique_paths(unique_paths):
  print(f"Testing {unique_paths.__name__}...")

  cases = [
    ((3, 1), 1),
    ((1, 3), 1),
    ((3, 2), 3),
    ((2, 3), 3),
    ((3, 7), 28),
    ((7, 3), 28),
    ((10, 10), 48620)
  ]

  for args, expected in cases:
    print(f"testing {args}")
    result = unique_paths(*args)

    assert result == expected, f"expected: {expected}, got: {result}"

  print(f"{unique_paths.__name__} passed.")

test_unique_paths(unique_paths)
test_unique_paths(unique_paths2)

# bottom-up solution, space optimized

# Space (R*C) -> SC (C)

'''
1 1 1 1 1
1 2 3 4 5
1 0 0 0 0

'''

# Space Complexity: O(min(R, C))
def unique_paths3(r, c):

  if r < c:
    r, c = c, r

  dp = [1] * c

  for i in range(1, r):
    dp2 = [0] * c
    dp2[0] = 1

    for j in range(1, c):
      # dp[i][j] = dp[i-1][j] + dp[i][j-1]
      dp2[j] =  dp[j] + dp2[j-1]
    
    dp = dp2

  return dp[-1]

test_unique_paths(unique_paths3)
