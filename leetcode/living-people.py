
# 16.10 Living People
"""
Given a list of people with their birth and death years, implement a method to
compute the year with the most number of people alive. You may assume that all people were born between 1900 and 2000 (inclusive). If a person was alive during any portion of that year, they should be included in that year's count. For example, Person (birth = 1908, death = 1909) is included in the counts for both 1908 and 1909.

hm = {0: 0, ...,  100: 0}

[[1908, 1954], [1930, 2000], [1945, 2005]]

NlogN

L M R
  L R
L R

mid = 50

"""

class Person:
  def __init__(self, birth_date, end_date):
    self.birth_date = birth_date
    self.end_date = end_date
  
  def __repr__(self):
    return f"Person({self.birth_date} - {self.end_date})"

  
def living_people_naive_allocation(people):
  years = [0 for i in range(0, 1000)] # 0 -> 1900; 1000 -> 2000

  # 100 (~M constant) * N 
  for p in people:
    for year in range(p.birth_date, p.end_date):
      years[year % 1900] += 1

  # 100 units search
  return years.index(max(years)) + 1900


class SegmentNode:
  def __init__(self, start, end, count=0, left=None, right=None):
    self.start = start
    self.end = end
    self.count = count
    self.left = left
    self.right = right


class Node:

  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.val = None
    self.left = None
    self.right = None

'''

nums = [1, 6, 20, 100, 2034] -> sum(1, 3)

input: [[1, 3], [3, 4], [0, 4]]

output: [126, 2134, 2161]

[[0, len(nums) - 1], [0, len(nums) - 1], [0, len(nums) - 1]]

3*3 = N^2 -> NlogN

N - build segment tree + 100*logN

[1901, 1901]

TC
100*N vs N + 100logN

10^12 vs 10^10 + 10^3

SC
100 vs logN

N = 10^10


Segment Tree question
https://leetcode.com/problems/range-sum-query-mutable/
https://www.youtube.com/watch?v=CN0N1ddJ9hA&t=514s

'''
class SegmentTree:
  def __init__(self, nums):
    self.root = self._buildTree(nums, 0, len(nums) - 1)
    
  def _buildTree(self, nums, start, end):
      
    if start > end:
      return None
    
    if start == end:
      node = Node(start, end)
      node.val = nums[start]
      return node
    
    node = Node(start, end)
    mid = (start + end) // 2
    
    node.left = self._buildTree(nums, start, mid)
    node.right = self._buildTree(nums, mid + 1, end)
    node.val = node.left.val + node.right.val
    return node

  def update(self, i: int, val: int) -> None:
    self._update(self.root, i, val)
      
  def _update(self, node, i, val):
    if node.start == node.end:
      node.val = val
      return
    
    mid = (node.start + node.end) // 2
    if i <= mid:
      self._update(node.left, i, val)
    else:
      self._update(node.right, i, val)
    node.val = node.left.val + node.right.val

  def sumRange(self, i: int, j: int) -> int:
    return self._search(self.root, i, j)
    
  def _search(self, node, i, j):
    if node.start == i and node.end == j:
      return node.val
    
    mid = (node.start + node.end) // 2

    if j < mid + 1:
      return self._search(node.left, i, j)
    elif i > mid:
      return self._search(node.right, i, j)
    return self._search(node.left, i, mid) + self._search(node.right, mid + 1, j)


def living_people_with_segment_tree(fn):
  pass


def test_living_people(fn):
  people = [
    Person(1908, 1954),
    Person(1930, 2000),
    Person(1945, 2005)
  ]
  
  answer = fn(people)
  print(f"{fn.__name__}({people}) = {answer}")
  assert answer in range(1945, 1954)

test_living_people(living_people_naive_allocation)
test_living_people(living_people_with_segment_tree)