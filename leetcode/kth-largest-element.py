
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Returns the element representing the kth largest element in the stream.

class NaiveKLargest:
  
  def __init__(self, k, nums: list):
    self.k = k
    self.nums = nums
  
  def add(self, n: int):
    self.nums.append(n) # O(n) amortized
    self.nums.sort() # O(nlogn)
    return self.nums[-self.k] # O(1)


class SlightlyBetterKLargest:
  
  def __init__(self, k, nums: list):
    self.k = k
    self.nums = nums
    # 1. turn this into linked list to optimized insertions + deletions
    # 2. sort, slice into max k elements
  
  def add(self, n: int):
    # if n < self.nums[0]: return
    self.nums.append(n) # O(n) amortized
    self.nums.sort() # O(nlogn)
    return self.nums[-self.k] # O(1)

class BinaryTreeKLargest:

  class TreeNode:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

  class Tree:

    def __init__(self, head):
      self.head = head

    def addToTree(self,num):
      pointer = self.head
      # add value to tree
    
  
  def __init__(self, k, nums: list):
    self.k = k
    self.nums = nums
    # 1. build BST from top k nums

  
  def add(self, n: int):
    # binary insertion
    # pop off whatever is extra to ensure k
    # return k
    pass
  

def test_k_largest(k_largest):
  print(f"testing {k_largest.__name__}")
  
  largest = k_largest(3, [4, 5, 8, 2])
  assert largest.add(5) == 5   # return 5
  assert largest.add(3) == 4   # return 4
  assert largest.add(10) == 5  # return 5
  assert largest.add(9) == 8   # return 8
  assert largest.add(4) == 8   # return 8

  print(f"{k_largest.__name__} passed")

# test_k_largest(NaiveKLargest)
# test_k_largest(BinaryTreeKLargest)


"""
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1]

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
"""

def longest_continuous_increasing_subsequence(nums):
  if len(nums) == 0:
    return 0

  # should return length
  greatest_length_so_far = counter = 1
  last_num = nums[0]

  for num in nums[1:]:

    if num > last_num:
      counter += 1
      
    else: 
      if greatest_length_so_far < counter:
        greatest_length_so_far = counter
      counter = 1
      
    last_num = num

  if greatest_length_so_far < counter:
    greatest_length_so_far = counter

  return greatest_length_so_far


def test_longest_continuous_increasing_subsequence(lcis):
  print(f"testing {lcis.__name__}")

  assert lcis([1,3,5,4,7]) == 3, f"was {lcis([1,3,5,4,7])}"
  assert lcis([2,2,2,2,2]) == 1, f"was {lcis([2,2,2,2,2])}"

  print(f"{lcis.__name__} passed")

test_longest_continuous_increasing_subsequence(longest_continuous_increasing_subsequence)