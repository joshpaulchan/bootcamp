
# Must Do Medium https://leetcode.com/list/5nh40bzr/
# Must Do Easy https://leetcode.com/list/5nh40hst/

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400


[1, 2, 3, 1, 5]
[2, 1, 1, 2]

(list[0] + loot(0 + 2), loot(0 + 1))
(list[2] + loot(4), loot(3))


"""

from functools import lru_cache

def cached_dp_rob(numbers: list) -> int:
  """
    2             1             2
  loot(0) --> (1 + loot(2)) vs loot(1)
    2             2             1
  loot(1) --> (1 + loot(3)) vs loot(2)
    1             1             1
  loot(2) --> (1 + loot(4)) vs loot(3)
    1             0             0
  loot(3) --> (1 + loot(5)) vs loot(4)

  """
  @lru_cache(maxsize=None)
  def loot(index: int) -> int:
    if index >= len(numbers):
      return 0
    else:
      return max(numbers[index] + loot(index + 2), loot(index + 1))
      
  x = loot(0)
  print(x)
  return x



def iter_dp_rob(numbers: list) -> int:
  sum_outside = 0
  sum_next = 0
  full_sum = 0

  i = 0
  while True:
    if i + 2 >= len(numbers):
      break

    sum_outside = full_sum + numbers[i] + numbers[i + 2]
    sum_next = full_sum + numbers[i + 1]

    if sum_outside > sum_next:
      i += 2
      full_sum = sum_outside
    else:
      i += 1
      full_sum = sum_next
    
  print(full_sum)
      
  return full_sum


def test_rob(rob):
  print(f"testing {rob.__name__}")

  assert rob([1 ,2, 3, 1]) == 4
  assert rob([1, 2, 3, 1, 5]) == 9
  assert rob([2, 1, 1, 2]) == 4

  print(f"passed {rob.__name__}")


# test_rob(cached_dp_rob)
# test_rob(iter_dp_rob)

"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

from collections import deque

class Node:

  def __init__(self, value=None, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    return f"{self.left}<-{self.value}->{self.right}"
  
  def __repr__(self):
    return str(self)

  def __eq__(self, other):

    return self.value == other.value and self.left == other.left and self.right == other.right


def invert_bfs(root: Node):
  queue = deque([root])

  while queue:
    tempNode = queue.popleft()
    if tempNode:
      tempNode.right, tempNode.left = tempNode.left, tempNode.right
      queue.append(tempNode.left)
      queue.append(tempNode.right)
  
  return root


def invert_dfs(root: Node):
  children = deque([root])

  while children:
    node = children.pop()
    if node:
      node.right, node.left = node.left, node.right
      children.append(node.left)
      children.append(node.right)
  
  return root


def invert_dfs_recursive(root: Node):
  if root:
    root.right, root.left = root.left, root.right
    invert_dfs(root.left)
    invert_dfs(root.right)
  
  return root


def test_invert(invert):
  print(f"testing {invert.__name__}")

  tree = Node(4,
      Node(2,
          Node(1),
          Node(3)
        ),
      Node(7,
          Node(6),
          Node(9)
        )
    )
  expected = Node(4,
      Node(7,
          Node(9),
          Node(6)
        ),
      Node(2,
          Node(3),
          Node(1)
        )
    )
  print(tree)
  print(expected)

  assert invert(tree) == expected
  
  print(f"passed {invert.__name__}")

test_invert(invert_bfs)
test_invert(invert_dfs)
test_invert(invert_dfs_recursive)