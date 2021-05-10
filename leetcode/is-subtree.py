# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    # def __str__(self):
    #   return f"{self.left}<-{self.val}->{self.right}"

def isSubtree(s: TreeNode, t: TreeNode) -> bool:
  """
     3
    / \
   4   5
  / \
 1   2


  s = Node(3, Node(4,Node(1), Node(2)), Node(5))
  t = Node(4, Node(1), Node(2))

  """
  pointer = t
  # if not s:
  #   return False
  # if matchTrees(s, t):
  #   return True
  # else:
  #   return isSubtree(s.left, t) or isSubtree(s.right, t)
  while pointer.value != s.value:
    if pointer.value < s.value:
      pointer = s.left
    else: 
      pointer= s.right

  if pointer.value == s.value:
    matchTrees(s, pointer)

  


def matchTrees(s: TreeNode, t: TreeNode) -> bool:
  if not s and not t:
    return True
  elif not s or not t:
    return False
  elif s.val != t.val:
    return False
  return matchTrees(s.left, t.left) and matchTrees(s.right, t.right)



def match(s: TreeNode, t: TreeNode) -> bool:
  if s == t:
    return True
  # if s !== :
  return matchTrees(s.left, t.left) and matchTrees(s.right, t.right)



# Ryan: Got this working in leetcode:
# Time complexity: O(N*M) Where N is the depth of Tree. Space Complexity: O(1) 
class Solution:
  def __init__(self):
    self.calledST = 0
    self.calledMT = 0

  def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
      self.calledST += 1    # understanding TC
      if not s:
          return False
      if self.matchTrees(s, t):
          return True
      return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

  # TC: O(T)    
  def matchTrees(self, s: TreeNode, t: TreeNode) -> bool:
      self.calledMT += 1    # understanding TC
      if not s and not t:
          return True
      elif not s or not t:
          return False
      elif s.val != t.val:
          return False
      else:
          return self.matchTrees(s.left, t.left) and self.matchTrees(s.right, t.right)

# Depth at 0
mainTree = TreeNode(4,
  TreeNode(1),
  TreeNode(2)
  )

# Depth at 1
mainTree = TreeNode(3,
  TreeNode(4,
    TreeNode(1),
    TreeNode(2)
    ),
  TreeNode(5)
)

# Depth at 2
mainTree = TreeNode(3,
  TreeNode(9,
    TreeNode(4,
      TreeNode(1),
      TreeNode(2)
      ),
    TreeNode(9)
  ),
  TreeNode(5)
)

subTree = TreeNode(4,
  TreeNode(1),
  TreeNode(2)
  )

# print(mainTree)
# print(subTree)
# print(matchTrees(mainTree, subTree))

# x = Solution()
# print(x.isSubtree(mainTree, subTree))
# print(f"matchTrees called {x.calledMT} times.")
# print(f"isSubtree called {x.calledST} times.")




