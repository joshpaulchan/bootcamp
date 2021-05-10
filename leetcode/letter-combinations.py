"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 
Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


"1234"

3^n ~ exponential
quadratic n^2
cubic n^3

["a", "b", "c"]

23,
["ca", "a", "a" "b", "b", "b", ", "c", "c"]


["*f","*e","*d"]
["*f","*e","*d"]-> 
for each * 
["ad","bd","cd"] + ["ad","bd","cd"] + ["af","bf","cf"]
[]

  2 3 



              i = 0
        /     |      \
  a           b        c
             i = 1
d e f        d e f    d e f

curr = []

curr.append('a') or curr.append('b')
['a']

i
v
343353534


 0   1
'2   3'


give me all combinations of numbers where sum = 6

arr = [2, 3, 5, 7]

ans = [[2, 2, 2], [3, 3]]

for i in range(idx, len(arr))


n * 3 ^ n

Time Complexity: O(N * (4 ^ N))
Space Complexity: O(N)

"""

def letterCombinations(digits: str) -> list:
  phone_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
  }

  if len(digits) == 0:
    return []

  if len(digits) == 1:
    return phone_map[digits]

  result = []
  def backtrack(i, curr):

    if i == len(digits):
      result.append(''.join(curr))
      return

    for c in phone_map[digits[i]]:
      curr.append(c)
      backtrack(i + 1, curr)
      curr.pop() 
  
  curr = []
  backtrack(0, curr)
  return result


def letter_combinations_generator(digits: str) -> list:
  phone_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
  }

  if len(digits) == 0:
    return []

  def backtrack(i=0, curr=""):
    if i == len(digits):
      return curr

    for c in phone_map[digits[i]]:
      # FIXME: gotta drain the generator someone?
      yield backtrack(i + 1, curr + c)
  
  return backtrack()


def test_letter_combos(letter_combos):
  print(f"testing {letter_combos.__name__}")

  # Example 1:

  # Input: digits = "23"
  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

  print("testing '23'")
  assert set(letter_combos("23")) == {"ad","ae","af","bd","be","bf","cd","ce","cf"}

  # Example 2:

  # Input: digits = ""
  # Output: []

  print("testing ''")
  assert letter_combos("") == []

  # Example 3:

  # Input: digits = "2"
  # Output: ["a","b","c"]

  print("testing '2'")
  assert set(letter_combos("2")) == {"a", "b", "c"}

  print(f"{letter_combos.__name__} passed")

# test_letter_combos(letterCombinations)

for permutation in letter_combinations_generator("23"):
  print(permutation)
  


# Alternate solution
import itertools
def letter_combinations(digits: str) -> list:
  phone_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
  }

  if len(digits) == 0:
    return []

  if len(digits) == 1:
    return phone_map.get(digits)
  

  l = []

  for c in digits:
    l.append(phone_map.get(c))

  return list(''.join(x) for x in itertools.product(*l))
  

def letter_combinations_generator(digits: str) -> list:

  def gen_list(l):
    return (x for x in l)
  
  phone_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
  }
  q = []
  for c in digits:
    q.append(gen_list(phone_map.get(c)))
  
  print(q)

print('h')  
print(letter_combinations('23'))
