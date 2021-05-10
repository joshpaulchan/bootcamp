"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""

from functools import lru_cache

@lru_cache
def insert_parentheses(string):
  spots_to_insert = [
    i for i, char in enumerate(string) if char == ")"
  ]
  permutations = []
  for spot in spots_to_insert:
    permutations.append(string[0:spot] + "()" + string[spot:])

  permutations.append(string + "()")
  
  return permutations


def test_insert_parentheses():
  assert insert_parentheses("") == ["()"]
  assert insert_parentheses("()") == ["(())", "()()"]
  ans = insert_parentheses("(())")
  expected = ["((()))", "(()())", "(())()"]
  assert ans == expected, f"expected {expected}, got {ans}"

# test_insert_parentheses()

def generate_parentheses(n):
  answer = set([])
  queue = [""]
  
  while queue:
    permutation = queue.pop(0)

    if len(permutation) == 2*n:
      answer.add(permutation)
    
    for p in insert_parentheses(permutation):
      if len(p) <= 2*n:
        queue.append(p)

  return list(answer)

# print(generate_parentheses(1))
print(generate_parentheses(2))
# print(generate_parentheses(3))

print(generate_parentheses(4))

